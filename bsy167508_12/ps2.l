%{
	#include <stdio.h>
	#include <string.h>
	#include <stdlib.h>
	#include "ps2.tab.h"
	
	const char s[2] = "/";
	int arr[2]={0,0};
%}
EN	"2016BSY750"[0-9]
CC	"ELL81"[0-9]
GRADE	{CC}"/"[1-9]"/"[1-9]
AUDIT	{CC}"/"[1-9]"/"("NP"|"P")"/A"
DROP	{CC}"/"[1-9]"/D"
NAME	[a-zA-Z]*
%option noyywrap
%%

{DROP}			{ yylval.flo=0.00; printf(" %s",yytext);
			return TOKDROP;
   			}
			

{AUDIT}			{  yylval.flo=0.00; printf(" %s",yytext);
			return TOKAUDIT;
   			}

{GRADE}			{ yylval.str=strdup(yytext); printf(" %s",yytext);
			return TOKGRAD;
			}
.			{ ;
			}
