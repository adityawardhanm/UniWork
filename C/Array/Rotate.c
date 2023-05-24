#include <stdio.h>

void right_rotate(int arr[], int n){
    int temp= arr[n-1];int i;
    for(i=n-1;i>0;i--){arr[i]=arr[i-1];}
    arr[0]=temp;
}

void array_right_rotate(int arr[], int n, int k){
    int i;
    for(i=0;i<k;i++){
        right_rotate(arr,n);
    }
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

    array_right_rotate(arr,n,k);
    printf("\nThe Final Array:\n");
    for(i=0;i<n;i++){
        printf("%d\n",arr[i]);
    }
    return 0;
}
