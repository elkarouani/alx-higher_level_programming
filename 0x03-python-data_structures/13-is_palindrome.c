#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to the first node in the list
 *
 * Return: pointer to the first node of tge new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the first node
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_track = *head;
	listint_t *fast_track = *head;
	listint_t *temp_node = *head;
	listint_t *dupli_node = NULL;

	if (!*head || !(*head)->next)
		return (1);

	while (true)
	{
		fast_track = fast_track->next->next;
		if (!fast_track)
		{
			dupli_node = slow_track->next;
			break;
		}
		if (!fast_track->next)
		{
			dupli_node = slow_track->next->next;
			break;
		}
		slow_track = slow_track->next;
	}

	reverse_listint(&dupli_node);

	while (dupli_node && temp_node)
	{
		if (temp_node->n == dupli_node->n)
		{
			dupli_node = dupli_node->next;
			temp_node = temp_node->next;
		}
		else
			return (0);
	}

	if (!dupli_node)
		return (1);

	return (0);
}
