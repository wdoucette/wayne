#include <stdio.h>
#include <stdlib.h>

// Pointer call by value example.
// malloc issues

void f(int *);

int main(int argc, char *argv[]) 

{
	
	int *a; 	// &a = 0xAAAAAA 	- int pointer a's address 
	int b = 10;	// &b = 0xBBBBBB	- int b's address holds the value 10

	
			// a =  0x102938 	- a points to a random address because it's unassigned
			// *a = 10034093	- a points to a random value held a 0x102938

	a=&b;		//			- assign int b's address to int pointer a

			// &a = 0xAAAAAA	- a is still at the same address
			//  a = 0xBBBBBB	- a now points to b's memory address
			// *a = 10		- a now points to the value 10 held at 0xBBBBBB


			// int * a and int * c are the same type...
	f(a);		// This means we are passing int pointer a by value to f(int *) ....
	
	
	// Error - invalid delete 
	// free(a);

//	while( getchar() !='q') {


//	printf("Press q quit");
		
//		f(a);
//	}
	
	return 0;


}

	
void f(int *c){

	// int pointer c has been passed the value of int pointer a
	// both and and c now point to b:
	
			// &c = 0xCCCCCC	- int pointer c's address
			// c  = 0xBBBBBB	- c now points to b's memory address
			// *c = 10		- c now points to the value 10 held at 0xBBBBBB

			// int pointer a's value was bassed to c 
			// both int pointers a and c point to b now

	*c=20; 		// c=20 so b now =20 because c is pointing to 0xBBBBBB

	// c = realloc(c, 1 * sizeof (c) ); // INVALID realloc because block was assigned outside this scope

	c = malloc(1000 * sizeof (c) ); // &c is now a new address block eg, 0xcccccc of which a and b are unaware...
	
	// These above methods do not allow the calling function to access new memory

	// we could return c by value so that a would point to c's new block
	// OR
	// we could pass a's address by reference, f(&a) --> f(int **c) so 
	// c's address = 0xAAAAAA

	// If we don't free c now, we will lose 1000 integers, 4000 bytes, every time this function is called
	// because we will have no reference to it left
	
// IMPORTANT: free(c);


//char * msg ="\n\
	// example output from valgrind after 1 iteration:\n\
\
	//==2382== HEAP SUMMARY:\n\
	//==2382==     in use at exit: 4,000 bytes in 1 blocks\n\
	//==2382==   total heap usage: 1 allocs, 0 frees, 4000 bytes allocated\n\
	//==2382==\n\
	//==2382== LEAK SUMMARY:\n\
	//==2382==    definitely lost: 4,000 bytes in 1 blocks\n\
	//==2382==    indirectly lost: 0 bytes in 0 blocks\n\
	//==2382==      possibly lost: 0 bytes in 0 blocks\n\
	//==2382==    still reachable: 0 bytes in 0 blocks\n\
	//==2382==         suppressed: 0 bytes in 0 blocks\n";

	//puts(msg);
}


