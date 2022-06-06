#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *joint;
};

int isEmpty(struct node *h)
{
    /*
    if (head == NULL)
        return 1;
    else
        return 0;
    */
    return h == NULL;
}

void insertbegin(struct node** head,int x)
{
    struct node *temp = NULL;
    temp = (struct node *)malloc(sizeof(struct node));
    if (!temp)
    {
        printf("Heap overflow");
        exit(1);
    }
    temp->data = x;
    temp->joint = NULL;

    if (*head == NULL)
    {
        *head = temp;
    }
    else
    {
        temp->joint = *head;
        *head = temp;
    }
}

void insertend(struct node** head,int x)
{
    struct node *temp = NULL;
    temp = (struct node *)malloc(sizeof(struct node));

    if (!temp)
    {
        printf("Heap overflow");
        exit(1);
    }
    temp->data = x;
    temp->joint = NULL;

    if (*head == NULL)
    {
        *head = temp;
    }
    else
    {
        struct node *temp2 = NULL;
        temp2 = *head;
        while (temp2->joint != NULL)
        {
            temp2 = temp2->joint;
        }
        temp2->joint = temp;
    }
}

void display(struct node *head)
{
    if (isEmpty(head))
        printf("Stack empty");
    else
    {
        struct node *temp = NULL;
        temp = head;
        while (temp->joint != NULL)
        {
            printf("%d->", temp->data);
            temp = temp->joint;
        }
        printf("%d\n", temp->data);
    }
}

int main()
{
    struct node *head = NULL;

    insertbegin(&head, 2);
    insertbegin(&head, 3);
    insertbegin(&head, 9);
    display(head);

    insertend(&head, 5);
    insertend(&head, 1);

    display(head);

    insertbegin(&head, 8);
    display(head);
    
    return 0;
}