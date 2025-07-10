// 이중 포문 방법

function solution(prices) {
  var answer = [];
  for (let i = 0; i < prices.length; i++) {
    let cnt = 0;
    for (let j = i + 1; j < prices.length; j++) {
      cnt++;
      if (prices[i] > prices[j]) {
        break;
      }
    }
    answer.push(cnt);
  }
  return answer;
}

// stack 활용

function solution(prices) {
  const answer = new Array(prices.length).fill(0);
  // 결과를 저장할 배열 초기화
  const stack = [];
  // 스택 초기화

  // prices 배열을 순회하면서
  for (let i = 0; i < prices.length; i++) {
    // 스택이 비어있지 않고, 현재 가격이 스택의 top에 있는 인덱스의 가격보다 작으면 (가격이 떨어지면)
    while (stack.length && prices[i] < prices[stack[stack.length - 1]]) {
      const j = stack.pop();
      // 스택에서 인덱스를 꺼냄

      answer[j] = i - j;
      // 현재 인덱스와 스택에서 꺼낸 인덱스의 차이를 결과 배열에 저장
    }
    stack.push(i);
    // 현재 인덱스를 스택에 push
  }

  // 배열 순회가 끝난 후에도 스택에 남아있는 인덱스들 처리
  while (stack.length) {
    const j = stack.pop();
    // 스택에서 인덱스를 꺼냄
    answer[j] = prices.length - 1 - j;
    // 배열의 마지막 인덱스와 스택에서 꺼낸 인덱스의 차이를 결과 배열에 저장
  }

  return answer;
  // 결과 배열 반환
}

// 참고 블로그
// https://valur.tistory.com/entry/programmers-JavaScript-%EC%A3%BC%EC%8B%9D%EA%B0%80%EA%B2%A9-42584
