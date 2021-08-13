#include <stdio.h>

struct emp
{
    int id;
    char name[10];
    float salary;
    char category;
};
int main()
{
    int number;
    scanf(" %d", &number);
    struct emp E[number];
    int i;
    for (i = 0; i < number; i++)
    {
        scanf(" %d", &E[i].id);
        scanf(" %s", &E[i].name);
        scanf(" %f", &E[i].salary);
        if (E[i].salary <= 0)
            printf("invalid ouput");
        else if (E[i].salary<500)
            E[i].category='A';
        else
            E[i].category='B';
    }
    struct emp temp;
    int j=0;
    for (i=0;i<number;i++)
    {
        for (j=0;j<number-i-1;j++)
        {
            if (E[j].salary>E[j+1].salary)
            {
                temp = E[j];
                E[j] = E[j+1];
                E[j+1] = temp;
            }
        }
    }
    for (i = 0; i < number; i++)
    {
        printf("%d\n", E[i].id);
        printf("%s\n", E[i].name);
        printf("%.2f\n", E[i].salary);
        printf("%c\n",E[i].category);
    }
    return 0;
}
