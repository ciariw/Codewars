//https://www.codewars.com/kata/5526fc09a1bbd946250002dc
/*
You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. 
Write a method that takes the array as an argument and returns this "outlier" N.
*/
function findOutlier(integers){

  for (i = 1; i < integers.length-1; i++){
      if (Math.abs(integers[i]%2) != Math.abs(integers[i-1]%2)){
        if (Math.abs(integers[i+1]%2) == Math.abs(integers[i-1]%2)){
          return integers[i];
        }else{
          return integers[i-1];
        }
      } else if (Math.abs(integers[i+1]%2) != Math.abs(integers[i-1]%2)){return integers[i+1]}
    }
}
