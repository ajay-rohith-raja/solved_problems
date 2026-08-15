class Solution {
    public int[] concatWithReverse(int[] nums) {
        int n = nums.length;
        int[] rev = new int[n];
        int[] ans = new int[n*2];

        int idx=0;
        for(int i=n-1;i>=0;i--){
            rev[idx] = nums[i];
            idx++;
        }
        int j=0;
        for(int i=0;i<n*2;i++){
            if(i<n){
                ans[i] = nums[i];
            }
            else{
                ans[i] = rev[j];
                j++;
            } 
        }
        return ans;
    }
}
