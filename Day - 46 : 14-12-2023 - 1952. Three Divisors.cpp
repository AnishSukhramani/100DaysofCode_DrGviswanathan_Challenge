class Solution {
public:
    bool isThree(int n) {
        int count = 0;
        for (int i = 1; i <= n; i++) { 
            if (n % i == 0) {
                count += 1;
            }
        }
        
        return count == 3; // Return true if count is equal to 3, otherwise return false
    }
};
