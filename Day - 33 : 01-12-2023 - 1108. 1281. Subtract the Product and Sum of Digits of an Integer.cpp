// class Solution {
// public:
//     int subtractProductAndSum(int n) {
//         string sn = to_string(n);
//         int sum = 0;
//         int product = 1;
//         for (int i = 0; i < sn.length(); i++) { // Initialize i to 0
//             int temp = sn[i] - '0'; // Convert char to int
//             sum += temp;
//             product *= temp;
//         }
//         return product - sum;
//     }
// };

class Solution {
public:
    int subtractProductAndSum(int n) {
        int sum=0; int prod=1;
        while(n!=0)
        {
            int dig=n%10;
            sum+=dig;
            prod*=dig;
            n/=10;
        }
        return prod-sum;
    }
};
