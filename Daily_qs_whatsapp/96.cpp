#include <stdio.h>

#define size 10

using namespace std;

void print_list(int arr[], int n)
{
    int i;
    for (i = 0; i < n - 1; i++)
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

int binary_search(int arr[], int f, int r, int x)
{
    if (f > r)
    {
        return -1;
    }
    int m = f + (r - 1) / 2;

    if (arr[m] == x)
        return m;
    if (x < arr[m])
        return binary_search(arr, f, m - 1, x);
    if (x > arr[m])
        return binary_search(arr, m + 1, r, x);
}

void func96(int arr[], int n_, int k_)
{
    int i, r = 0;
    for (i = 0; i < n_; i++)
    {
        // printf("i = %d\n", arr[i]);
        int y = k_ - arr[i];
        // printf("y = %d\n", y);
        r = binary_search(arr, 0, n_ - 1, y);
        // printf("At index %d\n", r);

        if (r != -1)
        {
            printf("Exists\n");
            printf("%d at %d & %d at %d", arr[i], i, arr[r], r);
            return;
        }
    }
    printf("Does not exist");
    return;
}

int main()
{
    int list[size];
    int k, n;
    printf("k = ");
    scanf(" %d", &k);
    printf("n = ");
    scanf(" %d", &n);

    int i;
    for (i = 0; i < n; i++)
    {
        printf("Enter value: ");
        scanf(" %d", &list[i]);
    }

    merge_sort(list, 0, n - 1);

    print_list(list, n);

    func96(list, n, k);

    return 0;
}