function solution(nums) {
  function isprime(number) {
    for (let i = 2; i <= Number(Math.sqrt(number)); i++) {
      if (number % i === 0) {
        return false;
      }
    }
    return true;
  }

  var l = nums.length;
  var number = 0;
  var cnt = 0;

  for (let i = 0; i <= l - 3; i++) {
    for (let j = i + 1; j <= l - 2; j++) {
      for (let k = j + 1; k < l; k++) {
        number = nums[i] + nums[j] + nums[k];
        if (isprime(number) === true) {
          cnt += 1;
        }
      }
    }
  }
  return cnt;

  return answer;
}
