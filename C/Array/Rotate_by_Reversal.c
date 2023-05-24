#include <stdio.h>

void reversal_right_rotate(int arr[], int start, int end){
    while(start<end){
        int temp;
        temp=arr[start];
        arr[start++]=arr[end];
        arr[end--]=temp;
    }
}

void arrange_reversal_rotate(int arr[], int n, int k){
    reversal_right_rotate(arr,0,n-k-1);
    reversal_right_rotate(arr,n-k,n-1);
    reversal_right_rotate(arr,0,n-1);
}

int main(){
    int n,k,i;
    printf("Number of Elements:");
    scanf("%d",&n);
    int arr[n];

    printf("The %d elements are:\n",n);
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }

    printf("Number of times to be rotated:");
    scanf("%d",&k);

    printf("The Original Array:\n");
    for(i=0;i<n;i++){
        printf("%d\n",arr[i]);
    }

    arrange_reversal_rotate(arr,n,k);
    printf("\nThe Final Array:\n");
    for(i=0;i<n;i++){
        printf("%d\n",arr[i]);
    }
    return 0;
}
