#include<stdlib.h>
#include<stdio.h>
#include<string.h>
int compare( const void *arg1, const void *arg2 ) { /* Compare all of both strings: */
	return strcmp( * ( char** ) arg1, * ( char** ) arg2 );
}
int main( int argc, char **argv ) {
	int i; /* Eliminate argv[0] from sort: */
	argv++; argc--; /* Sort remaining args using Quicksort algorithm: */
	qsort( (void *)argv, (size_t)argc, sizeof( char * ), compare ); /* Output sorted list: */
	for( i = 0; i < argc; ++i )
	  printf( " %s", argv[i] );
	printf( "\n" );
}
