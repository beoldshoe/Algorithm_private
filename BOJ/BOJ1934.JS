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
  function gcd(A, B) {
    while (A % B !== 0) {
      let r = A % B;

      if (r !== 0) {
        A = B;
        B = r;
      }
    }
    return B;
  }
  T = Number(input[0]);
  for (let i = 1; i <= T; i++) {
    let A = Number(input[i].toString().split(' ')[0]);
    let B = Number(input[i].toString().split(' ')[1]);
    let result = (A * B) / gcd(A, B);
    console.log(result);
  }
}

soultion(input);
