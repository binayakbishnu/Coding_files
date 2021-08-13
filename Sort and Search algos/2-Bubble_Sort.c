#include <stdio.h>


//? i runs 0 to < n-1 (n-1 rounds of swapping enough)
//? j runs 0 to < n-i-1
//? if j+1 < j, swap
//? sorting starts from last index
//? each ith element swapped with next unless next is larger or j reaches n-i-1


void print_numbers(int arr[], int n)
{
    int i = 0;
    for (i; i < n - 1; i++)
    {
        printf("%d, ", arr[i]);
    }
    printf("%d\n", arr[i]);
}

void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

void bubble_sort(int arr[], int n)
{
    int i, j;

    for (i = 0; i < n - 1; i++)
    {
        // printf("\ni=%d\n",i);
        for (j = 0; j < n - i - 1; j++)
        {
            if (arr[j + 1] < arr[j])
            {
                swap(&arr[j], &arr[j + 1]);
            }
            // print_numbers(arr, n);
        }
    }
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

    bubble_sort(numbers, total);

    printf("Sorted: \n");
    print_numbers(numbers, total);

    return 0;
}