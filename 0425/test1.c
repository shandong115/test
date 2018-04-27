#include <stdio.h>
#include <string.h>
int is_num(char c){
	if(c>='0'&&c<='9')
	  return 1;
	else if((c>='a'&&c<='z')||(c>='A'&&c<='Z'))
	  return 2;

	return 0;
}
int func(char *str, int *len){
	char *p1=NULL,*p2=NULL, *p3=str;
	int flag1=0, flag2=0;
	int len1=0, len2=0;
	char c;
	int Len=strlen(str);

	while(Len){
		c=p3[0];
		printf("c=%c\n",c);
		if(is_num(c) == 1){
			if(flag1 == 0){//change into number
				printf("change into number\n");
				flag1 = 1;
				flag2 = 0;
				p2 = p3;
				if(p1 == NULL){
					p1 = p3;
				}
			}
			else
				len2 = p3 - p2 + 1;
		}
		else if(is_num(c) == 2){
			if(flag2 == 0 && flag1 == 1){ //change into character
				printf("change into character\n");
				len2 = p3 - p2;
				if(len1<len2){
					p1 = p2;
					len1 = len2;
				}
				flag1 = 0;
				flag2 = 1;
			}
		}
		p3++;
		Len--;
	}
	if(len1 == 0)len1 = len2;
	*len = len1;
	return p1 - str;
}
int main(int argc, char *argv[]){
	//char *str = "a1235bdmn25916fgzn21a47abcde";
	//char *str = "a1235b";
	char sBuf[1024] = { 0 };
	int index = 0, len = 0;
	char *str = argv[1];
	printf("str:%s\n",str);
	index = func(str, &len);	
	memset(&sBuf, 0x00, sizeof(sBuf));
	strncpy(sBuf, str+index, len);
	printf("long str:%s|%d|%d\n", sBuf,index, len);
	return 0;
}
