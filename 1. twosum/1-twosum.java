public class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> nmap = new HashMap<>();
        for(int i=0;i < nums.length;i++){
            nmap.put(nums[i], i);
        }
        for(int i=0;i<nums.length; i++){
            int complement = target - nums[i];
            if(nmap.containsKey(complement) && nmap.get(complement)!=i){
                return(new int[] {i, nmap.get(complement)});
            }
        }
        throw new IllegalArgumentException("No two sum solution");
    }
    
}
