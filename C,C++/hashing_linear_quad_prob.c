#include <stdio.h>
#include <stdlib.h>

#define size 10

int hash_table[size] = {NULL};

void insert()
{
    int key;
    int index, h_key;

    printf("Enter value to be inserted: ");
    scanf(" %d", &key);

    h_key = key % size; // ideal position

    int i;
    for (i = 0; i < size; i++)
    {
        index = (h_key + i) % size; //alternative position
        //*starts with ideal position

        if (hash_table[index] == NULL)
        {
            hash_table[index] = key;
            break;
        }
    }
    if (i == size)
    {
        printf("\nCannot insert anymore\n");
    }
}

void insert2()
{
    int key;
    int index, h_key;

    printf("Enter value to be inserted: ");
    scanf(" %d", &key);

    h_key = key % size; // ideal position

    int i;
    for (i = 0; i < size; i++)
    {
        index = (h_key + i * i) % size; //alternative position
        //*starts with ideal position

        if (hash_table[index] == NULL)
        {
            hash_table[index] = key;
            break;
        }
    }
    if (i == size)
    {
        printf("\nCannot insert anymore\n");
    }
}

void search()
{
    int key, h_key, index;

    printf("Enter value to be searched for: ");
    scanf(" %d", &key);

    h_key = key % size; //ideal position to be found at

    int i;
    for (i = 0; i < size; i++)
    {
        index = (h_key + i) % size;

        if (hash_table[index] == key)
        {
            printf("Found at: %d\n", index);
            break;
        }
    }
    if (i == size)
    {
        printf("\nNot found\n");
    }
}

void display()
{
    int i;
    for (i = 0; i < size - 1; i++)
    {
        printf("%d. %d\n", i, hash_table[i]);
    }
    printf("%d. %d\n", i, hash_table[i]);
}

int main()
{
    int choice = 1;
    char method = 'L';

    printf("Choose method (L/Q): ");
    scanf(" %c", &method);

    if (method == 'L')
    {
        while (1)
        {
            printf("1. Add\n2. Search\n3. Display\n4. Exit\n");
            scanf(" %d", &choice);

            if (choice == 1)
            {
                insert();
            }
            else if (choice == 2)
            {
                search();
            }
            else if (choice == 3)
            {
                display();
            }
            else
            {
                break;
            }
        }
    }
    else
    {
        while (1)
        {
            printf("1. Add\n2. Search\n3. Display\n4. Exit\n");
            scanf(" %d", &choice);

            if (choice == 1)
            {
                insert2();
            }
            else if (choice == 2)
            {
                search();
            }
            else if (choice == 3)
            {
                display();
            }
            else
            {
                break;
            }
        }
    }

    return 0;
}