flex ps2.l
bison -d ps2.y
cc lex.yy.c ps2.tab.c
./a.out < in > out
