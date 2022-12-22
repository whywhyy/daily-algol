/**
 * @param {number[][]} rooms
 * @return {boolean}
 */
var canVisitAllRooms = function (rooms) {
  if (rooms.length === 1) {
    return true;
  }
  const visited = new Map();
  visited.set(0, true);

  const queue = [];
  rooms[0].forEach((it) => {
    queue.push(it);
  });

  while (queue.length) {
    const nowKey = queue.pop();
    if (visited.has(nowKey)) {
      continue;
    }
    visited.set(nowKey, true);
    rooms[nowKey].forEach((it) => {
      queue.push(it);
    });
  }

  let result = true;
  for (let i = 0; i < rooms.length; i++) {
    if (!visited.has(i)) {
      result = false;
      break;
    }
  }
  return result;
};
