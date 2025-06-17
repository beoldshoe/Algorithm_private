const fs = require('fs');
const { setPriority } = require('os');

// 입력 파일 경로 설정 (백준 등에서 입력받을 때 '/dev/stdin' 사용)
// 로컬 테스트할 경우 'input.txt'를 사용할 수도 있음
const readFileSyncAddress = '/dev/stdin';
// const readFileSyncAddress = 'input.txt';

// 입력을 읽어와 줄 단위로 나눈 후, 배열로 변환
const input = fs.readFileSync(readFileSyncAddress).toString().trim();

function solution(input){
    let l = input
    function maximum(l) {
        let result = ''
        let m_count = Number(0)

        for (let i = 0; i<l.length; i++){
            if (l[i] === 'M'){
                m_count++
            } else {
                if (m_count !==0){
                    result += '5'
                    for (let i = 0; i<m_count; i++){
                        result += '0'
                    }
                    m_count = 0
                } else{
                    result += '5'
                }
            }
        }
        if (m_count !== 0){
            for (let i =0; i<m_count; i++){
                result += '1'
            }
        }
        console.log(result)
    }
    maximum(l)

    function minimum(l){
        let result = ''
        let m_count = Number(0)

        for (let i = 0; i<l.length; i++){
            if (l[i] === 'M'){
                m_count++
            } else{
                if (m_count !== 0){
                    result += '1'
                    for (let i =0; i<m_count-1; i++){
                        result += '0'
                    }
                    m_count = 0
                }
                result += '5'
            }
        }
        if (m_count !== 0){
            result += '1'
            for (let i =0; i<m_count-1; i++){
                result += '0'
            }
        }
        console.log(result)
    }
    minimum(l)
}

solution(input)