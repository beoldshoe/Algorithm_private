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
  .split("\n")
  .map(Number);

function solution(input){
    N = input[0]
    let tips = []
    for (let i = 1; i<=N; i++){
        tip = input[i]
        tips.push(Number(tip))
    }
    tips.sort((a,b)=> b-a)
    let result = 0
    for (let i = 0; i<tips.length; i++){
        r = tips[i] - (i+1 - 1)
        if ( r < 0){
            r = 0
        }
        result += Number(r)
    }
    console.log(result)
}

solution(input)