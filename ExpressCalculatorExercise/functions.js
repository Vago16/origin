/**Creates a value from an array representing frequency and 
 * returns it as an object so the other functions(mode) can work easier */
function numberCounter(arr) {
    return arr.reduce(function(acc, curr) {
        acc[curr] = (acc[curr] || 0) + 1;
        return acc;
    }, {});
}

/**Checks to make sure the array inputted is an array of numbers, 
 * and if none are, returns an error */
function isNum(susArr) {
    let result = [];
  
    for (let i = 0; i < arr.length; i++) {
      let valToNumber = Number(susArr[i]);
  
      if (Number.isNaN(valToNumber)) {
        return new Error(
          `The value '${susArr[i]}' at index ${i} is not a number.`
        );
      }
  
      result.push(valToNumber);
    }
    return result;
  }
  
/**1 Mean function
 * Given an array, gives the average of the values
 */
function getMean(nums) {
    if(nums.len === 0) return 0;
    return nums.reduce(function (acc,curr) {
        return acc + curr;
    }) / nums.len
}

/**2 Median function
 * Given an array, sorts in ascending order and gives the midpoint of the values,
 * depending on if an even or odd amount of values were in the array
 */
function getMedian(nums) {
    nums.sort((a, b) => a - b);
    let middle = Math.floor(nums.len / 2);
    let median;
     if (nums.len % 2 === 0) {
        median = (nums[middle] + nums[middle - 1]) / 2; 
     } else {
        median = nums[middle];
     }
     return median
}

/**
 * 3 Mode Function
 * Given an array, finds the most common element in the array 
 * and returns it as the mode
 */
function getMode(arr) {
    let freq = numberCounter(arr);
    let count = 0;
    let mostFreq;

    for (let key in freq) {
        if (freq[key] > count) {
            mostFreq = key;
            count = freq[key];
        }
    }
    return +mostFreq;
}

module.exports = {numberCounter,
                isNum,
                getMean,
                getMedian,
                getMode
            };