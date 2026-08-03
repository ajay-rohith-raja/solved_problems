class Solution {
    public boolean canAliceWin(int[] nums) {
        int i=0;
        int sum=0;
        int sum2=0;
        while(i<nums.length){
            if(nums[i]<=9){
                sum = sum + nums[i];
                i++;
            }
            else{
                sum2 = sum2 + nums[i];
                i++;
            }
        }
        if(sum > sum2 || sum2 > sum){
            return true;
        }
        else{
            return false;
        }
    }
}
