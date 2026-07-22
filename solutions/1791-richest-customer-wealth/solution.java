class Solution {
    public int maximumWealth(int[][] accounts) {
        int n=accounts.length;
        int m = accounts[0].length;
        int amt=0;
        int res=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                res = res + accounts[i][j];
            }
            if(res>amt){
                amt=res;
            }
            res=0;
        }
        return amt;
    }
}
