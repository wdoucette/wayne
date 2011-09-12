#include <stdio.h>
#include <stdlib.h>


void callByValue(int []);
void callByReference(int *[]); 

void alloc(int );
void alloc2(int *);

int main(int argc, char *argv[])
{

/*	Understanding Pointers and Memory Allocation in C	
	 
	Conventions:

	All examples use functioning code in context. This means you can copy-paste, compile and execute all 
	examples. The top of each example gives an overview of the purpose and program flow, with expected 
	output.

	Code is what you see is what you get - printf() is used to format all output examples, exactly
	the way real code works.


	the statement: 
		
		printf(" --> the memory address of int a is: %p\n", &a);    

	will output:

		--> the memory address of int a is: 0xEA12C4
	

	Notes:

		Special formatting characters recognized by printf() are:
		%p - a hex number
		%i - an integer
		%d - a double
		%s - a string 
		%c - a char
		\n - new line

##################################################################################################################



	One factor causing confusion with pointers is the language syntax itself.
	The '*' character, for example, is used for two related, but entirely different operations
	when working with pointers. Lets clear up the confusion by illistrating a few examples while 
	compare syntax styles...	

*/


// VARIABLES:

 	int i; 
	printf(" --> the value of i is: %d\n", i );


/*
 *	--> the value of i is: -1000010	???
 *
 *
 * 	- Declaring a variable allocates memory space to store it. However, until a variable 
 * 	has been initialized, it will contain unpritictable values ...
 */
<<<<<<< HEAD
	
=======
	
	

	printf(" --> the memory address of i = %p\n", &i ); 	 

/*	
 *	--> the memory address of i = 0xAAAAAA	
 *
 *
 * 	... The '&' charactor tells the compiler that we want a variable's address, NOT its value ...
*/

 	i = 123;	
				
	printf(" --> the value of i is: %d\n", i );

/*
 * 	--> the value of i is: 123
 * 	
 * 	
 * 	- Interger i has now been initialized: The memory address 0xAAAAAA now contains the value 123 ...
 *
 * 	... While not considered pointers, even primitive variables can be thought of as 'pointing to
 * 	a memory address in which their value is stored ...
*/



/* POINTERS:
 *
 * 
 * 	C is inherently a pass-by value language - This means that a function makes it's
 * 	own locally copy of each parameter it receives.	Similarly, anyhing returned from a function 
 * 	is copied locally back inside the calling function. Pointers are implemented to pass memory 
 * 	addresses which reference some other external value without having to duplicate the entire value.
 *
 * 	Passing a pointer is in fact, passing a reference. Thus the term 'pass by reference'. 
 *
*/

	int * pt; 
 	
	printf(" --> the memory address of pt = %p\n", &pt );

/*	
 *	--> the memory address of pt = 0xFFFF00
 *
 *	... The int * operator tells the compiler that we want to declare an integer pointer type ...
*/	
	
 	printf(" --> the value of pt = %p\n", pt ); 	

/*	
 *	--> the value of of pt = 0x100101	???
 *
 *
 *
 * 	- Pointers are allocated a memory address just like other types and their values are also
 *  	  inditerminate until properly initialize -in other words, they point to random memory locations. 
*/

 	pt = &i; 	
/* 
 * 	
 * 	- int pointer pt has been assigned i's memory address.
 *
 *
 *  	... I like to think of this as setting the pointer's 'base reference' address ...
 *
*/ 

 	*pt = 456;  

	printf(" --> the value i contains = %d\n", i ); 	 
/*
 *	
 *	--> the value i contains = 456
 *
 *
 * 	Here we see the '*' character again, but this time it means 'return the value ptr points to.'
 *
 * 	We can achieve the same result using different  sytax:
*/

 	pt[0] = 789; 	
	
	printf(" --> the value of i[0] is: %d\n", i[0] ); 	 
 
/*
 * 	--> the value of i[0] is: 456
*/
	
	printf(" --> the value of i[1] is: %d\n", i[1] ); 	 
/*
 * 
 * 	--> the value of i[0] is: 100010 	???
 *
 *
 * 	As with other types, pointers to uninitialize locations also return indeterminate  values.
 * 	-I prefer this indexed array style syntax becase it is clear to me that ptr[0] will evaluate to 
 * 	get back the first 'element' of ptr.
 *
*
* / 	
>>>>>>> 0493bb8378ad63ae747d0bd29bd67c88cda6386c
	

	printf(" --> the memory address of i = %p\n", &i ); 	 

/*	
 *	--> the memory address of i = 0xAAAAAA	
 *
 *
 * 	... The '&' charactor tells the compiler that we want a variable's address, NOT its value ...
*/

 	i = 123;	
				
	printf(" --> the value of i is: %d\n", i );

/*
 * 	--> the value of i is: 123
 * 	
 * 	
 * 	- Interger i has now been initialized: The memory address 0xAAAAAA now contains the value 123 ...
 *
 * 	... While not considered pointers, even primitive variables can be thought of as 'pointing to
 * 	a memory address in which their value is stored ...
*/



/* POINTERS:
 *
 * 
 * 	C is inherently a pass-by value language - This means that a function makes it's
 * 	own locally copy of each parameter it receives.	Similarly, anyhing returned from a function 
 * 	is copied locally back inside the calling function. Pointers are implemented to pass memory 
 * 	addresses which reference some other external value without having to duplicate the entire value.
 *
 * 	Passing a pointer is in fact, passing a reference. Thus the term 'pass by reference'. 
 *
*/

	int * pt; 
 	
/*
 *	... The int * operator tells the compiler that we want to declare an integer pointer type ...
*
*/  	
`
	printf(" --> the memory address of pt = %p\n", &pt );

/*	
 *	--> the memory address of pt = 0xFFFF00
*/ 
	
	printf(" --> the value of pt = %p\n", pt ); 	

/*	
 *	--> the value of of pt = 0x100101	???
 *
 *
 * 	- Pointers are allocated a memory address just like other types and their values are also
 *  	  inditerminate until properly initialize -in other words, they point to random memory locations. 
*/


	pt = &i; 	

 	printf(" --> the memory address of pt = %p\n", &pt );

/*	
 *	--> the memory address of pt = 0xFFFF00
 *
 *
 *	- Pointer pt has been assigned int i's memory address -  0xFFFF00 now contains a's address.
 *
 *
 *  	... I like to think of this as setting the pointer's 'base reference' address ...
 *
*/ 

 	*pt = 456;  

	printf(" --> i's value is now: %d\n", i ); 	 

/*
 *	--> the value i is now: 456
 *
 *
 * 	Here we see the '*' character again, but this time it means 'return the value ptr points to.' 
 *
 * 	We can achieve the same result using different  sytax:
*/ 	
 	

	pt[0] = 789; 	
	
	printf(" --> the value of i[0] is: %d\n", i[0] ); 	 
 
/*
 * 	--> the value of i[0] is: 456
*/
	
	printf(" --> the value of i[1] is: %d\n", i[1] ); 	 
/*
 * 
 * 	--> the value of i[0] is: 100010 	???
 *
 *
 * 	- As with other types, pointers to uninitialize locations also return indeterminate values.
 * 	I prefer this indexed array style syntax becase it is clear to me that ptr[0] will evaluate to 
 * 	get back the first 'element' of ptr.
 *
*/ 	
	

// 	Arrays and pointer arithmatic.


 	int i[4]; 		// Declare an array of integers and initialize values:

 	i[0] =10;	
 	i[1] =20;
 	i[2] =30;
 	i[3] =40;
	

 	int * pt = &i; 	// Set ptr base reference address.
	
 	pritnf(" --> pt[0] = %d\n", pt[0]); 		

	// --> pt[0] = 10

 	printf(" --> ++pt[0] = %d\n", ++pt[0]); 

	// --> ++pt[0] = 20	// '++' pre-increments pt's base reference address such that 
				// pt's first element now points to a[1].
 
	printf(" --> --pt[0] = %d\n", --pt[0]); 

 	// --> ++pt[0] = 10 	// '--' pre-decrements out base back to a[0].

 	printf(" --> pt[3] = %d\n", pt[3]) ; 
 	// --> pt[3] = 40	// ...we're back to normal!



// 	Memory Allocation 

	#include <stdio.h>


	void fn(void);
	
	int main() {
	
		int i =1;
		fn(i);
		printf(" --> i = %p\n", i);

		// --> i = 1;

		return 0;				
	}

	fn(int i) { 

		i=2;
	}

// 	Why are the values of int i different in each function? This further example makes the situation clear:

	
	#include <stdio.h>

	void fn(int);

	int main() {
		
		int i =1;
		
		printf(" --> &i = %p\n". &i );		// Print int i's memory address.

		// --> 0xABCD00

		fn(i);
		printf(" --> i = %d\n", i);

		// --> i = 1;		// the value of int i remains 1.

		return 0;		
	}

	fn(int i) 

		i=2;
		printf(" -->&i = %p\n", &i;)		// Print int i's memory address.

		//  --> &i = 0xABCD04
	}

//	The values of int i in each function are seperate copies because their memory addresses are different. When
//	main() calls fn(), the value of int i is copied into fn()'s private memory space. 


	
//	Pointers are what make 'passing by reference' possible. In this case, the values copied locally
//	inside the called function are the memory addresses that 'point to' the referenced objects. 
	 

	#include <stdio.h>

	void fn(int *);


	int main() {


		int i = 1;
		int pt1 = &i;
	
		printf(" --> %p\n", &pt1);

		// --> 0xFFFF00  			// pt1's address.

		printf(" --> %p", pt1);

		//  --> 0xABCD00 - pt1's value = i's address.

		fn(pt1);

		// --> i is now 10 
	}	


	void fn(int * pt2) {


		printf("-->  pt2's address = %p\n". &pt2);

// 		-->  pt2's address = 0xFFFF01 

//		This is new. pt2 has been created to hold a copy 
//		of the passed-in value.


		printf("--> pt2's value = %p\n", pt2);

		// --> pt2's value = 0xABCD00		

//		pt2's value is set to int i's address. We can now reference int i as follows: 

		
		pt2[0]=10; 	// Assign 10 to offset 0 - int i's address  (Equivalent to *i=10)
			
	}


// 	Under the Hood
		
// 	Conceptually, pointers function as a vector table to cross-reference memory locations:
	

//	Pointers: A Vector Table Analogy

//	     Entry # (Ponters Address)     Reference (Value's Address) 
//	#################################################################
//					#				#
//		0xFFFF01		-->	0xAAAA00		#
///	#################################################################
//					#				#
//		0xFFFF02		-->	0xAAAA04		#
//	________________________________#_______________________________#


	
	// puts(ptr[1]); // prints the value of the next pointed to memory location. 
	// The contents of which are undefined so it will return us whatever random value happens to be there; 




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


##############################################


C Programming:

make filename -(where source file is named filename.c)
CC=/path/to/gcc/compiler/dejure
CFLAGS = -Wall (all warnings) -g (debug) -O3 (full optimize) -Os (small) --march=mycpuonly --mtune=tune2mycpu

Declare a pointer of type char:
char *ptr;
char buffer[255];

Set pointer’s address:
prt = &buffer[0];
buffer[1[=’a’;

// inc pointer
ptr++;

// dereference pointer
putc(*ptr, stdout);

Printing

printf(“Hello, %s\n”, “World.”); // Formatted printing to console.
fprintf(stdout, “Hello, %s\n”, “World.”); // Formatted printing to stream.

putc(mychar, stream); Print char to stream.
puts(mychar*); // Print char* to console. 

There are essentially three uses of the preprocessor--directives, constants, and macros. Directives are commands that tell the preprocessor to skip part of a file, include another file, or define a constant or macro. Directives always begin with a sharp sign (#) and for readability should be placed flush to the left of the page. All other uses of the preprocessor involve processing #define'd constants or macros. Typically, constants and macros are written in ALL CAPS to indicate they are special (as we will see).

Header Files

#include directive tells the preprocessor to grab the text of the file and place it directly into the current file

#define [identifier_name] [value] // preprocessor replaces text identifier_name with value
#define PI_PLUS_ONE (3.14 +1);


Pointers

void alloc(int **); // Declare alloc. Takes address of a pointer
void main(int argc, char *argv[]) {

int *a; // pointer to integer
*a = malloc( 1 * sizeof (*a) ); // Size to 1 integer.
*a = 1;
alloc(&a); // call alloc with a’s address
printf(“a[1] now = %i”, a[1]); 
return 0;
}

void alloc(int ** b){

*b=malloc(2 * sizeof (*b) );
 // *(*b) =1; // De-reference and set value of first location.
*(*b)[1]=2; // Another way to de-reference and set value of 2nd location.

}

Conditional Compilation
They include #if, #elif, #else, #ifdef, and #ifndef. An #if or #if/#elif/#else block or a #ifdef or #ifndef block must be terminated with a closing #endif. 


Avoid including headers multiple times:

#ifndef _FILE_NAME_H_
#define _FILE_NAME_H_

/* code */

#endif // #ifndef _FILE_NAME_H_


Macros

#define MULTI(x,y) x *y

int z = MULTI(3+2, 4+2) ….> 3+2 * 4 +2 =13
int z = MULTI((3+2), (4+2)) ….> (3+2) * (4 +2) =30

Macro tokens to string.
#define PRINT_TOKEN(token) printf(#token " = %s\n", token);
char *token = “mytoken”;
PRINT_TOKEN(token); // token = mytoken

Malloc

double *p;
p = malloc ( n * sizeof *p );


C Pointers and Memory Allocation


The Problem - Passing the pointer's value rather than its address:

int main(int argc, char *argv[]) 
{
	
	int *a; 	// &a = 0xAAAAAA 	- int pointer a's address 
	int b = 10;	// &b = 0xBBBBBB	- int b's address holds the value 10

	
			// a =  0x102938 	- a points to a random address because it's unassigned
			// *a = 10034093	- a points to a random value held a 0x102938

	a=&b					- assign int b's address to int pointer a

			// &a = 0xAAAAAA	- a is still at the same address
			//  a = 0xBBBBBB	- a now points to b's memory address
			// *a = 10		- a now points to the value 10 held at 0xBBBBBB


			// int * a and int * c are the same type...
	f(a);		// This means we are passing int pointer a by value to f(int *) ....

	return 0;

}

	
f(int *c){

			// &c = 0xCCCCCC	- int pointer c's address
			// c  = 0xBBBBBB	- c now points to b's memory address
			// *c = 10		- c now points to the value 10 held at 0xBBBBBB

			// int pointer a's value was bassed to c 
			// both int pointers a and c point to b now

	*c=20; 		// b now = 20.

	c = realloc(c, 1 * sizeof (c) ) // INVALID realloc because block was assigned outside this scope

	c = malloc(1 * sizeof (c) ); // &c is now a new address block eg, 0xcccccc of which a and b are unaware...
	
	// These above methods do not allow the calling function to access new memory

	// we could return c by value so that a would point to c's new block
	// OR
	// we could pass a's address by reference, f(&a) --> f(int **c) so 
	// c's address = 0xAAAAAA
}


Pass by reference


Returning by reference 




Return by value




