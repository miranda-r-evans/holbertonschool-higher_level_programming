#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: the linked list
 *
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *start;
	listint_t *end;
	listint_t *tmp;

	if (head == NULL)
		return (0);

	if (*head == NULL)
		return (1);

	start = *head;
	end = *head;

	while (end->next != NULL)
		end = end->next;

	while (end != start)
	{
		if (end->n != start->n)
			return (0);

		start = start->next;
		tmp = start;

		if (start == end)
			return (1);

		while (tmp->next != end)
			tmp = tmp->next;

		end = tmp;
	}

	return (1);
}
