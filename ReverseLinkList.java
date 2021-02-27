package reverse;

public class ReverseLinkList {
	static Node head;
	 
    static class Node {
 
        int data;
        Node next;
 
        Node(int d)
        {
            data = d;
            next = null;
        }
    }
 
 
    Node reverse(Node node)
    {
        Node prev = null;
        Node current = node;
        Node next = null;
        while (current != null) {
            next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        node = prev;
        return node;
    }
 
 
    void printList(Node node)
    {
        while (node != null) {
            System.out.print(node.data + " ");
            node = node.next;
        }
    }
 
   
    public static void main(String[] args)
    {
        ReverseLinkList list = new ReverseLinkList();
        list.head = new Node(6);
        list.head.next = new Node(7);
        list.head.next.next = new Node(11);
        list.head.next.next.next = new Node(31);
 
        System.out.println("Given");
        list.printList(head);
        head = list.reverse(head);
        System.out.println("");
        System.out.println("Reversed linked list ");
        list.printList(head);
    }

}
