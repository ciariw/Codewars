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
