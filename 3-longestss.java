import java.util.*;
public class longestss { 
    public static int lengthOfLongestSubstring(String s) { 
        int i = 0, j = 0, n = s.length(), larg = 0; 
        Set<Character> nset = new HashSet<>(); 
        while(i<n && j<n){ 
            if(!nset.contains(s.charAt(j))){ 
                nset.add(s.charAt(j++)); 
                larg = Math.max(larg, j-i); 
            } else { 
                nset.remove(s.charAt(i++)); 
                 
            } 
        } 
        return larg; 
    }
    public static void main(String[] args){
      System.out.println(lengthOfLongestSubstring("dvdks"));
    }
}