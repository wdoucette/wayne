// Function pointer demo.
// September 6th, 2011 -Wayne Doucette

/*=========== INCLUDES =============*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

/*========== PROTOTYPES ===========*/

int main(int, char**);
double doPow(double, double);
double doMod(double, double);
void _dtoa(char*, double);

// Function pointer definitions.
double (*GetPtr(const char ))(double, double);
double (*ptf)(double, double);
double fptr(double, double, double (*)(double,double) );

/*============= MAIN ===============*/

int main(int argc, char * argv[])
{
	// TODO Process argumemt, define usage.

	double x = atoi(argv[1]);
	double y = atoi(argv[3]);	
 	double d;
	char str[255];

	printf("Processing %d %s %d\n" , (int)x ,argv[2], (int)y);
	
	// Function pointer example 1.
	//d = fptr(1.0,2.0, &doMod );
	
	// Function pointer example 2.
	ptf=GetPtr(argv[2][0]);
	d=ptf(x , y);

	_dtoa(str, d);	
	printf("Solution is: %s\n", str );

	return 0;

}

void  _dtoa(char *str, double n){

	// Double to string.
	sprintf(str , "%.2f", (double)n);	


}

double fptr(double x, double y, double(*dellegate)(double, double)){

	return dellegate(x,y);
}

double (*GetPtr(const char opCode ))(double, double){

	if(opCode =='^')
		return &doPow;
	return &doPow;

}

double doPow(double x, double y){
	
	printf("Calling pow\n");
	return pow(x, y);//pow((float)x,(float)y);

}

double doMod(double x, double y){

	return 3.141;//mod(x,y);

}
