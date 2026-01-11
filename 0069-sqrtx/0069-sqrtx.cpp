class Solution {
public:
    int mySqrt(int x) {
        double sqrt = pow(x, 0.5);
        return (int)sqrt;
    }
};