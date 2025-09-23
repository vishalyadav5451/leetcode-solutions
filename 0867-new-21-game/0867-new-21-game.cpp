class Solution {
public:
    double new21Game(int n, int k, int maxPts) {
        vector<double> P(n+1,0.0);

        P[0] = 1;

        double currProbavSum = (k == 0) ? 0 : 1;

        for(int i = 1; i <= n; i++) {

            P[i] = currProbavSum/maxPts;

            if(i < k) 
                currProbavSum += P[i];

            if (i - maxPts >= 0 && i-maxPts <k) 
                    currProbavSum -= P[i-maxPts];
        }

        return accumulate(begin(P) + k, end(P), 0.0);
    }
};