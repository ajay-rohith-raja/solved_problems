class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int n1len = nums1.length;
        int n2len = nums2.length;
        int[] ans = new int[n1len]; 

        for(int i = 0; i < n1len; i++){
            int a = -1; 
            for(int j = 0; j < n2len; j++){
                
                if(nums1[i] == nums2[j]){
                    
                    for(int z = j + 1; z < n2len; z++){
                        if(nums2[z] > nums1[i]){
                            a = nums2[z];
                            break; 
                        }
                    }
                    break;
                }
            }
            ans[i] = a;
        }
        return ans;
    }
}
