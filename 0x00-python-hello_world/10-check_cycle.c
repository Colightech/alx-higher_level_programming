#include "lists.h"

/**
 * check_cycle - checks if a linked list is moving in cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *walk = list;
	listint_t *run = list;

	if (!list)
		return (0);

	while (walk && run && run->next)
	{
		walk = walk->next;
		run = run->next->next;
		if (walk == run)
			return (1);
	}

	return (0);
}
