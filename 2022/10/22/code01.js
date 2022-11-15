/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function (s, t) {
  if (s.length < t.length) {
    return "";
  }

  const subMap = new Map();
  [...t].forEach((ele, idx) => {
    if (subMap.has(ele)) {
      const current = subMap.get(ele);
      current.push(idx);
    } else {
      subMap.set(ele, [idx]);
    }
  });

  let startIdx;
  let endIdx;

  return startIdx === undefined
    ? ""
    : [...s].slice(startIdx, endIdx + 1).join("");
};
