// 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42587

class Solution {
    fun solution(priorities: IntArray, location: Int): Int {
        val list = arrayListOf<Pair<Int, Int>>();
        val result = arrayListOf<Pair<Int, Int>>();
        for((index, value) in priorities.withIndex()){
            list.add(Pair(index, value))
        }
        while(list.isNotEmpty()){
            val (nowIdx, nowValue) = list.removeAt(0)
            if(list.any({ (idx, value) ->  value > nowValue })){
                list.add(Pair(nowIdx, nowValue))
            }else{
                result.add(Pair(nowIdx, nowValue))
            }
        }
        return result.indexOfFirst({ (idx, value) ->  idx == location }) + 1
    }
}
