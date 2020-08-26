#define EOI			0	/* EOF	*/
#define SEMI		1	/* ;	*/
#define PLUS		2	/* +	*/
#define TIMES		3	/* *	*/
#define LP			4	/* (	*/
#define RP			5	/* )	*/
#define NUM_OR_ID	6	/* num	*/

extern char *yytext;
extern int yyleng;
extern int yylineno;
