function solution(participant, completion) {
  const Marathon = new Map();

  for (const person of participant) {
    Marathon.has(person)
      ? Marathon.set(person, Marathon.get(person) + 1)
      : Marathon.set(person, 1);
  }

  for (const person of completion) {
    Marathon.set(person, Marathon.get(person) - 1);
  }

  for (const [key, value] of Marathon) {
    if (value === 1) {
      return key;
    }
  }
}

// 참고 블로그
// https://velog.io/@skdbsqls/JavaScript-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%99%84%EC%A3%BC%ED%95%98%EC%A7%80-%EB%AA%BB%ED%95%9C-%EC%84%A0%EC%88%98
