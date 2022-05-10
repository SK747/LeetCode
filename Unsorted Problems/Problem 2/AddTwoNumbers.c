/*  
    Date: January 11th 2019
    Leetcode Q. 2
    Add two numbers (stored as a reverse linked list) and return solution as a linked list.
*/

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {

    int x=(l1->data+l2->data)/10;

    struct ListNode* head = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* p=head;
    struct ListNode* s;
    head->data = (l1->data+l2->data)%10;
    head->next=NULL;
    l1=l1->next;l2=l2->next;

    while(l1!=NULL || l2!=NULL){

        int a = l1==NULL:l1->data;
        int b = l2==NULL:l2->data;

       s = (struct ListNode*)malloc(sizeof(struct ListNode));

       s->data = (a+b+x)%10;
       s->next=NULL;
       p->next=s;
       p=s;
       x = (a+b+x)/10;
       l1 = l1==NULL?NULL:l1->next;
       l2 = l2==NULL?NULL:l2->next;
    }
    if(x!=0){
       s = (struct ListNode*)malloc(sizeof(struct ListNode));
       s->data = x;
       s->next=NULL;
       p->next=s;
    }
    return head;
}
