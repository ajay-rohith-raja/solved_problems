class Solution {
    public boolean threeConsecutiveOdds(int[] arr) {
        int c=0;
        for(int i:arr){
            if(i%2!=0){
                c=c+1;
                if(c==3){
                    return true;
                }
            }
            else{
                c=0;
            }
        }
        return false;
    }
}
