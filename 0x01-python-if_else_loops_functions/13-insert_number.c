#include "lists.h"

/**
 * insert_node - inserts a node at the end of a linked list
 * @head: start of linked list
 * @number: value of node to be added
 *
 * Return: address of new node, or NULL if failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *ptr = *head;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (*head);
	}

	while (ptr->next != NULL)
		ptr = ptr->next;

	ptr->next = new_node;

	return (new_node);
}
