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
  .split("\n");

function solution(input){
    let N = input[0]
    let l = input[1].toString().trim().split(' ').map(Number)
    l.sort((a,b)=> a-b)
    let result = l[N-1]
    for (let i = 0; i<N-1; i++){
        result += Number(l[i])/2
    }
    console.log(result)
}

solution(input)