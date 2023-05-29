#include <stdio.h>
#include <stdlib.h>

struct node{
    int data;
    struct node*next;
};
void printlist(struct node*head){
    struct node*temp=head;
    while (temp!=NULL){
        printf("%d",temp->data);
        temp=temp->next;
    }
    printf("\n");
}
int main(){
    struct node*head;
    struct node*middle;
    struct node*last;

    head= (struct node*)malloc(sizeof(struct node));
    middle= (struct node*)malloc(sizeof(struct node));
    last= (struct node*)malloc(sizeof(struct node));

    head->data=100;
    middle->data=200;
    last->data=300;

    head->next = middle;
    middle->next = last;
    last->next = NULL;

    printlist(head);
    printlist(middle);
}
