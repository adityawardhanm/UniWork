#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int max_element(int arr[], int n){
    int max = INT_MIN;
    for (int i = 0; i < n; i++){
        if (arr[i] > max){
            max = arr[i];
        }
    }
    return max;
}

void bucketsort(int arr[], int n){
    int max = max_element(arr, n);
    int bucket[max + 1];
    for (int i = 0; i < max + 1; i++){
        bucket[i] = 0;
    }
    for (int i = 0; i < n; i++){
        bucket[arr[i]]++;
    }
    int j = 0;
    for (int i = 0; i <= max; i++){
        while (bucket[i] > 0){
            arr[j++] = i;
            bucket[i]--;
        }
    }
}

void printlist(int arr[], int n) {
    for(int i = 0; i < n; i++){
        printf("%d\n", arr[i]);
    }
}

int main() {
    int n;
    printf("Enter size of Array:\n");
    scanf("%d", &n);

    int arr[n];

    printf("Enter %d elements:\n", n);
    for(int i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }

    printf("The Original Array:\n");
    printlist(arr, n);

    bucketsort(arr, n);

    printf("The Sorted Array:\n");
    printlist(arr, n);

    return 0;
}
