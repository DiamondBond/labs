from dearpygui.dearpygui import *

add_text("Hello world")
add_button("Save", callback="save_callback")
add_input_text("string")
add_slider_float("float")

def save_callback(sender, data):
    print("Save Clicked")

start_dearpygui()
