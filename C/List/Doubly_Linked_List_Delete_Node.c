
#include <stdio.h>
#include <stdlib.h>

struct node {
    struct node* prev;
    int data;
    struct node* next;
};

int size = 0;
struct node* head, *tail = NULL;

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
void deletenode(struct node** head, int key){
    struct node *temp;
    if ((*head) -> data==key){
        temp = *head;
        *head = (*head) -> next;
        free(temp);
    }
    else{
        struct node * current =* head;
        while(current -> next !=NULL){
            if (current -> next -> data == key){
                temp = current -> next;
                current -> next = current -> next -> next;
                free (temp);
                break;
            }
            else{
                current = current -> next;
            }
        }
    }
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

    deletenode(&head, 300);

    printf("The Final Array:\n");
    printlist();
    return 0;
}
