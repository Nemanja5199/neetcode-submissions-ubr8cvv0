class Solution {
public:
    int characterReplacement(string s, int k) {


        unordered_map<char,int> charMap;


        int l = 0;
        int r = 0;

        int maxf = 0;
        int res = 0 ;
        while(r< s.size()){

        if(charMap.find(s[r]) == charMap.end()){

             charMap[s[r]] = 1;
        } else{
            charMap[s[r]]++;
        }

        maxf = max(maxf,charMap[s[r]]);

        if((r - l + 1) - maxf <= k){

            res = max(res,r - l + 1);
          
        } else{
            
            charMap[s[l]]--;
            l++;

        }

          r++;

        
        }


        return res;
    }
    
};
