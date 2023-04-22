#include <stdio.h>

int main() {
    int arr[10],pos,i,size,val;

    printf("Number of Elements:");
    scanf("%d",&size);

    printf("%d elements are: \n",size);
    for(i=0;i<size;i++){
        scanf("%d",&arr[i]);
    }
    printf("Position to insert:");
    scanf("%d",&pos);

    printf("Enter the Value:\n");
    scanf("%d",&val);

    for (i = size - 1; i >= pos; i--){
        arr[i+1] = arr[i];
    }
    arr[pos]=val;
    size++;

    printf("Final array is:\n");

    for(i=0;i<size;i++){
        printf("%d \n",arr[i]);
    }
    return 0;
}
