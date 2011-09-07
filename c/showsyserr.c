/*=====================includes================*/

#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
/*======================types====================*/

/*=====================globals===================*/

char *progname; // Program name for error messages.

/*====================prototypes=================*/
void usage(void);
int main(int argc, char** argv);
/*======================main()====================*/

int main(int argc, char  *argv[])
{

	int en;
		
	progname = argv[0];

	if(argc == 2) {

		en = atoi(argv[1]);
		printf("Error #%4d\t in %s\n" , en, strerror(en));
	
	} else if(argc ==1) {
	
		en =0;

		for(;en<sys_nerr;en++) {
			
			printf("Error: %4d\tMsg: %s\n", en, strerror(en));
		}

	} else {
	
		usage();
		exit(1);
	}
	
	return 0;
}

void usage(void)

{
	// Send formatted print to stream.
	fprintf(stderr, "Usage: %s [ error_number ]\n", progname);
}

