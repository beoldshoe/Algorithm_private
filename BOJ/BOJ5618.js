const fs = require('fs');

// 입력 파일 경로 설정 (백준 등에서 입력받을 때 '/dev/stdin' 사용)
// 로컬 테스트할 경우 'input.txt'를 사용할 수도 있음
// const readFileSyncAddress = '/dev/stdin';
const readFileSyncAddress = 'input.txt';

// 입력을 읽어와 줄 단위로 나눈 후, 배열로 변환
const input = fs.readFileSync(readFileSyncAddress).toString().trim().split("\n");

function solution(input){
    const n = parseInt(input.shift(), 10);
    const data = input.toString().split(' ').map(Number);
    data.sort((a,b) => a-b);

    for (let i = 1; i <= data[0]; i++){
        let check = 0
        for (let j = 0; j < n; j++){
            if (data[j] % i === 0){
                continue;
            } else{
                check = 1
                break
            }
        }
        if (check === 0){
           console.log(i);
        }

    }
}

solution(input)