package tree


type Queue struct{
	head *QueueElem
	tail *QueueElem
	size int
}
type QueueElem struct{
	node *Node
	next *QueueElem
}

func makeQueue(node *Node) *Queue {
	head := QueueElem{
		node,
		nil,
	}
	queue := Queue{
		&head,
		&head,
		1,
	}
	return &queue
}
func (queue *Queue) enqueue(node *Node)  {
	newElem := &QueueElem{
		node,
		nil,
	}
	if queue.tail == nil{
		queue.tail = newElem
		queue.head = newElem
	}else{
		queue.tail.next = newElem
		queue.tail = newElem
	}
	queue.size++
}
func (queue *Queue)dequeue() *Node{
	if queue.head == nil{
		return nil
	}
	dequeued := queue.head
	queue.head = dequeued.next
	if queue.head == nil{
		queue.tail = nil
	}
	queue.size--
	return dequeued.node
}
