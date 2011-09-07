/* =================================== includes ============================*/
#include <stdio.h>
#include <stdlib.h>
#include "test.h"
#include <string.h>
/*========================= prototypes ==========================*/
int getCmd();
void stdin2stdout();
void initStruct();
void printTests(void);
unsigned int* mallocTest(char*, char*);


#define PRINT_TOKEN(token) printf(#token " = %s\n", token);

#define MEG 1024 * 1024	

typedef struct {

	char *name;
	int number=;

} DATA;

void allocateUnits(DATA*, char);



//Globals
DATA in[2];


void allocateUnits(DATA* du, char count )
{
//	du = malloc(count * sizeof *du);
	int i;
	for(i=0;i<count;i++){

		char ch[255];// = "null";	
		sprintf(ch,"My name is number %i", i);
		printf("sprint output %s\n", "ch");
		du[i].name = "wayne";//*ch;
		du[i].number =i;
	}	

}
unsigned int *  mallocTest(char *opt, char *len) {

	
	//opt="testopt"; //can assign string literal but can not change it: opt[0]='c' -> segfault.

	unsigned int *buffer = malloc(MEG * 10 * sizeof *buffer  );//);//7 * sizeof *buffer);//[255];
	unsigned int i;

	for(i=0;i<( MEG * 2 / sizeof *buffer ) ;i++){

		//buffer[0]=i;//'c';	// really really long sting to piss you off "  ;
	//	buffer[0]='c';
		*buffer=i;
		buffer++;
	}
	buffer -= i;
	printf("Buffer is: %i\n", buffer[i-1]);
	//buffer+=1; //dumps on free if pointer out of sync.

	char str[6] = "123456";//{'t','e','s','t','i','n','g'};//"testing";
	char *str2 = opt;//"High"; 
	str[0] ='a'; 
	//str2[0] ='z'; // Segfault 
	char *mptr;
	mptr=opt;		
	mptr++;
	
	printf("sizeof str[0] (%c): %d\n", str[0], sizeof(str[0]));
	printf("sizeof str2[0] (%c): %d\n", str2[0], sizeof(str2[0]));
	printf("sizeof char: %d\n", sizeof('c'));

	char *ptr;
	ptr=str;// same as &str[0]
	ptr++;

	*ptr = 'b';

	printf("\n");
	printf("Contents of str: %s\n", (str));
	printf("Contents of str2: %s\n", (str2));
	printf("sizeof str: %d\n", sizeof(str));

	printf("sizeof str[0] is: %i\n", sizeof(str[0]));
	
	//char *addr = &str[0];
	//printf("address of str[0]: %4d\n", &addr);
	
	printf("sizeof 'a' is: %d\n", sizeof('a'));
	printf("sizeof a is: %d\n", sizeof("a"));
	printf("content of str[0]: %c\n", (str[0]));

	//str[0]='a';

	printf("opt is %s\n", opt);
	
	if(*opt =='y') {

		printf("Resizing to %i with malloc\n", atoi(len));
		//str = malloc(atoi(len) * sizeof (char) );
	} else 
		printf("Not Resizing with malloc\n");

	for(i=0; i<atoi(len); i++){

		printf("New str value is: %s\n\n", str);
		printf("Setting: %i to: %c\n", i,i);
		printf("str[i] %c\n", str[i]);
		str[1] = (char)'a';//opt;//(char)i;
	}

	printf("Allocated\n");
	getchar();

	return buffer;
}


int main(int argc, char** argv)
{
	int i;
	if(__STDC_HOSTED__) 
		printf("\n\n***Hosted***\n");
	else printf("Stand alone");
	
	char *token = "mytoken";
	PRINT_TOKEN(token);

	// Process command line arguments.	
	for(i=1 ; i < argc ; i++) {
	
		printf("Arg #%i: %s\n", i, argv[i]);
	} 

	initStruct();
	printf("Struct name is: %s\n", in[0].name);

	//doStuff("test stuff");
	//getCmd();
	//stdin2stdout();
	//printTests();	

	//unsigned int  * buffy = mallocTest(argv[1], argv[2]);
	//free(buffy);
	//printf("Freed.\n\nPress a key.");
	getchar();

	char count =atoi(argv[3]);
	printf("defining %i du's\n", count);
	DATA *du;

	printf("du size: %i\n", sizeof du);
	printf("du address: %p\n", &du);

	du = malloc(count * sizeof du);
//	du[0].name="Wayne";
//	du[0].number=1;
//	du[1].name="barney";
//	du[1].number="2";
 
 	allocateUnits(du, count );
	printf("Data units initialized.\n");

	for(i=0;i<count;i++){

		printf("Data unit number:%i\tname: %s\n", du[i].number, du[i].name);

	}

	return 0;

}

void printTests() {

	printf("put char to stream: int putc(int ch, FILE *stream\n");
	putc('c',stdout); 



}

void doStuff(char* str){

	int i=0;

	FILE *io;
	io = fopen("/tmp/testfile", "w");
	
	while(str[i] != 0 ) {
		
		printf("Writing char %c value is %d\n", str[i], str[i]);	
		putc(str[i], io);
		i++;
	}

	// Write an end of line char.
	putc(10, io);
	fclose(io);

}


int getCmd() {

	int cmd = EOF;

	printf("#");
	
	cmd=getchar();
	printf("%c", cmd);

	putc(cmd, stderr);	

	return cmd;

}

void initStruct() {

	in[0].name =  "Handsom";
	in[0].number = 1; 	 
	

}


void stdin2stdout() {



	int ch = EOF;
	char str[1024];
	
	// ptr to char array.
	char *ptr;
	ptr =&str[0];

	int count =0;

//while ((c=getc(stdin)) != EOF)
 // putc(c, stdout);

	do {	
		ch = getc(stdin);
		*ptr=ch;
		ptr++;
		count++;

	} while (ch != EOF);

	// Reset ptr to start.
	ptr =&str[0];
	
	do { 
		putc(*ptr, stdout);
		ptr++;	
	
	} while (*ptr != EOF);

 

}


