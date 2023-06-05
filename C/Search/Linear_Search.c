#include <stdio.h>
#include <stdlib.h>

int main(){
    int i, n, x;
    int size;
    printf("Enter size of Array:\n");
    scanf("%d",&n);
    int arr[n];
    printf("Enter %d elements:\n",n);
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }

    printf("Enter the element to be found:\n");
    scanf("%d",&x);

    for (i=0;i<n;i++){
        if (arr[i]==x){
            printf("Element is present at index %d \n",i);
            break;
        }
    }
    if (i>n){
        printf("Element is not present in the array \n");
    }
    return 0;
}
