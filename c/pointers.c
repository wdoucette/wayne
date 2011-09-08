
#include <stdio.h>
#include <stdlib.h>

void f(int *);

int main(int argc, char *argv[])
{

	int *a;
	int b=20;

puts("\n");	

	printf("int * a is an undefined pointer to an integer\n");
	printf("a is located at &a %p\n", &a);
	printf("a points to address  %p \n", a);
	printf("*a points to an address holding the value:  %i\n", *a);


puts("\n");	


	printf("int b is located at %p\n", &b);
	printf("b holds the value %i\n", b);
	
puts("\n");	
	printf("pointing a to b's address: a=&b\n");
	a=&b;
	printf("a now points to %p\n", a);
	printf("&a is still located at &a%p\n", &a);
	printf("*a is now pointing to an address holding the value: %i\n", *a);


puts("\n");	
	f(a);


puts("\n");	
	printf("Returned from f()\n");
	printf("a is %i\n", *a);
	printf("b is %i\n", b);

	return 0;

}

void f(int *c)
{


puts("\n");
	printf("Now calling f(int *c) with f(a)");
	printf("int * c is a pointer located at address: &c %p\n", &c);
	printf("c points to address: %p (b's address)\n", c);
	printf("c is now pointing to an address holding the value: %i\n", *c);
puts("\n");
	printf("-c has been passed the value of a (b's address)\n");



puts("\n");

	printf("assigning *c=30\n");
	*c=30;
	
puts("\n");

	printf("c still points to b's address: %p\n", c);
	printf("*c is: %i\n", *c);
	
	puts("c= relloc ....\n");
	c = malloc(2 * sizeof (int) );

//	exit(0);
	printf("c is: %i\n", *c);
	//*c=40;
	printf("c is: %i\n", *c);
	printf("c points address: %p\n", c);


}


