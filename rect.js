// function selfDeviding(left, right) {
//   let num = [];
//   for(let i = 1; i<=right;i++){
//     let spilited = i.toString().split();
//     for(let j = 1; j < spilited.length;j++){
//       if(i%Number(spilited[j])===0){
//         num.push(spilited[i]);
//       }
//     }
//   }
//   console.log(num);
// }
// selfDeviding(1,22);

function binarySearch(nums,target){
  let left = 0, right = nums.length - 1, middle = left + right/2;

  let num = 0;
  for (let i = 0; i <nums.length; i++) {
    
    if(target === middle){
      num == i;
    }
    else if(target>middle){
      left == middle +1;
    }
    else{
      right == middle-1;
    }
  }
  console.log(num);
}
binarySearch([1,2,3,4,5,6,7],4);