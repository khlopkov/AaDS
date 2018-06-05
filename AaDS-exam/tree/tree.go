package tree

import (
	"math/rand"
	"time"
)

type Node struct {
	name int
	visasList []Visa
}
type Visa struct{
	officer *Node
	bribe int
}

const INF int = int(^(uint(0))>>1)

func GenerateRandomTree(n int) *Node {
	rand.Seed(time.Now().UnixNano())
	visasCount := rand.Intn(14) + 1
	root := Node{
		0,
		make([]Visa, visasCount),
	}
	root.generateChilds(n - visasCount)
	return &root
}

func (root *Node) generateChilds(remaining int){
	priority := makeQueue(root)
	dequeued := priority.dequeue()
	name:=1
	for dequeued != nil{
		for i:=0; i<len(dequeued.visasList); i++{
			visasCount := rand.Intn(15);
			bribe := rand.Intn(100)
			if visasCount < remaining {
				remaining -= visasCount
			}else {
				visasCount=remaining
				remaining = 0
			}
			dequeued.visasList[i] = Visa{
				&Node{
					name,
					make([]Visa, visasCount),
				},
				bribe,
			}
			priority.enqueue(dequeued.visasList[i].officer)
			name++
		}
		dequeued = priority.dequeue()
	}
}
func (root *Node) PrintTree(){
	priority := makeQueue(root)
	dequeued := priority.dequeue()
	for dequeued != nil{
		if len(dequeued.visasList) > 0 {
			print(dequeued.name)
			print(": ")
			for i := 0; i < len(dequeued.visasList); i++ {
				print("(", dequeued.visasList[i].officer.name,", ", dequeued.visasList[i].bribe, ") ")
				priority.enqueue(dequeued.visasList[i].officer)
			}
			println()
		}
		dequeued = priority.dequeue()
	}
}

func (node *Node)DFS(pathToNode int) int{
	min := pathToNode
	for i := 0; i < len(node.visasList); i++{
			path := node.visasList[i].officer.DFS(pathToNode + node.visasList[i].bribe)
			if path < min || i==0{
				min = path
			}
	}
	return min
}


