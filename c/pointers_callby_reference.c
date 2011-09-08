#include <stdio.h>
#include <stdlib.h>


void f(int **);

int main(int argc, char *argv[])
{
	
	int *a = NULL;
	printf("\naddress of a is %p\n", &a);
	printf("a[0]= %d\n", a[0]);
	printf("
	f(&a);

	printf("a[0]= %d\n", a[0]);


	free(a); 
	return 0;


}

	
void f(int **c){

//	*c = malloc(2 * sizeof (int) );
	puts("Now in f(int *cc)\n");
	c[0] =malloc(2* sizeof (int) ); // **c (c[0][0] now points to a

	 (*c)[0] =10;
	 (*c)[1] =20;

	printf("address of &(**c) is %p\n", &(**c));
	printf("value of (**c) is %d\n", (**c));
	printf("value of (*c)[1] is %d\n", (*c)[1]);
puts("\n");

	printf("address of &(*c) is %p\n", &(*c));
	printf("value of (*c) is %p\n", (*c));

puts("\n");
	printf("address of &c is %p\n", &c);
	printf("value of c is %p\n", c);

puts("\n");
	

	(*c)[0] =2; // **c =2
	//(*c)[1] =3; 

	*(++(*c)) =3 ;
	*(--(*c));

	// c is a pointer to a so a lives on when function returned
}


