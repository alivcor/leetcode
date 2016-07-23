public class sortMedian {
  public static void main(String[] args){
    int[] n1 = {1, 2, 4, 7, 26, 77};
    int[] n2 = {3,66,88,100};
    // 1, 2, 3, 4, 7, 26, 66, 77, 88, 100
    //3, 66, 77, 88 , 100
    double n3 = findMedianSortedArrays(n1, n2);
    System.out.println(n3);
  }
  public static double findMedianSortedArrays(int[] nums1, int[] nums2) { 
      int n1 = nums1.length;
        int n2 = nums2.length;
        int i=0, j=0, k=0, s=0;
        float[] res = new float[n1+n2];
        double mid = Math.floor((n1+n2)/2)+1;
        float med=0;
        while(i<n1 && j<n2 && s<=mid){
            if(nums1[i]<=nums2[j]){
                res[k++]=nums1[i++];
            } else {
                res[k++]=nums2[j++];
            }
            s = i+j;
        }
        if(s<=mid){
            while(i<n1){
                res[k++]=nums1[i++];
            }
            while(j<n2){
                res[k++]=nums2[j++];
            }
        }
        /*for(int y=0;y<res.length;y++){
            System.out.print(res[y]+", ");
        }*/
        System.out.println("");
        if((n1+n2)%2==0){
            med = (res[((n1+n2)/2)-1]+res[(n1+n2)/2])/2;
            //System.out.println("even, "+ );
        } else {
            med = res[(n1+n2)/2];
            //System.out.println("odd, "+ ]);
        }
       return med;
      
  } 
}
