#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
int infinite_while(void);
/**
 * main -entry point
 * Return: 0
 */
int main(void)
{
	int i;
	pid_t child;

	for (i = 0; i < 5; i++)
	{
		child = fork();
		if (child > 0)
		{
			sleep(1);
			printf("Zombie process created, PID: %d\n", child);
		}
		else
		{
			exit(0);
		}
	}
	infinite_while();
	sleep(10);
	return (0);
}
/**
 * infinite_while - runs an infinite while loop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

