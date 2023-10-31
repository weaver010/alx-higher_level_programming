#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert
 *
 * @head: head
 *
 * @number:number
 *
 * Return:listint_t
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *o = *head, *s;

s = malloc(sizeof(listint_t));
if (s == NULL)
{
return (NULL);
}
s->n = number;
if (o == NULL || o->n >= number)
{
s->next = o;
*head = s;
return (s);
}

while (o && o->next && o->next->n < number)
{
o = o->next;
}
s->next = o->next;
o->next = s;
return (s);
}
