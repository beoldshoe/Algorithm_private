/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  const stack = [];
  for (let i = 0; i < s.length; i++) {
    if (s[i] === '(' || s[i] == '[' || s[i] == '{') {
      stack.push(s[i]);
    } else if (s[i] === ')') {
      if (s[i - 1] == '(') {
        if (stack.length !== 0) {
          stack.pop();
        } else {
          return false;
        }
      } else {
        if (stack.length !== 0) {
          if (stack.pop() === '(') {
            continue;
          } else {
            return false;
          }
        } else {
          return false;
        }
      }
    } else if (s[i] === ']') {
      if (s[i - 1] == '[') {
        if (stack.length !== 0) {
          stack.pop();
        } else {
          return false;
        }
      } else {
        if (stack.length !== 0) {
          if (stack.pop() === '[') {
            continue;
          } else {
            return false;
          }
        } else {
          return false;
        }
      }
    } else if (s[i] === '}') {
      if (s[i - 1] == '{') {
        if (stack.length !== 0) {
          stack.pop();
        } else {
          return false;
        }
      } else {
        if (stack.length !== 0) {
          if (stack.pop() === '{') {
            continue;
          } else {
            return false;
          }
        } else {
          return false;
        }
      }
    }
  }
  if (stack.length !== 0) {
    return false;
  } else {
    return true;
  }
};
