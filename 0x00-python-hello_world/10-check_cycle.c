#include "lists.h"

/**
 * check_cycle - checks
 * Return: 1 
 */
int check_cycle(listint_t *list)
{
listint_t *i = list;
listint_t *o = list;
if (!list)
{
return (0);
}
while (o && o->next)
{
i = i->next;
o = o->next->next;
if (i == o)
{
return (1);
}
}
return (0);
}
