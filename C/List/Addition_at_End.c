#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node* next;
};

struct node* head = NULL;

void add_end(int val) {
    struct node* new_node = malloc(sizeof(struct node));
    new_node->data = val;
    new_node->next = NULL;

    if (head == NULL) {
        head = new_node;
    } else {
        struct node* last_node = head;
        while (last_node->next != NULL) {
            last_node = last_node->next;
        }
        last_node->next = new_node;
    }
}

void printlist(struct node* head) {
    struct node* temp = head;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

int main() {
    add_end(100);
    add_end(200);
    printlist(head);
    add_end(300);
    printlist(head);
}
