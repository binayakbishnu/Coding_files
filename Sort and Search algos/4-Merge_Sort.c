#include <stdio.h>

//? recursion used
//? merge function merges left part (l to m) and right part (m+1 to r)
//? main sorting occurs in this ^^
//! add extra elements left out from left or right part
//? mergesort function divides and runs recursively

#define size 10

void print_numbers(int arr[], int n)
{
    int i = 0;
    for (i; i < n - 1; i++)
    {
        printf("%d, ", arr[i]);
    }
    printf("%d\n", arr[i]);
}

void merge(int arr[], int l, int m, int r)
{
    int left_size = m - l + 1; //^ l,m both included
    int right_size = r - m;    //^ m not included
    int left_subarr[size], right_subarr[size];

    int i;
    for (i = 0; i < left_size; i++)
    {
        left_subarr[i] = arr[l + i];
    }
    for (i = 0; i < right_size; i++)
    {
        right_subarr[i] = arr[m + 1 + i];
    }
    printf("\nAfter division\n");
    printf("Left: ");
    print_numbers(left_subarr, left_size);
    printf("Right: ");
    print_numbers(right_subarr, right_size);

    // merging...
    i = 0;
    int j = 0;
    int k = l; //for merged arr
    //! L not 1
    while (i < left_size && j < right_size)
    {
        if (left_subarr[i] <= right_subarr[j])
        {
            arr[k] = left_subarr[i];
            i++;
        }
        else
        {
            arr[k] = right_subarr[j];
            j++;
        }
        k++;
    }

    // extras...
    while (i < left_size)
    {
        arr[k] = left_subarr[i];
        i++;
        k++;
    }

    while (j < right_size)
    {
        arr[k] = right_subarr[j];
        j++;
        k++;
    }
    printf("\nMerged array\n");
    print_numbers(arr,k);
}

void merge_sort(int arr[], int l, int r)
{
    if (l >= r)
        return;

    int m = (l + r) / 2;
    //* prevent overflow for large l and r: (l+(r-1))/2
    merge_sort(arr, l, m);
    merge_sort(arr, m + 1, r);
    merge(arr, l, m, r);
}

int main()
{
    int total = 0;
    int numbers[size];

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

    merge_sort(numbers, 0, total - 1);

    printf("Sorted: \n");
    print_numbers(numbers, total);

    return 0;
}