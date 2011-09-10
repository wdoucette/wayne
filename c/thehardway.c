#include <stdio.h>
#include <stdlib.h>

void callByValue(int []);
void callByReference(int *[]); 

void alloc(int );
void alloc2(int *);

int main() {



	//Normal way
	int *i = NULL; // realloc cant tolerate an uninitialize (random) value.
	
//	callByReference(&i);

	/*
		do stuff with i
	*/
//	free(i);

	
	// The hard way.

	int *p = NULL; // Declare a pointer so it is allocated an address block.
	printf("pointer address is: %p", &p);

	// Declare a second, pointer-to-a-pointer to pass as a reference to address block .
	int **pp; 
	pp  = &p; // assign  pp's base address.

	// int * pointer - I point to a vecotor pointer
	// int ** pointer - vector->vector[0 offset ]
	// int *** pointer - vector->vector->vector[data]


	printf("\naddress of pp %p\n", &pp);
	callByReference(pp); // Here we are passing a pointer by value, its base address will change but
				/// the data will still point to the same things. our pointer p!
				/// 

//	free(p);
//	p=NULL;


	
	int n = &p;

//	alloc(n); /// here we are passing p's address as an int value
	
//	printf("address of p: %p\n ",&p);
//	alloc2(p); /// here we are passing our pointer by value, the base address changes, but the data
			/// will still point to the same things...
			// when it's dereferenced, it's pointing to data. 

	free(p);

	return 0;
}

void callByReference(int **y ) //same as **y;
{

	printf("address of y %p\n", &y); // y has it's own new address because it was passed a value.
	printf("address of y[0] %p\n", &y[0]); // this value is p's address location
	
	// now derefrencing y, we set a new base to y[0] ~= p	
//	*y=malloc(4000 * sizeof(int) );
	
	y[0]=realloc(y[0], 4000 * sizeof(int) );

}

void alloc(int y ) // here we are passing the memory location as an int by value 
{



	printf("the address passed in is: %p\n", y);

	int *ptr;
	

	printf("******  the address of ptr: %p**********\n", &ptr);
	
	ptr = y; // set prt's address to what we passed in
	
	printf("******  the new address of ptr: %p**********\n", &ptr);
	printf("pptr[3] = %d\n", ptr[3]);	
	// now derefrencing y, we set a new base to y[0] ~= p	
	//y[0]=malloc(4000 * sizeof(int) );

	// ERROR -- This address is on someone else's stack!	
	//ptr=realloc(ptr, 4000 * sizeof(int) );

}


/// Vector table analogy.

void alloc2(int * x) {  /// Makes it's own copy of the address 'lookup table'
printf("address of x %p\n", &x);
	x = realloc(x, 4000 * sizeof (int) );



}


