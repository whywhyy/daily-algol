// Design Circular Queue
class MyCircularQueue(k: Int) {
    val queue = ArrayDeque<Int>();
    val maxSize: Int = k;
    fun enQueue(value: Int): Boolean {
        var result: Boolean = false;
        if(this.queue.size < this.maxSize){
            this.queue.addLast(value);
            result = true;
        }
        return result;
    }

    fun deQueue(): Boolean {
        var result: Boolean = false;
        if(!this.queue.isEmpty()){
            this.queue.removeFirst();
            result = true;
        }
        return result;
    }

    fun Front(): Int {
        var result: Int = -1;
        if(!this.queue.isEmpty()){
            result = this.queue.first();
        }
        return result;
    }

    fun Rear(): Int {
        var result: Int = -1;
        if(!this.queue.isEmpty()){
            result = this.queue.last();
        }
        return result;
    }

    fun isEmpty(): Boolean {
        return this.queue.isEmpty();
    }

    fun isFull(): Boolean {
        var result: Boolean = false;
        if(this.queue.size == this.maxSize){
            result = true;
        }
        return result;
    }
}

//empty - isfull 사용하기
class MyCircularQueue(k: Int) {
    
    private val queue = Node(0)
    private var capacity = k
    
    init {
        queue.next = queue
        queue.prev = queue
    }

    fun enQueue(value: Int): Boolean {
        if(isFull() || capacity == 0) return false
        val node = Node(value)
        node.prev = queue
        node.next = queue.next
        queue.next!!.prev = node
        queue.next = node
        capacity--
        return true
    }

    fun deQueue(): Boolean {
        if(isEmpty()) return false
        capacity++
        val prev = queue.prev!!
        prev.prev!!.next = queue
        queue.prev = prev.prev
        return true
    }

    fun Front(): Int {
        if(isEmpty()) return -1
        return queue.prev!!.value
    }

    fun Rear(): Int {
        if(isEmpty()) return -1
        return queue.next!!.value
    }

    fun isEmpty(): Boolean {
        return queue.next == queue
    }

    fun isFull(): Boolean {
        return capacity == 0
    }
    
    private class Node(val value: Int,
                      var next: Node? = null,
                      var prev: Node? = null)

}

//
class MyCircularQueue(k: Int) {

    private val ringBuffer: IntArray = IntArray(k+1)
    private val capacity = k+1
    val count :Int
        get() = ringBuffer.count()

    private var read = 0
    private var write = 0

    fun enQueue(value: Int): Boolean {
        if (isFull())
            return false
        else{
            ringBuffer[write] = value
            write = (write + 1) % capacity
            return true
        }

    }

    fun deQueue(): Boolean {
        if (isEmpty())
            return false
        else {
            read = (read + 1) % capacity
            return true
        }
    }

    fun Front(): Int {
        if (isEmpty())
          return -1
        else
            return ringBuffer[read]
    }

    fun Rear(): Int {
        if (isEmpty())
            return -1
        else {
            val indx = if (write == 0) (capacity-1) else (write-1)
            return ringBuffer[indx]
        }
    }

    fun isEmpty(): Boolean {
        return (write == read)
    }

    fun isFull(): Boolean {
        return ((write + 1)%capacity == read)
    }
}

// isFull, isEmpty 를 활용하자 ! 
// this를 쓰지 않아도 된다!?
class MyCircularQueue(k: Int) {

    val queue = ArrayList<Int>(k)
    val queueSize = k
    fun enQueue(value: Int): Boolean {
        if(!isFull()){
            queue.add(value)
            return true
        }
        return false
    }

    fun deQueue(): Boolean {
        if(!isEmpty()){
            queue.removeAt(0)
            return true
        }
        return false
    }

    fun Front(): Int {
        if(isEmpty()){
            return  -1
        }
        return queue[0]
    }

    fun Rear(): Int {
        if(isEmpty()){
            return  -1
        }
        return queue[queue.size-1]
    }

    fun isEmpty(): Boolean {
        return queue.size == 0
    }

    fun isFull(): Boolean {
        return queue.size == queueSize
    }

}