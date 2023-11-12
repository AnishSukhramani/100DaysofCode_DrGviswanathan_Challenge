class Solution {
 public:
  string addBinary(string a, string b) {
    string ans;
    int carry = 0;
    int i = a.length() - 1;
    int j = b.length() - 1;

    while (i >= 0 || j >= 0 || carry) {
      if (i >= 0)
        carry += a[i--] - '0';
      if (j >= 0)
        carry += b[j--] - '0';
      ans += carry % 2 + '0';
      carry /= 2;
    }

    reverse(begin(ans), end(ans));
    return ans;
  }
};
// This C++ code defines a class `Solution` with a public member function `addBinary` that takes two binary strings `a` and `b` as input and returns their sum as a binary string. The function uses a simple binary addition algorithm with a carry variable. It iterates through the input strings from right to left, adding corresponding bits along with the carry. The result is constructed in the `ans` string, which is then reversed before being returned. The loop continues until both input strings are processed, and any remaining carry is handled.
