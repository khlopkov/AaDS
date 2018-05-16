package kruskal

import (
	"AaDSLab3/graph"
	"math/rand"
	"AaDSLab3/set"
)

type EdgeList struct {
	edges []Edge
}

type Path struct {
	from int
	to int
}
type Edge struct {
	weight int
	path Path
}


func ConvertToEdgeList(gr *graph.Graph) *EdgeList{
	matrix := gr.GetMatrix()
	n := gr.GetVertexesCount()
	edgeList := EdgeList{
		edges:[]Edge{},
	}
	for i:=0; i<n; i++{
		for j:=i; j<n; j++{
			if matrix[i][j] != 0{
				newEdge := Edge{
					weight:matrix[i][j],
					path:Path{
						from: i,
						to: j,
					},
				}
				edgeList.edges = append(edgeList.edges, newEdge)
			}
		}
	}
	return &edgeList
}

func (edgeList *EdgeList)swap(aIndex int, bIndex int){
	t:=edgeList.edges[aIndex]
	edgeList.edges[aIndex] = edgeList.edges[bIndex]
	edgeList.edges[bIndex]=t
}

func (edgeList *EdgeList)quickSort(left int, right int)  {
	if(left<right){
		pivotIndex:=rand.Intn(right-left) + left
		pivotIndex = edgeList.partition(left, right, pivotIndex)
		edgeList.quickSort(left, pivotIndex-1)
		edgeList.quickSort(pivotIndex+1, right)
	}
}

func (edgeList *EdgeList)partition(left int, right int, pivotIndex int) int {
	pivotValue:=edgeList.edges[pivotIndex].weight
	edgeList.swap(pivotIndex, right)
	tempIndex:=left
	for i:=left; i<right;i++{
		if edgeList.edges[i].weight<pivotValue{
			edgeList.swap(i, tempIndex)
			tempIndex+=1
		}
	}
	edgeList.swap(tempIndex,right)
	return tempIndex
}

func (graph *EdgeList)KruskalAlg(n int) int{
	var res []Edge
	m := len(graph.edges)
	var cost int = 0
	graph.quickSort(0, m - 1)
	var setStruct = set.NewSet(n)
	for i := 0; i < m; i++{
		a := graph.edges[i].path.from
		b := graph.edges[i].path.to
		w := graph.edges[i].weight
		if setStruct.Get(a) != setStruct.Get(b){
			cost += w
			res = append(res, graph.edges[i])
			setStruct.Unite(a, b)
		}
	}
	return cost
}