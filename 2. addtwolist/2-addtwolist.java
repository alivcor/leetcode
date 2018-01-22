/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode revList(ListNode h){
        if(h==null || h.next==null){
            return h;
        }
        ListNode p1 = h;
        ListNode p2 = h.next;
        h.next = null;
        while(p1!=null && p2 != null){
            ListNode t = p2.next;
            p2.next = p1;
            p1 = p2;
            p2 = t;
        }
        return p1;
    }
    public ListNode getsumList(long sum){
        int d = (int) (sum%10);
        ListNode b = new ListNode(d);
        ListNode head = b;
        sum = sum/10;
        while(sum!=0){
            d = (int) (sum%10);
            ListNode a = new ListNode(d);
            sum = sum/10;
            b.next = a;
            b = a;
        }
        return head;
    }
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        long rx = 1;
        ListNode r1 = l1;
        ListNode r2 = l2;
        ListNode q1 = r1;
        ListNode q2 = r2;
        while(q1!=null){
            //System.out.println(q1.val);
            q1 = q1.next;
        }
        while(q2!=null){
            //System.out.println(q2.val);
            q2 = q2.next;
        }
        long n1=0, n2=0;
        long nsum=0;
        while(r1!=null){
            n1 = n1 +  (r1.val)*rx;
            rx = rx*10;
            r1 = r1.next;
        }
        rx = 1;
        while(r2!=null){
            n2 = n2 +  (r2.val)*rx;
            rx = rx*10;
            r2 = r2.next;
        }
        System.out.println(n1);
        System.out.println(n2);
        nsum = n1 + n2;
        ListNode sumList = getsumList(nsum);
        System.out.println(nsum);
        return sumList;
    }
}
