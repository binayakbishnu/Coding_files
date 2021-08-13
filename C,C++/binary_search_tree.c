#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *left;
    struct Node *right;
};

struct Node *root = NULL;

void insert(int d)
{
    struct Node *temp = NULL;
    temp = (struct Node *)malloc(sizeof(struct Node));
    // printf("Enter data: ");
    // scanf(" %d", &temp->data);
    temp->data = d;
    temp->left = NULL;
    temp->right = NULL;
    if (root == NULL)
    {
        root = temp;
    }
    else
    {
        struct Node *parent = NULL;
        struct Node *current = NULL;

        current = root;

        while (1)
        {
            parent = current;

            if (d < parent->data)
            {
                // current = current->left;

                if (current->left == NULL)
                {
                    current->left = temp;
                    current = current->left;
                    return;
                }
                current = current->left;
            }
            else if (d > parent->data)
            {
                // current = current->right;

                if (current->right == NULL)
                {
                    current->right = temp;
                    current = current->right;
                    return;
                }
                current = current->right;
            }
        }
    }
}

void pre_order_traversal(struct Node *root)
{
    if (root != NULL)
    {
        printf("%d", root->data);
        pre_order_traversal(root->left);
        pre_order_traversal(root->right);
        // printf("\n");
    }
}

void in_order_traversal(struct Node *root)
{
    if (root != NULL)
    {
        pre_order_traversal(root->left);
        printf("%d", root->data);
        pre_order_traversal(root->right);
        // printf("\n");
    }
}

void post_order_traversal(struct Node *root)
{
    if (root != NULL)
    {
        pre_order_traversal(root->left);
        pre_order_traversal(root->right);
        printf("%d", root->data);
        // printf("\n");
    }
}

int main()
{
    insert(5);
    insert(3);
    insert(8);
    insert(6);
    insert(4);
    insert(2);
    insert(7);

    // printf("%d",root->data);

    pre_order_traversal(root);
    printf("\n---\n");
    in_order_traversal(root);
    printf("\n---\n");
    post_order_traversal(root);
    printf("\n---\n");

    return 0;
}
