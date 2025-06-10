const fs = require('fs');
const { setPriority } = require('os');

// 입력 파일 경로 설정 (백준 등에서 입력받을 때 '/dev/stdin' 사용)
// 로컬 테스트할 경우 'input.txt'를 사용할 수도 있음
const readFileSyncAddress = '/dev/stdin';
// const readFileSyncAddress = 'input.txt';

// 입력을 읽어와 줄 단위로 나눈 후, 배열로 변환
const input = fs.readFileSync(readFileSyncAddress).toString().trim();

function solution(input){
    let i = 2;
    let n = Number(input);
    while(true){
        if (n % i === 0){
            console.log(i)
            n = n / i;
        } else {
            i++;
        }

        if (n === 1){
            break
        }
    }
}

solution(input)