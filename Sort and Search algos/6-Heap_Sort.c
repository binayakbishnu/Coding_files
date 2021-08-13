#include <stdio.h>


//? similar to selection sort
//? lowest element moved forward
//? i runs n/2 -1 to >=0 to heapify
//? i runs n-1 to >0 to swap and heapify
//? heapify function creates heaps
//? sorting starts from index 0

//* In-place
//* Unstable

void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

void heapify(int arr[], int n, int i)
{
    int largest = i;       // Initialize largest as root
    int left = 2 * i + 1;  // left = 2*i + 1
    int right = 2 * i + 2; // right = 2*i + 2

    // If left child is larger than root
    if (left < n && arr[left] > arr[largest])
        largest = left;

    // If right child is larger than largest so far
    if (right < n && arr[right] > arr[largest])
        largest = right;

    // If largest is not root
    if (largest != i)
    {
        swap(&arr[i], &arr[largest]);

        // Recursively heapify the affected sub-tree
        heapify(arr, n, largest);
    }
}

void heap_sort(int arr[], int n)
{
    // Build heap (rearrange array)
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    // One by one extract an element from heap
    for (int i = n - 1; i > 0; i--)
    {
        // Move current root to end
        swap(&arr[0], &arr[i]);

        // call max heapify on the reduced heap
        heapify(arr, i, 0);
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

    heap_sort(numbers, total);

    printf("Sorted: \n");
    print_numbers(numbers, total);

    return 0;
}
