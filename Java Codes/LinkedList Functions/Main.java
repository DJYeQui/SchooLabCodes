public class Main {
    public static void main(String[] args) {
        LinkedList LL = new LinkedList();
        Reverse func = new Reverse();
        LinkedList LL2 = new LinkedList();
        LL2.insertLast(95);
        LL2.insertLast(96);
        LL2.insertLast(97);
        LL2.insertLast(98);
        LL2.insertLast(99);
        LL2.insertLast(100);

        LL.insertLast(2);
        LL.insertLast(3);
        LL.insertLast(4);
        LL.insertLast(5);
        LL.insertLast(6);
        LL.insertAfter(9999,2);
        LL.insertFirst(-1);
        LL.print();
        LL.deleteNode(3);
        LL.print();


        func.reverseLL(LL2);


        LinkedList llSum = new LinkedList();
        llSum.insertLast(1);
        llSum.insertLast(2);
        llSum.insertLast(3);
        llSum.insertLast(4);
        llSum.insertLast(7);
        llSum.insertLast(8);
        llSum.insertLast(2);
        llSum.insertLast(3);
        llSum.insertLast(4);
        llSum.insertLast(6);

        SumK sumK = new SumK(llSum.getHead());
        sumK.SumK(10);

    }


}