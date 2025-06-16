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
    let N = BigInt(input[0])
    let l = input[1]

    let current_B = 'R'
    let current_R = 'B'
    let count_B = Number(1)
    let count_R = Number(1)

    for (let i = 0; i < l.length; i++){
        if (current_B !== l[i]){
            if (l[i] === 'B'){
                count_B++
            }
        }
        current_B = l[i]
    }

        for (let i = 0; i < l.length; i++){
        if (current_R !== l[i]){
            if (l[i] === 'R'){
                count_R++
            }
        }
        current_R = l[i]
    }
    if (count_B < count_R){
        console.log(count_B)
    } else{
        console.log(count_R)
    }
}

solution(input)