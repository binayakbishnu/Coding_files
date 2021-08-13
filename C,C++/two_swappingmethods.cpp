#include <stdio.h>


void swap1(int &x, int &y)
{
    int t = x;
    x = y;
    y = t;
}

void swap2(int *x, int *y)
{
    int t = *x;
    *x = *y;
    *y = t;
}

int main()
{
    int a = 10, b = 20;
    printf("a = %d, b = %d\n", a, b);
    swap1(a, b);
    printf("a = %d, b = %d\n", a, b);
    swap2(&a, &b);
    printf("a = %d, b = %d", a, b);

    return 0;
}