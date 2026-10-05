import java.util.*;

// Tried my DSA on java  
// class Add_Two_Numbers {
//     public static void main(String[] args) {
        
//         LinkedList<Integer> l1 = new LinkedList<>(Arrays.asList(2,4,3));
//         LinkedList<Integer> l2 = new LinkedList<>(Arrays.asList(5,6,4));
//         LinkedList<Character> l3 = new LinkedList<>();
        
//         int e = l1.size();
//         String num1 = "";
//         for (int i = 0; i < e; i++) {
//             num1 = Integer.toString(l1.pop()) + num1;
//         }

//         e = l2.size();
//         String num2 = "";
//         for (int i = 0; i < e; i++) {
//             num2 = Integer.toString(l2.pop()) + num2;
//         }
        
//         int a = Integer.parseInt(num1) + Integer.parseInt(num2);
//         String b = Integer.toString(a);

//         for (int i = 0; i < b.length(); i++) {
//             l3.push(b.charAt(i));
//         }

//         System.out.println(l3);
//     }
// }



/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        ListNode dummy = new ListNode(0);
        ListNode current = dummy;

        int carry = 0;

        while (l1 != null || l2 != null || carry != 0) {

            int x = (l1 != null) ? l1.val : 0;
            int y = (l2 != null) ? l2.val : 0;

            int sum = x + y + carry;

            int digit = sum % 10;
            carry = sum / 10;

            current.next = new ListNode(digit);
            current = current.next;

            if (l1 != null)
                l1 = l1.next;

            if (l2 != null)
                l2 = l2.next;
        }

        return dummy.next;
    }
}