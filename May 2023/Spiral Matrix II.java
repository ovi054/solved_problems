class Solution {
    public int[][] generateMatrix(int n) {
        int[][] arr = new int[n][n];
        int left = 0, right =n-1, top =0, bottom = n-1;
        int i = 1;
         while(i<=n*n)
        {
            for(int j= left;j<=right;j++)
            {
                arr[top][j] = i;
                // System.out.println(i);
                i++;
            }
            top++;
            for(int j= top;j<=bottom;j++)
            {
                arr[j][right] = i;
                // System.out.println(i);
                i++;
            }
            right--;
            if(top<=bottom){
            for(int j= right;j>=left;j--)
            {
                arr[bottom][j] = i;
                // System.out.println(i);
                i++;
            }
            bottom--;}
            if(left<=right){
            for(int j= bottom;j>=top;j--)
            {
                arr[j][left] = i;
                // System.out.println(i);
                i++;
            }
            left++;}
        }
        return arr;
    }
}