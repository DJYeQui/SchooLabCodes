#include <iostream>

class Node {
public:
    int data;
    Node *next;

    Node(int value, Node *n) {
        data = value;
        next = n;
    }
};

class Queue {
private:
    Node *head;
    int counter = 0;

public:
    Queue() { head = nullptr; }

    void enQ(int val) {
        Node *nodeWhichWillAdd = new Node(val, nullptr);

        if (head == nullptr) {
            head = nodeWhichWillAdd;
            counter++;
        }
        else {
            Node *p = head;
            while (p->next != nullptr){p = p->next;}
            counter++;
            p->next = nodeWhichWillAdd;
        }
    }

    void deQ() {
        head = head->next;
        counter--;
    }

    Node top() {
        return *head;
    }

    bool isEmpty() {
        return head == nullptr;
    }

    int size() {
        return counter;
    }


    void print() {
        Node *curr = head;
        while (curr->next != nullptr) {
            std::cout << curr->data << " -> ";
            curr = curr->next;
        }
        std::cout << curr->data << std::endl;
        std::cout << "size of Q: " << size() << std::endl;
    }
};

int main() {
    Queue q;
    q.enQ(1);
    q.enQ(2);
    q.enQ(3);
    q.enQ(4);
    q.print();
    q.deQ();
    q.print();

    return 0;
}
