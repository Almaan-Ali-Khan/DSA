class Solution {
public:
    int numberOfSteps(int num) {
        int i = 0;
        while (num > 0){
            if (num%2 == 0){
                i++;
                num /= 2;
            }
            if (num%2 == 1){
                i++;
                num -= 1;
            }
        }
        return i;
    }
};