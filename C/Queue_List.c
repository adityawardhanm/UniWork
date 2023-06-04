#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node* next;
};

struct node* front = NULL;
struct node* rear = NULL;

void printlist(struct node* head) {
    struct node* temp = head;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

void enqueue(int val){
    struct node* head = (struct node*) malloc(sizeof(struct node));
    if (head == NULL){
        printf("Queue is full");
    }
    else{
        head->data = val;
        head->next = NULL;
        if (front == NULL){
            front = rear = head;
        }
        else{
            rear->next = head;
            rear = head;
        }
    }
}

void dequeue(){
    struct node* head = front;
    if (front == NULL){
        printf("The Queue is Empty");
    }
    else{
        front = front->next;
        free(head);
        if (front == NULL){
            rear = NULL;
        }
    }
}

int main(){
    enqueue(100);
    enqueue(200);
    enqueue(300);
    printf("\n");
    printlist(front);
    printf("\n");
    dequeue();
    printlist(front);
    return 0;
}
