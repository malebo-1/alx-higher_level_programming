#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>

int is_palindrome(listint_t **head);
void print_python_list_info(PyObject *p);
size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);

#endif /* LISTS_H */
