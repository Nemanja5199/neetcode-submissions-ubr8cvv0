class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size()) return false;

        vector<int> count(26);

        for(char& c : s1){
            count[c - 'a']++;
        }

        int l = 0, r = 0;  

        int matchedValues = s1.size();

        for(int i = 0; i < s2.size(); i++){  
            if(count[s2[i] - 'a'] > 0){
                l = i;
                r = i;
                while(r - l + 1 <= s1.size()){
                    if(count[s2[r] - 'a'] > 0){
                        count[s2[r] - 'a']--;
                        matchedValues--;
                        r++;
                    } else{
                        while(l != r){
                            count[s2[l] - 'a']++;
                            l++;  
                        }
                        matchedValues = s1.size();
                        break;
                    }
                }

                if(!matchedValues) return true;  
            }
        }

        return false;
    }
};