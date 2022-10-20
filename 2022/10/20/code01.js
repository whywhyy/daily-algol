/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function (num) {
  const arr = ["I", "V", "X", "L", "C", "D", "M"]; // 1, 5 , 10, 50, 100, 500, 1000
  const results = [];
  let nowNum = num;
  let currentPos = 0;
  while (nowNum > 0) {
    const currentNum = nowNum % 10;
    const firstArr = arr[currentPos * 2];
    const secondArr = arr[currentPos * 2 + 1];
    const thirdArr = arr[currentPos * 2 + 2];
    if (currentNum >= 1 && currentNum <= 3) {
      results.push(firstArr.repeat(currentNum));
    }
    if (currentNum === 4) {
      results.push(firstArr + secondArr);
    }
    if (currentNum === 5) {
      results.push(secondArr);
    }
    if (currentNum >= 6 && currentNum <= 8) {
      results.push(secondArr + firstArr.repeat(currentNum - 5));
    }
    if (currentNum === 9) {
      results.push(firstArr + thirdArr);
    }
    currentPos += 1;
    nowNum = Math.floor(nowNum / 10);
  }

  // I II III
  // IV V VI VII VIII
  // IX

  //

  return results.reverse().join("");
};

// order 순서로
var intToRoman = function (num) {
  const list = [
    "M",
    "CM",
    "D",
    "CD",
    "C",
    "XC",
    "L",
    "XL",
    "X",
    "IX",
    "V",
    "IV",
    "I",
  ];
  const valueList = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
  let result = "";

  // Run until we have converted the full number
  while (num !== 0) {
    // Loop though the available numerals
    for (let i = 0; i < list.length; i++) {
      // Check if the outstanding number is greater than the current numeral
      if (num >= valueList[i]) {
        // If so, add this numeral to the result and subtract its value from the outstanding number
        result += list[i];
        num -= valueList[i];
        break;
      }
    }
  }
  return result;
};
