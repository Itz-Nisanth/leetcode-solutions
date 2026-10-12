// 344. Reverse String

// Write a function that reverses a string. The input string is given as an array of characters s.
// You must do this by modifying the input array in-place with O(1) extra memory.

// Example 1:
// Input: s = ["h","e","l","l","o"]
// Output: ["o","l","l","e","h"]

// Example 2:
// Input: s = ["H","a","n","n","a","h"]
// Output: ["h","a","n","n","a","H"]

class Solution {
    public void reverseString(char[] s) {
        int l = 0;
        int r = s.length-1;

        while(l < r) {
            Character temp = s[l];
            s[l] = s[r];
            s[r] = temp;

            l++;
            r--;
        }  
    }
}

//Output:
//Input: s = ["h","e","l","l","o"]
//Output: ["o","l","l","e","h"]
//Input: s = ["H","a","n","n","a","h"]
//Output: ["h","a","n","n","a","H"]