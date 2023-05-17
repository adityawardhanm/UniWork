#include <stdio.h>
#include <conio.h>

int main() {
    int arr[100],key,i,n;
    printf("Number of Elements:");
    scanf("%d",&n);

    printf("The %d elements are:\n",n);
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }

    printf("The Element to be searched:");
    scanf("%d",&key);

    for(i=0;i<n;i++){
        if(arr[i]==key){
            printf("Element found at %d\n",i);
        }
    }
    return 0;
