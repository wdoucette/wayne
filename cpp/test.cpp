//#include <stdio.h>
#include <iostream>

// Include header.
//#include "foo.h"

// Or, declare inline.
void foo();


using namespace std;


int main(int argc, char** argv) {

    cout << "\nTest OK\n";
    foo();

    return 0;
}

void foo() {

    cout << "\nFoo says hi\n";

}



