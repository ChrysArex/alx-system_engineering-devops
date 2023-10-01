#include <stdio.h>
#include <stddef.h>
#include <unistd.h>
/**
 * infinite_while - sleep indefinitly
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

/**
 * main - creates 5 zombie processes.
 * Return: 0
 */
int main(void)
{
	pid_t cpid, ppid = getpid();
	int i;

	for (i = 0; i < 5; i++)
	{
		cpid = fork();
		if (cpid == 0)
			return (0);
		printf("Zombie process created, PID: %d\n", cpid);
	}
	infinite_while();
	return (0);
}
