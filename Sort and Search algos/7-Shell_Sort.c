// C++ implementation of Shell Sort
#include <stdio.h>


//? Variation of insertion sort
//? Reduce number of movements when moving element
//? comparison is not with adjacent
//? comparison is between those separated by amount = gap


void printArray(int arr[], int n)
{
	int i = 0;
	for (i=0; i<n-1; i++)
		printf("%d ",arr[i]);

	printf("%d\n",arr[n-1]);
}

int shellSort(int arr[], int n)
{
	// Start with a big gap, then reduce the gap
	int gap = 0;
	for (gap = n/2; gap > 0; gap /= 2)
	{
		printf("Gap = %d\n",gap);
		// Do a gapped insertion sort for this gap size.
		// The first gap elements a[0..gap-1] are already in gapped order
		// keep adding one more element until the entire array is
		// gap sorted
		int i = 0;
		for (i = gap; i < n; i += 1)
		{
			printf("i = %d\n",i);
			// add a[i] to the elements that have been gap sorted
			// save a[i] in temp and make a hole at position i
			int temp = arr[i];

			// shift earlier gap-sorted elements up until the correct
			// location for a[i] is found
			int j = 0;		
			for (j = i; j >= gap && arr[j - gap] > temp; j -= gap)
			{
				printf("j = %d\n",j);
				printf("Half-swapping...\n");
				arr[j] = arr[j - gap];
				printf("End of j iteration: ");
				printArray(arr,n);
			}
			
			// put temp (the original a[i]) in its correct location
			printf("j outside j-loop = %d\n",j);
			arr[j] = temp;
			printf("***End of i iteration: ");
			printArray(arr,n);
		}
		printf("End of gap iteration: ");
		printArray(arr,n);
	}
	return 0;
}

int main()
{
	int arr[] = {9, 8, 3, 7, 5, 6, 4, 1};
	int i = 0;
	int n = sizeof(arr)/sizeof(arr[0]);

	printf("Initial: ");
	printArray(arr, n);

	shellSort(arr, n);

	printf("Final: ");
	printArray(arr, n);

	return 0;
}

