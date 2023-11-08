#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
void print_python_bytes(PyObject *p)
{
long int l;
int i;
char *s= NULL;
printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}
PyBytes_AsStringAndSize(p, &s, &l);
printf("  size: %li\n", l);
printf("  trying string: %s\n", s);
if (l < 10)
{	
printf("  first %li bytes:", l + 1);
}
else
{
printf("  first 10 bytes:");
}
for (i = 0; i <= l && i < 10; i++)
{
printf(" %02hhx", s[i]);
}
printf("\n");
}
void print_python_list(PyObject *p)
{
long int l = PyList_Size(p);
int i;
PyListObject *s = (PyListObject *)p;
const char *t;
printf("[*] Python list info\n");
printf("[*] Size of the Python List = %li\n", l);
printf("[*] Allocated = %li\n", s->allocated);
for (i = 0; i < l; i++)
{
t = (s->ob_item[i])->ob_type->tp_name;
printf("Element %i: %s\n", i, t);
if (!strcmp(t, "bytes"))
{
print_python_bytes(s->ob_item[i]);
}
}
}
