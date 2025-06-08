const fs = require('fs');

// 입력 파일 경로 설정 (백준 등에서 입력받을 때 '/dev/stdin' 사용)
// 로컬 테스트할 경우 'input.txt'를 사용할 수도 있음
const readFileSyncAddress = '/dev/stdin';
// const readFileSyncAddress = 'input.txt';

// 입력을 읽어와 줄 단위로 나눈 후, 배열로 변환
const input = fs.readFileSync(readFileSyncAddress).toString().split(' ');

function solution(input) {
  const num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  const N = input[0];
  const B = Number(input[1]);
  let l = N.length;
  let result = 0;

  for (let i = 0; i < l; i++) {
    for (let j = 0; j < num.length; j++) {
      if (N[i] === num[j]) {
        result += B ** (l - i - 1) * j;
        break;
      }
    }
  }
  return result;
}

result = solution(input);

console.log(result);
