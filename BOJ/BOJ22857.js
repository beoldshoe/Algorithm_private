const fs = require('fs');

// 입력 파일 경로 설정 (백준 등에서 입력받을 때 '/dev/stdin' 사용)
// 로컬 테스트할 경우 'input.txt'를 사용할 수도 있음
const readFileSyncAddress = '/dev/stdin';
// const readFileSyncAddress = 'input.txt';

// 입력을 읽어와 줄 단위로 나눈 후, 배열로 변환
const input = fs.readFileSync(readFileSyncAddress).toString().trim().split("\n");

function solution(input){
    const [n, k] = input[0].split(' ').map(Number);
    const arr = input[1].split(' ').map(Number);

    const dp = Array.from({ length: n + 1 }, () => Array(k + 1).fill(0));

    for (let i = 1; i <= n; i++) {
        for (let j = 0; j <= k; j++) {
            if (arr[i - 1] % 2 === 1) { // 홀수인 경우
                if (j > 0) {
                    dp[i][j] = dp[i - 1][j - 1];
                }
            } else { // 짝수인 경우
                dp[i][j] = dp[i - 1][j] + 1;
            }
        }
    }

    // 최대 길이 계산
    let maxLength = 0;
    for (let i = 0; i <= n; i++) {
        for (let j = 0; j <= k; j++) {
            maxLength = Math.max(maxLength, dp[i][j]);
        }
    }

    console.log(maxLength);
}

solution(input)

