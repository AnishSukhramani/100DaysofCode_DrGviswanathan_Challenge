class Solution {
public:
    bool isPalindrome(int x) {
        string s = to_string(x);
        string t = s;
        reverse(t.begin(),t.end());
        return s==t;
    }
};


// This C++ class, `Solution`, contains a method `isPalindrome` that checks whether an integer `x` is a palindrome. 
// 1. It first converts the integer `x` to a string `s` using `to_string(x)`.
// 2. Then, it creates a copy of the string `s` and reverses it to get the string `t`.
// 3. Finally, it compares the original string `s` with the reversed string `t` and returns `true` if they are the same (i.e., the integer is a palindrome) and `false` otherwise.
