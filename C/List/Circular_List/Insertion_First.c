#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node* link;
};

struct node * last = NULL;

void addnode(int val){
    struct node * temp;
    temp = malloc(sizeof (struct node));
    if (last == NULL){
        temp -> data = val;
        temp -> link = temp;
        last = temp;
    }
    else{
        temp -> data = val;
        temp -> link = last -> link;
        last -> link = temp;
    }
}


void printlist() {
    if (last == NULL) {
        printf("Linked list is empty.\n");
    }
    else {
        struct node *temp;
        temp = last -> link;
        do{
            printf(" %d",temp -> data);
            temp = temp -> link;
        }while (temp != last -> link);
    }
    printf("\n");

}

int main() {
    addnode(100);
    addnode(200);
    addnode(300);

    printf("The Original Array:\n");
    printlist();
}
