
#include <stdio.h>
#include <stdlib.h>

struct node {
    struct node* prev;
    int data;
    struct node* next;
};

int size = 0;
struct node* head, *tail = NULL;

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

void addnode(int val) {
    struct node *new_node = (struct node*)malloc(sizeof(struct node));
    new_node->data = val;

    if (head == NULL) {
        head = tail = new_node;
        head->prev = NULL;
        tail->next = NULL;
    }
    else {
        tail->next = new_node;
        new_node->prev = tail;
        tail = new_node;
        tail->next = NULL;
    }
    size++;
}

void addmiddle(int val, struct node *head, struct node *last) {
    while (head != last) {
        if (((head->prev) == last) && ((last->next) == last)) {
            break;
        }
        head = head->next;
        last = last->prev;
    }
    struct node *a = NULL;
    a = (struct node*)malloc(sizeof(struct node));
    struct node *b = NULL;
    b = (struct node*)malloc(sizeof(struct node));

    b->data = val;
    a = head->prev;
    a->next = b;
    b->prev = a;
    b->next = head;
    head->prev = b;
}

void printlist() {
    struct node* ptr = head;
    if (head == NULL) {
        printf("Linked list is empty.\n");
        return;
    }

    while (ptr != NULL) {
        printf("%d ", ptr->data);
        ptr = ptr->next;
    }
    printf("\n");
}

int main() {
    addnode(100);
    addnode(200);
    addnode(300);
    addnode(400);
    addnode(500);

    printf("The Original Array:\n");
    printlist();
    addmiddle(250, head, tail);

    printf("The Final Array:\n");
    printlist();
    return 0;
}
