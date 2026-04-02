class Solution {
public:
    bool isAnagram(string s, string t) {

        if(s.length() != t.length()){
            return false;
        }


        unordered_map<char,int> r;
        unordered_map<char,int> h;


        for (int i=0 ; i<s.length() ; i++){
            r[s[i]]++;
            h[t[i]]++;
        }

        return r == h ;

       

        
    }
};
