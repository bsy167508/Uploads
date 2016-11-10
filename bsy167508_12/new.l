%{
	#include <stdio.h>
	#include <string.h>
	#include <stdlib.h>
	#include "ps2.tab.h"
	
	const char s[2] = "/";
	char *arr;
%}

GRADE	"ELL81"[0-9]/[1-8]/([1-9]|"10")
AUDIT	"ELL81"[0-9]/[1-8]/("NP"|"P")/"A"
DROP	"ELL81"[0-9]/[1-8]/"D"
SKIP	([ \t]+|"2016BSY750"[0-9])
%%

{DROP}			{ arr=strtok(yytext, s);
			yylval=0;
			return TOKDROP;
			}

{AUDIT}				{ arr=strtok(yytext, s);
				yylval=0;
				return TOKAUDIT;
				}

{GRADE}				{ arr=strtok(yytext, s);
				yylval=atoi(arr[1])*atoi(arr[2]);
				return TOKGRAD;
				}

{SKIP}				;
