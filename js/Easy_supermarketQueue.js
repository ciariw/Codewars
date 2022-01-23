//https://www.codewars.com/kata/57b06f90e298a7b53d000a86/train/python
/*
There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

input
customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
n: a positive integer, the number of checkout tills.
output
The function should return an integer, the total time required.

Important
Please look at the examples and clarifications below, to ensure you understand the task correctly :)
*/
function queueTime(customers, n) {
  // fill the cueue
  // if you cant, create cueues. if you can, return the max
  let time = 0
  if (customers.length <= n){
    return customers.length > 0  ? Math.max(...customers):0;
  }
  
  let cueCount = Math.ceil(customers.length/(n % customers.length));
  let sub2 = 0;
  let = cue = Array(n).fill(0);
  let customerID = 0;
  while (true){
    for (let i = 0; i < cue.length;i++){
      cue[cue.indexOf(Math.min(...cue))] += customers[customerID];
      customerID +=1;
      if (customerID >= customers.length){
        return Math.max(...cue)
      }
    }

  }
 
}
