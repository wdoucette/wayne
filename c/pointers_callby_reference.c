#include <stdio.h>
#include <stdlib.h>


void f(int **);

int main(int argc, char *argv[])
{
	
	int *a = NULL;
	f(&a);

	printf("a[0]= %d", a[0]);

	free(a);
	return 0;


}

	
void f(int **c){

	*c = malloc(2 * sizeof (int) );
	(*c)[0] =2;
	(*c)[1] =3;

}


