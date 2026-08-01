import java.util.*;
class Solution {
    public int calPoints(String[] operations) {
        int n = operations.length;
        int[] stack = new int[n];
        int top= -1;
        for(int i=0;i<n;i++){
            if(operations[i].equals("C")){
                top = top-1;
            }
            else if(operations[i].equals("D") ){
                int db = stack[top] * 2;
                stack[++top] = db;
            }
            else if(operations[i].equals("+")){
                int pl = stack[top] + stack[top-1];
                stack[++top] = pl;
            }
            else{
                stack[++top] = Integer.parseInt(operations[i]);
            }
        }
        int sum=0;
        for(int x=0;x<=top;x++){
            sum = sum + stack[x];
        }
        return sum;
    }
}
