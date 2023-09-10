#include "lists.h"

/**
 * is_palindrome - checks if a list is palindrome
 * @head: list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
    listint_t *current = *head;
    static listint_t *temp;

    if (current == NULL)
        return (1);
    if (temp == NULL)
        temp = current;
    if (is_palindrome(&current->next) && temp->n == current->n)
    {
        temp = temp->next;
        current = current->next;
        return (1);
    }
    temp = current;
    return (0);   
}