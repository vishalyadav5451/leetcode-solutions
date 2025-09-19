class Solution {
public:
    
    int sum = 0;
    int CountOfDigit( int num ) {
        int count = 0;
        sum = 0;
        while ( num != 0) {
            //num=38
            sum += num%10; //8
            num /= 10;
            count++;
        }

        return count ;
    }

    int addDigits(int num) {
        
        while(CountOfDigit(num) > 1 ) {

            num = sum;
        }

        return sum;
    }
};