class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int [] newArray = new int[nums1.length + nums2.length];
        for (int i = 0; i<nums1.length; i++){
            newArray[i] = nums1[i];
        }
        for (int i = nums1.length; i<nums2.length+nums1.length; i++){
            newArray[i] = nums2[i-nums1.length];
        }
        Arrays.sort(newArray);
        int pos = newArray.length/2;
        if (newArray.length%2==0)
            return (newArray[pos] + newArray[pos-1])/2f;
        return newArray[pos];
        
    }
}