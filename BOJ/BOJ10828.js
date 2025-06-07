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

// 첫 번째 줄은 명령의 개수 n, 나머지는 명령어들
const [n, ...commands] = input;

function solution(n, commands) {
  const stack = [];
  const result = [];

  for (let i = 0; i < n; i += 1) {
    const command = commands[i].split(' ')[0];
    switch (command) {
      case 'pop':
        if (stack.length === 0) {
          result.push(-1);
        } else {
          result.push(stack.pop());
        }
        break;
      case 'size':
        result.push(stack.length);
        break;
      case 'empty':
        if (stack.length === 0) {
          result.push(1);
        } else {
          result.push(0);
        }
        break;
      case 'top':
        if (stack.length === 0) {
          result.push(-1);
        } else {
          result.push(stack[stack.length - 1]);
        }
        break;
      default:
        stack.push(commands[i].split(' ')[1]);
        break;
    }
  }
  return result.join('\n');
}
const result = solution(n, commands);
console.log(result);

// 참고 블로그
// https://gurtn.tistory.com/67
