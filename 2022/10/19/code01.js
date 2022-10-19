// https://leetcode.com/problems/top-k-frequent-words/
/**
 * @param {string[]} words
 * @param {number} k
 * @return {string[]}
 */
var topKFrequent = function (words, k) {
  const wordCountMap = new Map();
  words.forEach((word) => {
    if (wordCountMap.has(word)) {
      const cur = wordCountMap.get(word);
      wordCountMap.set(word, cur + 1);
    } else {
      wordCountMap.set(word, 1);
    }
  });

  return [...wordCountMap]
    .map(([key, val]) => ({ word: key, count: val }))
    .sort((a, b) => b.count - a.count || a.localeCompare(b))
    .slice(0, k)
    .map((ele) => ele.word);
};
