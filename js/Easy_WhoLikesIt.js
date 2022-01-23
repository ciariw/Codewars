// https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python
/*
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. 
We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:
*/
function likes(names) {
  let leng = names.length;
  let soln;
  let lis;
  if (leng == 0) { 
    return "no one likes this";
  }else if (leng == 1){
    return names[0] + " likes this";
  }else if (leng == 2){
    return names[0] + " and " + names[1] + " like this";
  }else if (leng == 3){
    return names[0] + ", " + names[1] + " and " + names[2] + " like this";
  }else if (leng > 3){
    return names[0] + ", " + names[1] + " and " + (leng - 2) + " others like this";
  }
  
  
}
