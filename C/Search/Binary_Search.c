#include <stdio.h>
#include <stdlib.h>

int bisearch(int arr[], int l, int r, int x){
    if (r>=1){
        int mid = 1 + (r-1)/2;
        if (arr[mid]==x){
            return mid;
        }
        if (arr[mid]>x){
            return bisearch(arr,l,mid-1,x);
        }
        return bisearch(arr,mid+1, r, x);
    }
    return -1;
}

int main(){
    int size;
    printf("Enter size of Array:\n");
    scanf("%d",&size);
    int arr[size], i;
    printf("Enter %d elements:\n",size);
    for(i=0;i<size;i++){
        scanf("%d",&arr[i]);
    }

    int n = sizeof(arr)/sizeof(arr[0]);
    int x;
    printf("Enter the element to be found:\n");
    scanf("%d",&x);
    int result = bisearch(arr,0,n-1,x);
    if (result!=-1){
        printf("Element is present at index %d \n",result);
    }
    else{
        printf("Element is not present in the array \n");
    }
}
