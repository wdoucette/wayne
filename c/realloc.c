/*============ includes ============*/
#include <stdio.h>
#include <stdlib.h>


/*============= types ==============*/
struct BUFFER{

	int size;
	char *data;
	int bs;

}; 
/*============= globals ============*/


/*=========== prototypes ===========*/

void fAllocate(int ** ptr, int size); // Declare alloc. Takes address of a pointer
void bufferAllocate(struct BUFFER *);


/*============= main ================*/
int main(int argc, char *argv[]) 
{

	// Allocate  buffer to bs bytes then increase by bs bytes.
	// Allocate a to 1 int then increase to 2 int.

	struct BUFFER buffer = {0,NULL,256};

	bufferAllocate(  &buffer);
	bufferAllocate(  &buffer);

	int *a = NULL; // Set ptr to NULL so realloc initially acts like malloc on empty block. 
	
	fAllocate(&a, 1); 
	a[0]=1;

	fAllocate(&a, 2);
	a[1]=2;	

	printf("a[0] = %i\n", a[0]);
	printf("a[1] = %i\n", a[1]);

	free(a);
	free(buffer.data);
	return 0;
}

void bufferAllocate(struct BUFFER *b){
	
	// Increase BUFFER.data allocation by bs bytes. 
	(*b).data = realloc((*b).data , (*b).bs * sizeof ((*b).data));
	(*b).size += (*b).bs ;

	printf("Buffer size is now %i\n", (*b).size);
}

void fAllocate(int ** o, int size){
	
	// Resize o.

	*o = realloc(*o,  size * sizeof *o );
	// *(*o) =1; // De-reference and set value of first location.
	//(*o)[1]=2; // Another way to de-reference and set value of 2nd location.
	//(*o)[0]=97;

}
