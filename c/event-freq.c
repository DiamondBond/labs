/* gcc -g -o event-freq `pkg-config --libs --cflags gtk4` event-freq.c */
#include <gtk/gtk.h>

static guint timeout_id = 0;
static GQueue *evqu = NULL;

typedef struct
{
  uint32_t evtime;
  uint64_t time;
} TimeInfo;

GdkRGBA bucket_colors[8] = {
  { 0, 1, 0, 1 }, /* < 2 ms */
  { 0.1, 0.8, 0, 1 }, /* 2-3 ms */
  { 0.3, 0.6, 0, 1 }, /* 4-7 ms */
  { 0.9, 0.8, 0, 1 }, /* 8-15 ms */
  { 1, 0.4, 0, 1 }, /* 16-31 ms */
  { 1, 0.0, 0, 1 }, /* 32-63 ms */
  { 0.7, 0.0, 0.3, 1 }, /* 64-127 ms */
  { 0.6, 0.0, 0.5, 1 }, /* >= 128 ms */
};

const char *bucket_labels[8] = {
  "< 2ms",
  "2-3ms",
  "4-7ms",
  "8-15ms",
  "16-31ms",
  "32-63ms",
  "64-127ms",
  ">= 128ms",
};

gboolean
timeout_cb (GtkDrawingArea *drawing_area)
{
  gtk_widget_queue_draw (GTK_WIDGET (drawing_area));
  timeout_id = 0;
  return G_SOURCE_REMOVE;
}

static void
paint_progressbar_trough (cairo_t *cr,
                          int      width)
{
  cairo_save (cr);
  cairo_rectangle (cr, 0.5, 0.5, width, 40);
  cairo_set_source_rgb (cr, 0, 0, 0);
  cairo_stroke (cr);
  cairo_restore (cr);
}

static void
paint_progressbar_elem (cairo_t *cr,
                        GdkRGBA *color,
                        int      width,
                        double   start,
                        double   len)
{
  cairo_save (cr);
  cairo_translate (cr, width * start, 0);
  cairo_rectangle (cr, 0.5, 0.5, width * len, 40);
  gdk_cairo_set_source_rgba (cr, color);
  cairo_fill (cr);
  cairo_restore (cr);
}

static void
paint_label (cairo_t     *cr,
             const gchar *str)
{
  PangoLayout *layout;

  layout = pango_cairo_create_layout (cr);
  pango_layout_set_markup (layout, str, -1);
  pango_cairo_show_layout (cr, layout);
  g_object_unref (layout);
}

static void
motion_cb (GtkEventControllerMotion *controller,
           double x, double y,
           GtkDrawingArea *drawing_area)
{
  TimeInfo *info;
  uint32_t evtime;
  uint64_t handled_time;

  handled_time = g_get_monotonic_time ();
  evtime = gtk_event_controller_get_current_event_time (GTK_EVENT_CONTROLLER (controller));
  info = g_new0 (TimeInfo, 1);
  *info = (TimeInfo) { evtime, handled_time };

  g_queue_push_tail (evqu, info);

  if (timeout_id == 0)
    timeout_id = g_timeout_add (100, (GSourceFunc) timeout_cb, drawing_area);
}

static void
clear_queue_before (GQueue  *evqu,
                    int32_t  evtime)
{
  TimeInfo *info;

  while ((info = g_queue_peek_head (evqu)) != NULL)
    {
      if (info->evtime < evtime)
        {
          g_free (info);
          g_queue_pop_head (evqu);
        }
      else
        break;
    }
}

static void
drawing_area_draw (GtkDrawingArea *area,
                   cairo_t        *cr,
                   int             width,
                   int             height,
                   gpointer        data)
{
  int n_events, diff, i;
  int min_dev = G_MAXINT, max_dev = 0, avg_dev = 0;
  TimeInfo *first, *last, *info, *info2;
  gdouble ev_per_sec, scale, start;
  guint time_buckets[8] = { 0 };
  guint latency_buckets[8] = { 0 };
  PangoLayout *layout;
  GList *l;
  gchar *str;

  last = g_queue_peek_tail (evqu);
  if (!last)
    return;

  clear_queue_before (evqu, last->evtime - 1000);

  n_events = g_queue_get_length (evqu);
  if (n_events <= 1)
    return;

  first = g_queue_peek_head (evqu);
  if (!first || first == last)
    return;

  diff = (last->evtime - first->evtime);
  if (diff == 0)
    return;

  scale = 1000 / diff;
  ev_per_sec = n_events * scale;

  for (l = evqu->head; l != NULL; l = l->next)
    {
      TimeInfo *info, *info2 = NULL;
      int64_t lat_diff;

      info = l->data;
      if (l->next)
        info2 = l->next->data;

      if (info2)
        {
          diff = (int) info2->evtime - info->evtime;
          min_dev = MIN (min_dev, diff);
          max_dev = MAX (max_dev, diff);
          avg_dev += diff;

          for (i = G_N_ELEMENTS (time_buckets) - 1; i >= 0; i--)
            {
              if (diff >= (1 << i) || i == 0)
                {
                  time_buckets[i] += 1;
                  break;
                }
            }
        }


      lat_diff = info->time - ((int64_t) info->evtime * 1000);

      for (i = G_N_ELEMENTS (latency_buckets) - 1; i >= 0; i--)
        {
          if (lat_diff >= ((1 << i) * 1000) || i == 0)
            {
              latency_buckets[i] += 1;
              break;
            }
        }
    }

  avg_dev = avg_dev / (n_events - 1);

  /* Print events per second */
  cairo_translate (cr, 50, 0);

  cairo_translate (cr, 0, 50);
  cairo_save (cr);
  cairo_translate (cr, -25, 0);
  paint_label (cr, "<big><b>Frequency</b></big>");
  cairo_restore (cr);

  cairo_translate (cr, 0, 50);
  paint_progressbar_elem (cr,
                          &(GdkRGBA) { 0.3, 0.3, 0.3, 1 },
                          width - 100, 0, CLAMP (ev_per_sec / 1000, 0, 1));
  paint_progressbar_trough (cr, width - 100);

  cairo_translate (cr, 0, 50);
  str = g_strdup_printf ("%d Ev/Sec", (int) ev_per_sec);
  paint_label (cr, str);
  g_free (str);

  /* Print stats about event separation */
  cairo_translate (cr, 0, 50);
  cairo_save (cr);
  cairo_translate (cr, -25, 0);
  paint_label (cr, "<big><b>Separation</b></big>");
  cairo_restore (cr);

  cairo_translate (cr, 0, 50);
  start = 0;

  for (i = 0; i < G_N_ELEMENTS (time_buckets); i++)
    {
      double len = (double) time_buckets[i] / (n_events - 1);

      paint_progressbar_elem (cr,
                              &bucket_colors[i],
                              width - 100,
                              start, len);
      start += len;
    }

  paint_progressbar_trough (cr, width - 100);

  cairo_translate (cr, 0, 50);
  str = g_strdup_printf ("Mean diff: %dms, Min. diff: %dms, Max. diff: %dms",
                         avg_dev, min_dev, max_dev);
  paint_label (cr, str);
  g_free (str);

  /* Print latency stats */
  cairo_translate (cr, 0, 50);
  cairo_save (cr);
  cairo_translate (cr, -25, 0);
  paint_label (cr, "<big><b>Latency</b></big>");
  cairo_restore (cr);

  cairo_translate (cr, 0, 50);
  start = 0;

  for (i = 0; i < G_N_ELEMENTS (time_buckets); i++)
    {
      double len = (double) latency_buckets[i] / n_events;

      paint_progressbar_elem (cr,
                              &bucket_colors[i],
                              width - 100,
                              start, len);
      start += len;
    }

  paint_progressbar_trough (cr, width - 100);

  /* Print legend */
  cairo_translate (cr, 0, 50);
  cairo_save (cr);
  cairo_translate (cr, -25, 0);
  paint_label (cr, "<big><b>Legend</b></big>");
  cairo_restore (cr);

  cairo_translate (cr, 0, 50);

  for (i = 0; i < G_N_ELEMENTS (bucket_colors); i++)
    {
      cairo_save (cr);

      cairo_translate (cr, (i % 4) * 80, (i / 4) * 50);

      cairo_rectangle (cr, 0, 0, 24, 24);
      gdk_cairo_set_source_rgba (cr, &bucket_colors[i]);
      cairo_fill (cr);

      cairo_move_to (cr, 0, 32);
      cairo_set_source_rgb (cr, 0, 0, 0);
      cairo_show_text (cr, bucket_labels[i]);
      cairo_fill (cr);

      cairo_restore (cr);
    }
}

static gboolean
close_request_cb (GtkWindow *window,
                  GMainLoop *loop)
{
  g_main_loop_quit (loop);
  return TRUE;
}

int
main (int argc, char *argv[])
{
  GtkWidget *window, *drawing_area;
  GMainLoop *loop;
  GtkEventController *mot;

  evqu = g_queue_new ();
  loop = g_main_loop_new (NULL, FALSE);

  gtk_init ();

  window = gtk_window_new ();
  gtk_window_set_title (GTK_WINDOW (window), "Wiggle your mouse here");
  drawing_area = gtk_drawing_area_new ();
  gtk_window_set_child (GTK_WINDOW (window), drawing_area);
  gtk_window_maximize (GTK_WINDOW (window));

  g_signal_connect (window, "close-request",
                    G_CALLBACK (close_request_cb), loop);

  gtk_drawing_area_set_draw_func (GTK_DRAWING_AREA (drawing_area),
                                  drawing_area_draw,
                                  NULL, NULL);

  mot = gtk_event_controller_motion_new ();
  g_signal_connect (mot, "motion", G_CALLBACK (motion_cb), drawing_area);
  gtk_widget_add_controller (window, mot);
  gtk_widget_show (window);

  g_main_loop_run (loop);

  return 0;
}
