// https://leetcode.com/problems/minimum-number-of-refueling-stops/
function minRefuelStops(target: number, startFuel: number, stations: number[][]): number {
    let fillCount = 0;
    let currentPos = startFuel;
    stations.sort((a, b) => b[1] - a[1] || a[0] - b[0]);
    while (target > currentPos && stations.filter(([pos, fuel]) => pos <= currentPos).length) {
        const fillIdx = stations.findIndex((ele) => ele[0] <= currentPos);
        currentPos += stations[fillIdx][1];
        stations.splice(fillIdx, 1);
    }

    return target <= currentPos ? fillCount : -1;
};
