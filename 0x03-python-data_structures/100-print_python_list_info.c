#include<stdio.h>
#include<Python.h>
/**
 * print_python_list_info - print
 * @p:p
 * Return:void
 */
void print_python_list_info(PyObject *p)
{
int d, s, i;
PyObject *o;
d = PyList_Size(p);
s = ((PyListObject *)p)->allocated;
printf("[*] Size of the Python List = %d\n", d);
printf("[*] Allocated = %d\n", s);
for (i = 0; i < d; i++)
{
o = PyList_GetItem(p, i);
printf("Element %d: %s\n", i, Py_TYPE(o)->tp_name);
}
}
