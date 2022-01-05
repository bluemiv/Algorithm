// 배열의 합을 구하는 메소드
const sum = (nums) => nums.length === 0 ? 0 : nums.reduce((_, cur) => _ += cur)

function findSubarrMaxSum(arr){
  let maxSum = 0;
  let maxSubArrs = [];
  
  // subArr의 길이 (몇개를 뽑을지)
  // subArr의 길이를 내림차순으로 정렬하기 위해, 역순으로 루프 
  let pickCount = arr.length
  while(pickCount >= 0) {
    
    for(let startIdx = 0; startIdx<=arr.length-pickCount; startIdx++) {
      const endIdx = startIdx + pickCount;
      const subArr = arr.slice(startIdx, endIdx)
      const subArrSum = sum(subArr)
      
      // 양 끝에 0이 있는 경우는 볼 필요도 없으므로 다음으로 넘어감
      if(subArrSum[0] === 0 || subArrSum[subArr.length-1] === 0) {
        continue
      }
      
      // 합이 0인 경우도 볼필요없기 때문에, 0이 아닌 경우에만 최댓값을 구함
      if(subArrSum !== 0) {
        if(maxSum < subArrSum) {
          maxSum = subArrSum
          maxSubArrs = [subArr] 
        } else if(maxSum === subArrSum) {
          maxSubArrs.push(subArr)
        } 
      }
    }
    
    pickCount -= 1
  }
  
  maxSubArrs = maxSubArrs.length === 1 ? maxSubArrs[0] : maxSubArrs
  const result = [maxSubArrs, maxSum]
  return result
}
