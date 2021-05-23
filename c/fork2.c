#include <stdio.h>
#include <unistd.h>

int main( void ) {
	int pid = fork();

	if ( pid == 0 ) {
		printf( "This is child process\n" );
		printf( "This is the child process \"calling getpid %d\"\n", getpid() );
		printf( "This is the child process \"calling getppid %d\"\n", getppid() );
                sleep(10);
		printf( "This is the child process \"calling getppid %d\"\n", getppid() );
	} else {
		printf( "This is the parent process \"pid of child is\" %d\n", pid );
		printf( "This is the parent process \"calling getpid %d\"\n", getpid() );
		printf( "This is the parent process \"calling getppid %d\"\n", getppid() );
                sleep(2);
	}

	return 0;
}
