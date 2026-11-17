class Solution {
  public:
    int factorial(int n) {
        // code here
        int t = n;
        if (n==0){
            return 1;
        }
        while (n > 2){
            n -= 1;
            t *= (n);
        }
    return t;
    }
};