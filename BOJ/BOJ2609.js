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
    // console.log(input)
    input.sort((a,b)=>a-b)
    function gcd(a, b){
        while(a % b !== 0){
            let r = a % b

            if (r !==0){
                a = b;
                b = r;
            }
        }
        return b
    }
    let a = input[0]
    let b = input[1]
    // console.log(a, b)
    console.log(gcd(a,b))
    console.log(a*b/gcd(a,b))
}

solution(input)