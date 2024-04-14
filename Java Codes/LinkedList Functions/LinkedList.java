
public class LinkedList {
    private Node head;

    public LinkedList() {
        head = null;
    }

    public void insertFirst(int val) {
        Node newNode = new Node(val);
        if (head == null) head = newNode;
        else {
            newNode.next = head;
            head = newNode;
        }
    }

    public void insertLast(int val) {
        Node newNode = new Node(val);
        if (head == null) head = newNode;
        else {
            Node curr = head;
            while (curr.next != null) {
                curr = curr.next;
            }
            curr.next = newNode;
        }
    }

    public void insertAfter(int val, int index) {
        Node newNode = new Node(val);
        if (head == null) head = newNode;
        else {
            Node curr = head;
            for (int i = 0; i < index - 1; i++) {
                curr = curr.next;
            }
            Node nextOf = curr.next;
            curr.next = newNode;
            newNode.next = nextOf;
        }
    }

    public int deleteFirst() {
        int storeValue = 0;
        if (head != null) {
            storeValue = head.value;
            head = head.next;
        }
        return storeValue;
    }

    public int deleteLast() {
        int value = Integer.MAX_VALUE;
        Node storedAdress = new Node(0);
        if (head != null) {
            Node curr = head;
            if (curr.next == null) {
                value = curr.value;
                head = null;
            } else {
                while (curr.next.next != null) {
                    curr = curr.next;
                    if (curr.next.next == null) {storedAdress = curr.next; break;}
                }
                if (curr.next.next == null) storedAdress = curr.next;
                value = storedAdress.value;
                curr.next = null;
            }
        }
        return value;
    }

    public void deleteNode(int val) {
        if (head != null) {
            Node curr = head;
            while (curr.next != null) {
                if (curr.next != null && curr.next.value == val) break;
                curr = curr.next;
            }
            if (curr.next != null && curr.next.value == val) {
                curr.next = curr.next.next;
            } else {
                System.out.println("there is not searched Node in LL");
            }
        }
    }

    public void print() {
        if (head == null) {
            System.out.println("There is not any Node in LL");
            return;
        }
        Node curr = head;
        while (curr.next != null) {
            System.out.print(curr.value + " -> ");
            curr = curr.next;
        }
        System.out.println(curr.value);
    }

    public Node getHead() {
        return head;
    }
}
