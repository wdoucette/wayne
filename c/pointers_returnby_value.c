#include<stdio.h>
#include<stdlib.h>

int * f(void);

int main(int argc, char *argv[])
{

	int *a =NULL;
	
	a=f();

	printf("a[0]=%i\n", a[0]);
	printf("a[1]=%i\n", a[1]);
//	printf("*a=%i\n", *a);
//	printf("*(++a)=%i\n", *(++a));

	free(a);
	return 0;

}


int *f(void)
{
	int *c = malloc(  2 * sizeof (int) );
	c[0]=10;
	c[1]=20;

	// Return by value -local pointer dies, but persists as copy.
	return c;

}

