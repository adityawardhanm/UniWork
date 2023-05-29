#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node* link;
};

void printlist(struct node* head) {
    if (head == NULL) {
        printf("Linked list is empty.\n");
    }
    else {
        struct node *temp;
        temp = head->link;
        do{
            printf(" %d",temp -> data);
            temp = temp -> link;
        }while (temp != head ->link);
    }
    printf("\n");

}

int main() {
    struct node * a, *b, *c;
    a = malloc(sizeof(struct node));
    b = malloc(sizeof(struct node));
    c = malloc(sizeof(struct node));

    a -> data = 100;
    a -> link = b;

    b -> data = 200;
    b -> link = c;

    c -> data = 300;
    c -> link = a;

    printf("The Original Array:\n");
    printlist(c);
}
