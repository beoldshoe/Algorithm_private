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
  .split('\n');

// 첫 번째 줄은 명령의 개수 n, 나머지는 명령어들
const [n, ...commands] = input;

// 큐 노드를 위한 클래스
class Node {
  constructor(item) {
    this.item = item; // 저장할 값
    this.next = null; // 다음 노드를 가리킬 포인터
  }
}

// 연결리스트 기반 큐 구현
class Queue {
  constructor() {
    this.head = null; // 큐의 앞쪽
    this.tail = null; // 큐의 뒤쪽
    this.size = 0; // 큐의 크기
  }

  // 큐에 값 추가 (enqueue)
  push(item) {
    const node = new Node(item);
    if (!this.head) {
      // 큐가 비어있을 경우 head와 tail 모두 새 노드를 가리킴
      this.head = node;
      this.head.next = this.tail;
    } else {
      // 기존 tail 다음에 새 노드 연결
      this.tail.next = node;
    }
    this.tail = node; // tail 갱신
    this.size += 1; // 크기 증가
  }

  // 큐의 현재 크기 반환
  getSize() {
    return this.size;
  }

  // 큐에서 값 제거 (dequeue)
  pop() {
    if (this.size > 2) {
      const item = this.head.item;
      this.head = this.head.next;
      this.size -= 1;
      return item;
    } else if (this.size === 2) {
      const item = this.head.item;
      const newHead = this.head.next;
      this.head = newHead;
      this.tail = newHead; // tail도 같이 갱신
      this.size -= 1;
      return item;
    } else if (this.size === 1) {
      const item = this.head.item;
      this.head = null;
      this.tail = null;
      this.size -= 1;
      return item;
    } else {
      return -1; // 큐가 비어 있으면 -1 반환
    }
  }

  // 큐가 비어있는지 확인
  empty() {
    return this.size ? 0 : 1;
  }

  // 큐의 맨 앞 값 반환
  front() {
    return this.head ? this.head.item : -1;
  }

  // 큐의 맨 뒤 값 반환
  back() {
    return this.tail ? this.tail.item : -1;
  }
}

// 명령어 처리 함수
function solution(n, commands) {
  let answer = '';
  const queue = new Queue();

  for (let i = 0; i < n; i += 1) {
    const command = commands[i].split(' ')[0]; // 명령어 종류 추출

    switch (command) {
      case 'push':
        const pushItem = commands[i].split(' ')[1]; // push할 값
        queue.push(pushItem);
        break;
      case 'pop':
        answer += queue.pop() + ' ';
        break;
      case 'front':
        answer += queue.front() + ' ';
        break;
      case 'back':
        answer += queue.back() + ' ';
        break;
      case 'empty':
        answer += queue.empty() + ' ';
        break;
      case 'size':
        answer += queue.getSize() + ' ';
        break;
      default:
        break;
    }
  }

  // 문자열로 결과 출력. 공백으로 붙인 결과를 줄바꿈으로 변경
  return answer.split(' ').join('\n');
}

// 결과 출력
const answer = solution(n, commands);
console.log(answer);

// 참고 블로그
// https://junghyeonsu.tistory.com/243
