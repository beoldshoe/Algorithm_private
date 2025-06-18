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
  let N = Number(input[0]);
  let M = Number(input[2]);
  let crain = input[1].toString().trim().split(' ').map(Number);
  let box = input[3].toString().trim().split(' ').map(Number);

  crain.sort((a, b) => b - a);
  box.sort((a, b) => b - a);
  let cnt = 0;
  if (box[0] > crain[0]) {
    cnt = -1;
  } else {
    while (box.length !== 0) {
      for (let i = 0; i < crain.length; i++) {
        if (box.length && crain[i] < box[-1]) {
          continue;
        }
        for (let j = 0; j < box.length; j++) {
          if (crain[i] >= box[j]) {
            box.splice(j, 1);
            break;
          }
        }
      }
      cnt += 1;
    }
  }
  console.log(cnt);
}

solution(input);

// 참고 블로그
// https://my-first-programming.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EB%B0%B0-1092-javascript
// https://codinghejow.tistory.com/249
