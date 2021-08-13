#include <stdio.h>

//? Divide and conquer (like MergeSort but around pivot not middle)
//! no extra array
//? put all smaller elements to its left and all larger to its right
//* here pivot is last element in each partition

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

int partitioning(int arr[], int first, int last) // index number passed not size
{
    int pivot = arr[last];
    int i = first - 1;

    int j = 0;
    for (j = first; j < last; j++) //will not compare last element as it is pivot
    {
        if (arr[j] < pivot)
        {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[last]); //swapping pivot at last to bring it behind all elements less than itself
    return i + 1;
}

void quick_sort(int arr[], int first, int last)
{
    if (first >= last)
    {
        return;
    }

    int x = partitioning(arr, first, last);

    quick_sort(arr, first, x - 1);
    quick_sort(arr, x + 1, last);
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

    quick_sort(numbers, 0, total - 1);

    printf("Sorted: \n");
    print_numbers(numbers, total);

    return 0;
}
