import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        Map<String, Integer> map = new HashMap<>();
        
        for (int i = 0; i < players.length; i++) {
            map.put(players[i], i);
        }
        
        for (String name : callings) {
            int curIdx = map.get(name);
            int frontIdx = curIdx - 1;
            
            String frontPlayer = players[frontIdx];
            players[curIdx] = frontPlayer;
            players[frontIdx] = name;
            
            map.put(frontPlayer, curIdx);
            map.put(name, frontIdx);
        }
        
        return players;
    }
}