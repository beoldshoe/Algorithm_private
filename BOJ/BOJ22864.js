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
  .split(" ")
  .map(Number);


function solution(input){
    let result = 0;
    let firodo = 0;

    for (let i = 0; i<24; i++){
        if (firodo + input[0] > input[3]){
            firodo -= input[2]
            if (firodo < 0){
                firodo = 0
            }
        } else{
            result += input[1]
            firodo += input[0]
        }
    }
    return result
}

result = solution(input)
console.log(result)