#include<stdlib.h>
#include<stdio.h>


int* f1() {
 int *b = malloc(sizeof(int));
 *b = 5;
 
return b;
}

int main() {
 int *a = NULL;
 a = f1(); // assign the return value of f1 to a.
 printf("%d\n", *a); // prints 5...not its *a not just a.

free(a);
 return 0;
}
