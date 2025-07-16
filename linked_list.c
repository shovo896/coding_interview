#include <stdio.h>
#include <stdlib.h>

// Define the node structure
struct Node {
    int data;
    struct Node* next;
};

int main() {
    int n, val;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    struct Node* head = NULL;
    struct Node* temp = NULL;
    struct Node* newNode;

    // Create linked list using for loop
    for (int i = 0; i < n; i++) {
        printf("Enter value %d: ", i + 1);
        scanf("%d", &val);

        newNode = (struct Node*)malloc(sizeof(struct Node));
        newNode->data = val;
        newNode->next = NULL;

        if (head == NULL) {
            head = newNode;
            temp = newNode;
        } else {
            temp->next = newNode;
            temp = newNode;
        }
    }

    // Display the linked list
    printf("Linked list elements: ");
    for (temp = head; temp != NULL; temp = temp->next) {
        printf("%d ", temp->data);
    }
    printf("\n");

    // Free memory
    for (temp = head; temp != NULL; ) {
        struct Node* toFree = temp;
        temp = temp->next;
        free(toFree);
    }

    return 0;
}
