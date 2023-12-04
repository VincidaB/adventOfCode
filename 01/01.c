/* Vincent Belpois */
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>



int main(){
	char buf;
	char first, last;
	int sum = 0;
	while(1){
		scanf("%c", &buf);
		int i = 0;
		if(!first && isdigit(buf))
			first = buf;
		if(isdigit(buf))
			last = buf;
		if(buf == '\n'){
			printf("%c%c\n",first,last);
			first = '\0';
			last = '\0';
		}
	}
	return  0;
}
