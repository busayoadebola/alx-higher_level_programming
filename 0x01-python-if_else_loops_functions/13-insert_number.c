#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 ** insert_node - Inserts a number into a sorted singly-linked list.
 ** @head: A pointer the head of the linked list.
 ** @number: The number to insert.
 **
 ** Return: If the function fails - NULL.
 ** Otherwise - a pointer to the new node.
 **/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current;

	new_node = (listint_t *)malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	current = *head;
	while (current->next != NULL && current->next->n <= number)
	{
		current = current->next;
	}
	new_node->next = current->next;
	current->next = new_node;
	return (new_node);
}
