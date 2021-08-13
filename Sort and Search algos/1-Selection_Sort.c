#include <stdio.h>

//? i increments 0 to n-2
//? j runs i+1 to n-1
//? if j element is less than i element, swap them
//? sorting starts from index 0
//? lowest number in array excluding one just sorted moved forward

void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

void selection_sort(int arr[], int n)
{
    int i, j;

    for (i = 0; i < n - 1; i++)
    {
        int m = i;
        for (j = i + 1; j < n; j++)
        {
            if (arr[j] < arr[m])
            {
                m = j;
            }
        }
        swap(&arr[m], &arr[i]);
    }
}

void print_numbers(int arr[], int n)
{
    int i = 0;
    for (i; i < n - 1; i++)
    {
        printf("%d, ", arr[i]);
    }
    printf("%d\n", arr[i]);
}

int main()
{
    int numbers[10];
    int total = 0;

    printf("Enter number of elements: ");
    scanf(" %d", &total);

    int k = 0;
    for (k; k < total; k++)
    {
        printf("Enter element: ");
        scanf(" %d", &numbers[k]);
    }

    printf("Unsorted: \n");
    print_numbers(numbers, total);

    selection_sort(numbers, total);

    printf("Sorted: \n");
    print_numbers(numbers, total);

    return 0;
}