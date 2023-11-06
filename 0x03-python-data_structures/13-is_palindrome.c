#include "lists.h"
/**
 * chpalindrome - check
 * @h: h
 * @a: a
 * Return: 1
 */
int chpalindrome(listint_t **h, listint_t *a)
{
int r;
if (a != NULL)
{
r = chpalindrome(h, a->next);
if (r != 0)
{
r = (a->n == (*h)->n);
*h  = (*h)->next;
return (r);
}
return (0);
}
return (1);
}

/**
 * is_palindrome - checks
 * @head: head
 * Return: 1
 */
int is_palindrome(listint_t **head)
{
if (head == NULL)
{
return (0);
}
return (chpalindrome(head, *head));
}
