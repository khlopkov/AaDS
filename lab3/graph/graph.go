package graph

import (
	"math/rand"
	"time"
	)

type Graph struct{
	matrix [][] int
	vertexes int
}

func InitRandomGraph(n int, m int, q int, r int) *Graph{
	rand.Seed(time.Now().UTC().UnixNano())
	chance :=  float64(m) / float64(n) / float64(n)
	graph := Graph{
		matrix: [][] int{},
		vertexes:n,
	}
	for i:=0; i<n; i++ {
		graph.matrix = append(graph.matrix, make([]int, n))
	}
	for i:=0; i<n; i++{
		for j:=0; j<n; j++{
			if rand.Float64() < chance && graph.matrix[i][j]==0 && i!=j {
				weight := rand.Intn(r) + q
				graph.matrix[i][j] = weight
				graph.matrix[j][i] = weight
			}
		}
	}
	return &graph
}
func (graph *Graph) GetMatrix() [][]int{
	return graph.matrix
}
func (graph *Graph) GetVertexesCount() int{
	return graph.vertexes
}
