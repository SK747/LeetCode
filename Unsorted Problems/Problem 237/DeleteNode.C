/*  
    Date: December 18th 2018

    Leetcode Q. 237
    
    C Solution to merging deleting a node from a linked list
*/

#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int data; // data stored
    struct node *next; // pointer to the next node
}node_t;


void push(node_t * head, int val);
void deletenode(node_t * remove);
void display(struct node* head);
struct node* mergeTwoLists(struct node* l1, struct node* l2);


int main()
{

    // initializing linked list

    node_t * head = NULL;
    head = malloc(sizeof(node_t));

    node_t * head2 = NULL;
    head2 = malloc(sizeof(node_t));

    head->data = 1;
    head->next = NULL;

    head2->data = 1;
    head2->next = NULL;

    int testarray[] = { 2, 3, 4, 3, 5, 7, 8};

    for (int k = 0; k < 7; k++){
        push(head, testarray[k]);
    }

    for (int i = 3; i < 8; i++){
        push(head2, i);
    }

    display(head);
    display(head2);

    node_t * deleter = head;

    while (deleter->next != NULL) {
        if (deleter->data == 3){
            deletenode(deleter);
        }
        deleter = deleter->next;
    }

    display(head);

    return 0;
}

void push(node_t * head, int val) {
    node_t * current = head;
    while (current->next != NULL) {
        current = current->next;
    }

    /* now we can add a new variable */
    current->next = malloc(sizeof(node_t));
    current->next->data = val;
    current->next->next = NULL;
}

void deletenode(node_t * remove){
    node_t * temp;
    temp = remove->next;
    remove->data=temp->data;
    remove->next=temp->next;
    free(temp);
}

void display(struct node* head)
{
    struct node *current; // new pointer current, of type struct node
    current = head; // set this pointer to head
    if(current!= NULL)
    {
        printf("Linked List: ");
        do
        {
            printf("%d ",current->data); // access data in the current pointer to the struct node
            current = current->next;
        }
        while (current!= NULL);
        printf("\n");
    }
    else
    {
        printf("The List is empty\n");
    }

}
