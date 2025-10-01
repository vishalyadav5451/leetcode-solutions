class Solution {
public:
    string convertToTitle(int columnNumber) {
        string result;

        while(columnNumber > 0) {

            columnNumber--;

            int remain = columnNumber % 26 ; 
            columnNumber = columnNumber/26 ;
            char ch = remain + 'A' ;
            result.push_back(ch);
        }

        reverse(begin(result),end(result));
        return result ;
    }
};