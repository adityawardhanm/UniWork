#include <stdio.h>

int josephus(int n, int k){
    if (n == 1){
        return n;
    }
    else{
        return (josephus(n - 1, k) + k - 1) % n + 1;
    }
}

int main()
{
    int n, k;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    printf("Enter the value of k: ");
    scanf("%d", &k);
    printf("The safe place is %d\n", josephus(n, k));
    return 0;
}
