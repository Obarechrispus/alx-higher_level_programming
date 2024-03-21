#include "lists.h"
/**
 *print_dlistint - a function that prints the number of elements in a linked list
 *@h: number of elements
 *
 *
 *Returnn: node
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t node = 0;
	while (h != NULL)
	{
	printf("%d\n", h->n);
	h = h->next;
	node++;
	}
	return node;
}
