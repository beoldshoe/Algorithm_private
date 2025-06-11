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

    function gcd(a, b){
        while(a % b !==0){
            let r = a % b

            if (r !== 0){
                a = b
                b = r
            }
        }
        return b
    }

    let n = Number(input[0])
    for (let i = 1; i<=n; i++){
        input.sort((a,b)=>a-b)
        let a = Number(input[i].split(' ')[0])
        let b = Number(input[i].split(' ')[1])
        let g = gcd(a,b)
        console.log(a * b / g)
    }
}

solution(input)