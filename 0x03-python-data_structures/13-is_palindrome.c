/*
 * File: 13-is_palindrome.c
 * Auth: Okere Uchechukwu
 */

#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *current = *head, *next_node, *prev = NULL;

	while (current)
	{
		next_node = current->next;
		current->next = prev;
		prev = current;
		current = next_node;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: 0 if the linked list is not a palindrome, 1 if it is.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *reversed, *middle;
	size_t count = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmp = *head;
	while (tmp)
	{
		count++;
		tmp = tmp->next;
	}

	tmp = *head;
	for (i = 0; i < (count / 2) - 1; i++)
		tmp = tmp->next;

	if ((count % 2) == 0 && tmp->n != tmp->next->n)
		return (0);

	tmp = tmp->next->next;
	reversed = reverse_listint(&tmp);
	middle = reversed;

	tmp = *head;
	while (reversed)
	{
		if (tmp->n != reversed->n)
			return (0);
		tmp = tmp->next;
		reversed = reversed->next;
	}
	reverse_listint(&middle);

	return (1);
}
