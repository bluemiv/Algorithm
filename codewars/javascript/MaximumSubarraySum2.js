// https://www.codewars.com/kata/56e3cbb5a28956899400073f

const sum = (nums) => nums.length === 0 ? 0 : nums.reduce((_, cur) => _ += cur)

function findSubarrMaxSum(arr){
  let maxSum = 0;
  let maxSubArrs = [];
  
  let pickCount = 0
  while(pickCount <= arr.length) {
    
    for(let startIdx = 0; startIdx<=arr.length-pickCount; startIdx++) {
      const endIdx = startIdx + pickCount;
      const subArr = arr.slice(startIdx, endIdx)
      const subArrSum = sum(subArr)
      
      if(subArrSum !== 0) {
        if(maxSum < subArrSum) {
          maxSum = subArrSum
          maxSubArrs = [subArr] 
        } else if(maxSum === subArrSum) {
          maxSubArrs.push(subArr)
        } 
      }
    }
    
    pickCount += 1
  }
  
  maxSubArrs = maxSubArrs.length === 1 ? maxSubArrs[0] : maxSubArrs
  const result = [maxSubArrs, maxSum]
  return result
}
