class Solution {
public:
    bool isAnagram(string s, string t) {

        if(s.length() != t.length()){
            return false;
        }


        unordered_map<char,int> r;
        unordered_map<char,int> h;


        for(char c : s){

        auto it = r.find(c);

        if(it != r.end()){
            it->second ++;
        }else{

            r[c]= 1;
        }

        }

        for(char c : t){

        auto it = h.find(c);

        if(it != h.end()){
            it->second ++;
        }else{

            h[c]= 1;
        }

        }


        for(char c : s){

            if( r[c] != h[c] ){
                return false;
            }
        }

        return true;

        
    }
};
