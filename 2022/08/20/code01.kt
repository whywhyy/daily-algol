// https://leetcode.com/problems/minimum-number-of-refueling-stops/

class Solution {
    fun minRefuelStops(target: Int, startFuel: Int, stations: Array<IntArray>): Int {
        var currentPos = startFuel
        var fillCount = 0
        val sortedStations = stations.sortedWith(compareByDescending({ it[1] })).toMutableList()
        while (target > currentPos && sortedStations.indexOfFirst { it[0] <= currentPos } != -1) {
            val idx = sortedStations.indexOfFirst { it[0] <= currentPos }
            currentPos += sortedStations[idx][1]
            fillCount += 1
            sortedStations.removeAt(idx)
        }
        return if (target <= currentPos) {
            fillCount
        } else {
            -1
        }
    }
}
