class Solution {
    public int solution(int[] num_list) {
        int answer1 = num_list[0];
        int total = 0;
        
        for (int i = 1; i < num_list.length; i++) {
            answer1 = answer1 * num_list[i];
        }
        
        for (int num : num_list) {
            total += num;
        }
        
        return answer1 < total * total ? 1 : 0; 
    }
}