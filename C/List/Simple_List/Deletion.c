#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node* next;
};

void delete_node(struct node ** head, int key) {
    struct node * temp;
    if((*head)-> data ==key){
        temp = *head;
        *head = (*head)->next;
        free(temp);
    }
    else{
        struct node * current_node = *head;
        while (current_node->next!=NULL){
            if(current_node -> next->data==key){
                temp = current_node->next;
                current_node->next=current_node->next->next;
                free(temp);
                break;
            }
            else{
                current_node=current_node->next;
            }
        }
    }
}

void printlist(struct node* Node) {
    while (Node != NULL) {
        printf("%d ", Node->data);
        Node = Node->next;
    }
    printf("\n");
}

int main() {
    struct node *head = NULL;
    struct node *middle = NULL;
    struct node *last = NULL;

    head = malloc(sizeof(struct node));
    middle = malloc(sizeof(struct node));
    last = malloc(sizeof(struct node));

    head->data = 100;
    middle->data = 200;
    last->data = 300;

    head->next = middle;
    middle->next = last;
    last->next = NULL;

    printlist(head);
    delete_node(&head, 200);
    printlist(head);
    return 0;
}
