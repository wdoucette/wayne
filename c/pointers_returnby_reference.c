#include<stdio.h>
#include<stdlib.h>

int ** f(void);

int main(int argc, char *argv[])
{

	int **a;
	
	a=f();

//	printf("a[0]=%i", *a[0]);
//	printf("a[1]=%i", *a[1]);
//	printf("*a=%i", **a);
//	printf("*(++a)=%i", **(++a));

//	free(a);
	return 0;

}


int **f(void)
{
	int ** c;
	c = malloc(  2 * sizeof c );
	(*c)[0]=10;
	(*c)[1]=20;

	// Error! - returning a local variable.
	return &c;

}

