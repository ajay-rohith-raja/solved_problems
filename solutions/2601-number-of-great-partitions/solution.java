class Solution {
    public int countPartitions(int[] nums, int k) {
        long totalSum = 0;
        for (int num : nums) totalSum += num;
        
        
        if (totalSum < 2 * k) return 0;
        
        int n = nums.length;
        long MOD = 1_000_000_007;
        
        
        long[] dp = new long[k];
        dp[0] = 1;
        
        
        for (int num : nums) {
            for (int j = k - 1; j >= num; j--) {
                dp[j] = (dp[j] + dp[j - num]) % MOD;
            }
        }
        

        long invalidSubsetsCount = 0;
        for (int j = 0; j < k; j++) {
            invalidSubsetsCount = (invalidSubsetsCount + dp[j]) % MOD;
        }
        
        
        long totalPartitions = 1;
        for (int i = 0; i < n; i++) {
            totalPartitions = (totalPartitions * 2) % MOD;
        }
        
        
        long result = (totalPartitions - 2 * invalidSubsetsCount + MOD) % MOD;
        
        return (int) result;
    }
}
