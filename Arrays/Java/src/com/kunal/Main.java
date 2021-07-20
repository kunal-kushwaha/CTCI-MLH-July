package com.kunal;

import java.util.HashMap;
import java.util.Map;

public class Main {

    public static void main(String[] args) {

    }
    public int longestCharReplace(String s, int k) {
        int start = 0;
        int maxLen = 0; // max repeating characters in the box
        int max = 0; // this is the answer

        Map<Character, Integer> map = new HashMap<>();

        for (int end = 0; end < s.length(); end++) {
            char ch = s.charAt(end);

            map.put(ch, map.getOrDefault(ch, 0) + 1);

            // max length of the repeating character in the box
            maxLen = Math.max(maxLen, map.get(ch));

            // condition violation
            // size of the box - maxLen = characters I need to flip
            // if this is > k, means condition violated
            if (end-start+1 - maxLen > k) {
                // slide my window
                char first = s.charAt(start);
                map.put(first, map.get(first) - 1);
                start++;
            }
            max = Math.max(max, end-start+1);
        }
        return max;
    }
}
