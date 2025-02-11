

import kotlin.collections.mutableListOf
import kotlin.io.readLine
class Solution { // 100 ms
    fun removeOccurrences(s: String, part: String): String {
        var stack = mutableListOf<String>()
        s.forEach { 
            stack.add(it.toString())
            if (stack.size >= part.length && stack.takeLast(part.length).joinToString("") == part) {
                repeat(part.length) { stack.removeLast() }  
            }
         }
         return stack.joinToString("")
    }
}

// to only string handle
class Solution { // 20 ms
    fun removeOccurrences(s: String, part: String): String {
        var currentS = ""
        s.forEach {
            currentS += it
            if (currentS.endsWith(part)) {
                currentS = currentS.removeSuffix(part)
            }
         }
        return currentS
    }
}

// no string append - only find and delete
class Solution {  // 13 ms  
    fun removeOccurrences(s: String, part: String): String {
        var result = s
        var n = part.length
        do {
            val idx = result.indexOf(part)
            if (idx != -1) {
                result = result.removeRange(idx, idx + n)
            }
        } while(idx != -1)
        
        return result
    }
}