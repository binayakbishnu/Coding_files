#include <stdio.h>


//? i runs 1 (NOT 0) to <n
//? while loop to insert ith element between those less than it and those more than it
//? sorting starts from left side
//? no swapping occurs


void insertion_sort(int arr[], int n)
{
    int i, j, x;

    for (i = 1; i < n; i++)
    {
        x = arr[i];
        j = i-1;
        //* pushing those which are greater than x one step backwards
        while (j>=0 && arr[j] > x)
        {
            arr[j+1] = arr[j];
            j -= 1;
        }
        //! j is now -1
        arr[j+1] = x;
    }
}

void print_numbers(int arr[],int n)
{
    int i=0;
    for (i;i<n-1;i++)
    {
        printf("%d, ", arr[i]);
    }
    printf("%d\n",arr[i]);
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

    insertion_sort(numbers, total);

    printf("Sorted: \n");
    print_numbers(numbers, total);


    return 0;
}