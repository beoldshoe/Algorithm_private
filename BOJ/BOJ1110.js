const fs = require('fs');

// 입력 파일 경로 설정 (백준 등에서 입력받을 때 '/dev/stdin' 사용)
// 로컬 테스트할 경우 'input.txt'를 사용할 수도 있음
const readFileSyncAddress = '/dev/stdin';
// const readFileSyncAddress = 'input.txt';

// 입력을 읽어와 줄 단위로 나눈 후, 배열로 변환
const input = fs.readFileSync(readFileSyncAddress).toString().trim();

function solution(input){
    let result = Number(input);
    let count = 0;
    while(true){

        let sum = Math.floor(result / 10) + result % 10;
        result = (result % 10) * 10 + sum % 10;
        count ++;
        if (result == Number(input)){
            break;
        }
    }
    console.log(count);
}

solution(input)