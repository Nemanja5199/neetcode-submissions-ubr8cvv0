class Solution {
public:
    bool checkInclusion(string s1, string s2) {

         if (s1.length() > s2.length()) {
            return false;
        }


        vector<int> s1Char (26,0);
        vector<int> s2Char (26,0);

        for(char& c : s1){
            s1Char[c - 'a']++;
        }
        
         for(int i = 0; i < s1.size(); i++) {
            s2Char[s2[i] - 'a']++;
        }
         int match = 0;
         for(int i = 0 ; i < 26 ; i++){
            if(s1Char[i] == s2Char[i]) match++;
         }


        int l = 0;
        int r = s1.size();

        while(r < s2.length()){

            if(match == 26){
                return true;
            }

            int index = s2[r] - 'a';

            if(s2Char[index] == s1Char[index]) match--;
            s2Char[index]++;
            if(s2Char[index] == s1Char[index]) match ++;
           index = s2[l] - 'a';
           if(s2Char[index] == s1Char[index]) match--;
           s2Char[index]--;
           if(s2Char[index] == s1Char[index]) match ++;

           l++;
           r++;


        
        }


        return match == 26;

        
    }
};
