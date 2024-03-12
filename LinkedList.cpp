
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

class LinkedList {
private:
    Node *head;
    int size = 0;
public:
    LinkedList() { head = nullptr; }

    void addFrontOfLL(int val) {
        Node *a = new Node(val, nullptr);
        if (head == nullptr) {
            head = a;
            size++;
        } else {
            a->next = head;
            head = a;
            size++;
        }
    }

    void addLastOfLL(int val) {
        Node *a = new Node(val, nullptr);
        if (head == nullptr) {
            head = a;
            size++;
        } else {
            Node *curr = head;
            while (curr->next != nullptr) {
                curr = curr->next;
            }
            curr->next = a;
            size++;
        }
    }

    int addDeclaredPlace(int val, int place) { // place possible least value starts from 1 not 0
        if (place > size || place <= 0) return 1;
        else {
            Node *newNode = new Node(val, nullptr);
            Node *curr = head;
            for (int i = 0; i < place - 1; ++i) { curr = curr->next; }
            Node *a = curr->next;
            curr->next = newNode;
            newNode->next = a;
            return 0;
        }
    }

    int deleteIndex(int index) {  // its possible least value is 0
        if (index > size || index < 0) return 1;
        else if (index == 0) {
            head = head->next;
            return 0;
        } else {
            Node *curr = head;
            for (int i = 0; i < index - 1; ++i) { curr = curr->next; }
            curr->next = curr->next->next;
            return 0;
        }
    }

    bool isEmpty(){
        return head == nullptr;
    }

    void print() {
        Node *curr = head;
        while (curr->next != nullptr) {
            std::cout << curr->data << " -> ";
            curr = curr->next;
        }
        std::cout << curr->data << std::endl;
    }
};

int main() {
    LinkedList ll;
    ll.addFrontOfLL(4);
    ll.addFrontOfLL(5);
    ll.addFrontOfLL(6);
    ll.addLastOfLL(1);
    ll.addDeclaredPlace(-9, 3);
    ll.print();
    ll.deleteIndex(0);
    ll.print();

    return 0;
}