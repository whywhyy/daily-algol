// https://programmers.co.kr/learn/courses/30/lessons/42583?language=kotlin
// 강산 // 왜안돼지..
// 아 ! 다리길이보다 많은 트럭은 올라갈 수 없다!!@#!@#!@#!@#
// 흠.. 다시 ! 풀어야할듯
class Solution {
    fun solution(bridge_length: Int, weight: Int, truck_weights: IntArray): Int {
        val list = arrayListOf<Int>()
        for(value in truck_weights){
            list.add(value)
        }

        var answer = 0
        val queue = arrayListOf<Pair<Int,Int>>()
        while(list.isNotEmpty()){
            answer += 1
            while(queue.isNotEmpty()){
                // remove queue
                val (qTruck, qAnswer) = queue[0]
                val qMoved = answer - qAnswer +1
                if(qMoved < bridge_length){
                    break
                }
                queue.removeAt(0)
            }
            val nowTruck = list.removeAt(0)
            queue.add(Pair(nowTruck, answer))
            var nowTotal = queue.map({(truck, answer) -> truck}).sum()
            if(list.isNotEmpty() && nowTotal + list[0] <= weight){
                // go input
                continue
            }else {
                val (qTruck, qAnswer) = queue[0]
                answer +=  bridge_length - (answer - qAnswer) + 1
            }
        }
        while(queue.isNotEmpty()){
            // remove queue
            val (qTruck, qAnswer) = queue[0]
            val qMoved = answer - qAnswer + 1
            if(qMoved < bridge_length){
                answer +=  bridge_length - qMoved
            }
            queue.removeAt(0)
        }
        return answer
    }
}