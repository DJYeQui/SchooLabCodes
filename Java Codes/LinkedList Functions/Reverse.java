
public class Reverse {

    public Reverse() {
    }

    public LinkedList reverseLL(LinkedList LLForReverse) {
        System.out.print("before deletion: ");
        LLForReverse.print();
        LinkedList LL = new LinkedList();
        while (LLForReverse.getHead() != null) LL.insertLast(LLForReverse.deleteLast());
        LLForReverse = LL;
        System.out.print("after deletion: ");
        LLForReverse.print();

        return LLForReverse;
    }
}
