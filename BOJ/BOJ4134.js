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

function soultion(input) {
  function isPrime(num) {
    let n = Math.sqrt(num);

    for (let i = 2; i <= n; i++) {
      if (num % i === 0) {
        return false;
      }
    }
    return true;
  }

  T = input[0];
  for (let i = 1; i <= T; i++) {
    n = Number(input[i]);
    while (true) {
      if (n === 0 || n === 1) {
        console.log(2);
        break;
      }
      if (isPrime(n)) {
        console.log(n);
        break;
      } else {
        n += Number(1);
      }
    }
  }
}

soultion(input);
