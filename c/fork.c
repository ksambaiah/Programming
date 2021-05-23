#include <stdio.h>
#include <unistd.h>

int main( void ) {
	int pid = fork();

	if ( pid == 0 ) {
		printf( "This is child process\n" );
		printf( "This is the child process \"calling getpid %d\"\n", getpid() );
                sleep(1200);
	} else {
		printf( "This is the parent process \"pid of child is\" %d\n", pid );
		printf( "This is the parent process \"calling getpid %d\"\n", getpid() );
	}

	return 0;
}
