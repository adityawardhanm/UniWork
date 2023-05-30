#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node* next;
};
struct node* head = NULL;

void push(int val) {
    struct node* new_node = malloc(sizeof(struct node));
    new_node->data = val;
    if (head == NULL) {
        new_node->next = NULL;
    }
    else {
        new_node->next = head;
    }
    head = new_node;
}

int pop() {
    if (head == NULL) {
        printf("Stack Underflow\n");
        return -1;
    }
    else {
        struct node* temp = head;
        int temp_data = head->data;
        head = head->next;
        free(temp);
        return temp_data;
    }
}

void display() {
    if (head == NULL) {
        printf("Stack Underflow\n");
    }
    else {
        printf("The Stack is: ");
        struct node* temp = head;
        while (temp != NULL) {
            printf("%d ", temp->data);
            temp = temp->next;
        }
        printf("\n");
    }
}

int main() {
    int choice, value;
    printf("Stack using linked list\n");
    while (1) {
        printf("\n1.Push\n2.Pop\n3.Display\n4.Exit\n");
        printf("Enter Your Choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                printf("Enter Value to Insert: ");
                scanf("%d", &value);
                push(value);
                break;
            case 2:
                printf("Popped element is %d\n", pop());
                break;
            case 3:
                display();
                break;
            case 4:
                exit(0);
                break;
            default:
                printf("Choose Correct Choice\n");
                break;
        }
    }
    return 0;
}
