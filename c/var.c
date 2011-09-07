#include <stdio.h>
#include <stdlib.h>


void pibr(int  *);
void piPtrbr(int **);


int main(int argc, char *argv[])

{

	int a = 0; // pointer to an int.
	pibr(&a);


	printf("A is now: %d.\n", a);

	int * buffer;
	piPtrbr(&buffer);
	
	printf("buffer[0]: %d.\n", buffer[0]);
	printf("buffer[1]: %d.\n", buffer[1]);
	getchar();

	free(buffer);	
	return 0;


}

void pibr( int *b){

	printf("address of b %p\n", b);
	*b = 314;
}

void piPtrbr(int **val){

	*val= malloc(2* sizeof (*val) );
	**val = 33;
	
//	(**val)++;// inc data
	(*val)++; // inc referenced pointer
	**val=100; // assign to start of referenced ptr.
	(*val)-- ; //dec referenced pointer
	**val  =38;
	(*val)[1] = 56; // assign to referenced ptr

	// (*ptr) // deref to ptr's val (contained ptr)
	// (*ptr)[0] // deref to contained ptr's val - an int;  
	// *(*ptr) // ref ptr to ref val;
}
