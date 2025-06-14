const fs = require('fs');

// 입력 파일 경로 설정 (백준 등에서 입력받을 때 '/dev/stdin' 사용)
// 로컬 테스트할 경우 'input.txt'를 사용할 수도 있음
// const readFileSyncAddress = '/dev/stdin';
// const readFileSyncAddress = 'input.txt';

// 입력을 읽어와 줄 단위로 나눈 후, 배열로 변환
const input = fs.readFileSync(0, 'utf-8').toString().trim().split('\n');

function solution(input) {
  let N = Number(input[0]);
  let costs = [];
  for (let i = 1; i <= N; i++) {
    costs.push(Number(input[i]));
  }

  costs.sort((a, b) => b - a);
  result = 0;
  for (let i = 0; i < costs.length; i++) {
    if (i % 3 !== 2) {
      result += Number(costs[i]);
    }
  }

  console.log(result);
}

solution(input);
