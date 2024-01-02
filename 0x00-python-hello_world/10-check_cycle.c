#include "lists.h"

/**
 * check_cycle - Does a linked list contain a cycle?
 * @list: The linked lists to be checked
 *
 * Return: 1 when cycleis present, 0 if thre is no cycle
 */
int check_cycle(listint_t *list)
{
listint_t *slow = list;
listint_t *fast = list;

if (!list)
return (0);
while (slow && fast && fast->next)
{
slow = slow->next;
fast = fast->next->next;
if (slow == fast)
return (1);
}

return (0);
}
