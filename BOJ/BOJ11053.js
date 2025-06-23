const fs = require('fs');
const { inflate } = require('zlib');

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
    let N = Number(input[0])
    let A = input[1].toString().trim().split(" ").map(Number)
    let dp =[]
    for (let i = 0; i<N; i++){
        dp.push(Number(1))
    }
    for (let i = 0; i<N; i++){
        for(let j=0; j<i; j++){
            if (A[j]<A[i]){
                dp[i] = Math.max(dp[i], dp[j] + 1)
            }
            
        }
    }
    console.log(Math.max(...dp))
}

solution(input)