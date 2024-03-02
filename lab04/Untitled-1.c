#include <stdio.h>

int main(int *n, char *str)
{
	if (n == 2)
		printf("Hello World!\n");
	else
	{
		printf("print anything.\n");
		exit(1);
	}
	return 0;
}