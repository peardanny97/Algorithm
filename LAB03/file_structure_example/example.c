#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char **argv) { 
    FILE *fin = fopen(argv[1], "r");
    FILE *fout = fopen(argv[2], "w");
    int a, b; 
    fscanf(fin, "%d", &a);
    fscanf(fin, "%d", &b);
    int result; 
    if (strcmp(argv[3], "add") == 0) {
        result = a + b;
    }
    else if (strcmp(argv[3], "sub") == 0) {
        result = a - b;
    }
    fprintf(fout, "%d\n", result);
    return 0; 
}