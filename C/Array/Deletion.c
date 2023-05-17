#include <stdio.h>

int main() {
    int arr[100],pos,c,n;
    printf("Number of Elements:");
    scanf("%d",&n);
    printf("The %d elements are:\n",n);
    for(c=0;c<n;c++){
        scanf("%d",&arr[c]);
    }
    printf("The location of element to be deleted:");
    scanf("%d",&pos);
    if(pos>=n+1){
        printf("Invalid Input");
    }
    else{
        for(c=pos;c<n-1;c++){
            arr[c]=arr[c+1];
        }
        printf("Result Array is \n");
        for(c=0;c<n-1;c++){
            printf("%d\n",arr[c]);
        }
    }
    return 0;
}
