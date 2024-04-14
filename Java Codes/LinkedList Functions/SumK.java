
public class SumK {
    private Node head;

    public SumK(Node h) {
        head = h;
    }

    public void SumK(int k) {
        print(head);
        int sumOfNodes = 0;
        Node startPoint = head;
        Node endPoint;

        Node curr = head;
        while (curr != null) {
            sumOfNodes += curr.value;
            if (sumOfNodes == k) {
                endPoint = curr;
                deleteInterval(startPoint, endPoint);
                sumOfNodes = 0;
                curr = head;
                startPoint = head;
                continue;
            } else if (sumOfNodes > k) {
                sumOfNodes = 0;
                startPoint = curr;
                continue;
            }
            curr = curr.next;
        }
    }

    public void deleteInterval(Node startNode, Node endNode) {
        System.out.println("star: " + startNode.value + " end " + endNode.value + " head " + head.value);
        Node deletionStartNode = new Node(0);

        Node curr = head;
        if (head.equals(startNode)) {
            while (curr != null) {
                if (curr.equals(endNode)) {
                    if (curr == null) {
                        head = null;
                    } else {
                        head = curr.next;
                    }
                    break;
                }
                curr = curr.next;
            }
        } else {
            while (curr.next != null) {
                if (curr.next.equals(startNode)) {
                    deletionStartNode = curr;
                }
                if (curr.equals(endNode)) {
                    deletionStartNode.next = curr.next;
                    break;
                }
                curr = curr.next;
            }
        }
        print(head);
    }

    public void print(Node head) {
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
}
