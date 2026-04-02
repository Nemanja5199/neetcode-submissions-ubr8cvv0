class Solution {
public:


    bool isAphaNum(char A){

        if( A >= 'a'  && A <= 'z'){
            
            return true;
        }

        else if( A >= 'A' && A <= 'Z')
        {
            return true;
        }

        else if( A >= '0' && A <= '9')
        {
            return true;
        }

        return false;

    }

    bool isPalindrome(string s) {

    int l = 0;

    int r = s.length() - 1;




    while ( l < r){


      if(!isAphaNum(s[l])){

        l++;
        continue;

      }  


      else if(!isAphaNum(s[r])){

        r--;
        continue;
      }


    cout<< s[l]<<','<<s[r];
    cout<<'|';

      if(tolower(s[l]) != tolower(s[r])){

        return false;
      }

      l++;
      r--;


    }


    return true;

        
    }
};
