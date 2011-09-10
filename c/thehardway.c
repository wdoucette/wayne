#include <stdio.h>
#include <stdlib.h>

void callByValue(int []);
void callByReference(int *[]); 

void alloc(int );
void alloc2(int *);

int main(int argc, char *argv[])
{

//	Understanding Pointers and Memory Allocation in C	
	 
//	Conventions:

//	All examples use functioning code in context. This means you can copy-past, compile and execute.
//	is. The top of each example gives a textual overview of the purpose and program flow, with expected 
//	output  


//	A factor causing confusion with pointers is the language syntax itself.
//	The '*' character, for example, is used for two related, but entirely different operations
//	when working with pointers. Lets clear up the confusion by illistrating a few examples while 
//	compare syntax styles.	




 	int i; 

// 	Declaring i as an integer will allocate a memory block of 4 bytes. However, since 
//	int i is uninitialized, the 4 bytes it occupies will contain unpredictable values.
	

	// Print int i's address - &i

	printf(" --> &i = %p\n", &i); 	 

	// --> &i = 0xAAAAAA 			// i's memory address

 	i = 123					// Assign memory address location 0xAAAAAA = 123.


//	-While not considered pointers, even primitive variables can be thought of as 'pointing to'
//	 a memory address in which their value is stored.



	// Pointers

	int * pt 			// Define pt as type int * (a pointer to an integer)
 	printf(" --> &pt = %p\n", &pt) 	// Print pt's memory address:

	// --> &pt = 0xFFFF00.


 	pt = &i 	
	
// 	pt's address (0xFFFF00) now contains the value 0xAAAAAA - i's address. I like to think 
//	of this as setting a pointer's 'base reference' address.


 	*pt = 456 	// i now = 456! 

//	Here we see the '*' character again, but this time it means 'return the value ptr points to.'
// 	We can achieve the same result using different  sytax:


 	pt[0] = 789; 	// i now = 789
 	pt[1] = ??? 	// points to an unallocated location!


// 	-I prefer this indexed array style syntax becase it is clear to me that ptr[0] will evaluate to 
//	get back the first 'element' of ptr.
	


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

//	C is inherently a pass-by value language. This means that a called function makes it's
//	own locally copy of each parameter it receives.	Similarly, anyhing returned from a function
//	is copied locally back inside the calling function.

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


