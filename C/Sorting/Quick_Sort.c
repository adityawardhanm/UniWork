#include <stdio.h>
#include <stdlib.h>

void quicksort(int arr[], int first, int last){
    int i, j, pivot, temp;
    if(first < last){
        pivot = first;
        i = first;
        j = last;
        while (i < j){
            while (arr[i] <= arr[pivot] && i < last){
                i++;
            }
            while (arr[j] > arr[pivot]){
                j--;
            }
            if (i < j){
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        temp = arr[pivot];
        arr[pivot] = arr[j];
        arr[j] = temp;
        quicksort(arr, first, j-1);
        quicksort(arr, j+1, last);
    }
}


void printlist(int arr[], int n) {
    int i;
    for(i = 0; i < n; i++){
        printf("%d\n", arr[i]);
    }
}

int main() {
    int i, n;
    printf("Enter size of Array:\n");
    scanf("%d", &n);

    int arr[n];

    printf("Enter %d elements:\n", n);
    for(i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }

    printf("The Original Array:\n");
    printlist(arr, n);

    quicksort(arr,0,n-1);

    printf("The Sorted Array:\n");
    for(i = 0; i < n; i++){
        printf("%d\n", arr[i]);
    }

    return 0;
}
