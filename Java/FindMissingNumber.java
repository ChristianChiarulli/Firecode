package Java;

import java.utils.Arrays;

class FindMissingNumber{

public static int findMissingNumber(int[] arr) {
    
    Arrays.sort(arr);
    
    for (int i = 0; i < arr.length-1; i++){
        
        if (arr[i] + 1 != arr[i+1]){
            return (arr[i]+1);
        }
    }
    return -1;
}
}
