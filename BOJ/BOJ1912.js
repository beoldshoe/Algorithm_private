const fs = require('fs');

// 입력 파일 경로 설정 (백준 등에서 입력받을 때 '/dev/stdin' 사용)
// 로컬 테스트할 경우 'input.txt'를 사용할 수도 있음
const readFileSyncAddress = '/dev/stdin';
// const readFileSyncAddress = 'input.txt';

// 입력을 읽어와 줄 단위로 나눈 후, 배열로 변환
const input = fs
  .readFileSync(readFileSyncAddress)
  .toString()
  .trim()
  .split('\n');

function solution(input) {
  let n = Number(input[0]);
  let number = input[1].toString().trim().split(' ').map(Number);
  let dp = [];
  for (let i = 0; i < n; i++) {
    dp.push(0);
  }
  dp[0] = number[0];
  let result = -10000000;
  for (let i = 1; i < n; i++) {
    dp[i] = Math.max(number[i], number[i] + dp[i - 1]);
    result = Math.max(result, dp[i]);
  }

  console.log(Math.max(...dp));
}

solution(input);
