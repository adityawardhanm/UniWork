#include <stdio.h>
#include <stdlib.h>

struct node {
    struct node* prev;
    int data;
    struct node* next;
};

struct node* reverse(struct node* head) {
    struct node* current = head;
    struct node* temp = NULL;

    while (current != NULL) {
        temp = current->prev;
        current->prev = current->next;
        current->next = temp;
        current = current->prev;
    }

    if (temp != NULL) {
        head = temp->prev;
    }

    return head;
}

void printlist(struct node* head) {
    if (head == NULL) {
        printf("Linked list is empty.\n");
        return;
    }

    struct node* ptr = head;
    while (ptr != NULL) {
        printf("%d ", ptr->data);
        ptr = ptr->next;
    }
    printf("\n");
}

int main() {
    struct node* head;
    struct node* middle;
    struct node* last;

    head = (struct node*)malloc(sizeof(struct node));
    middle = (struct node*)malloc(sizeof(struct node));
    last = (struct node*)malloc(sizeof(struct node));

    head->prev = NULL;
    head->data = 100;
    head->next = middle;

    middle->prev = head;
    middle->data = 200;
    middle->next = last;

    last->prev = middle;
    last->data = 300;
    last->next = NULL;

    head = reverse(head);
    printlist(head);

    return 0;
}
