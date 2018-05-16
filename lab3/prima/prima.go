package prima

import "AaDSLab3/graph"

type Edge struct {
	weight int
	to int
}

func (e *Edge)GetWeight() int{
	return e.weight
}
func (e *Edge)GetTo() int{
	return e.to
}

func PrimaAlg(graph *graph.Graph) int{
	w := graph.GetMatrix()
	n := graph.GetVertexesCount()
	cost:=0
	const INF int = int(^(uint(0))>>1)
	dist := make([]Edge, n)
	used := make([]bool, n)
	for i:=0; i<n; i++{
		dist[i].weight = INF
		used[i] = false
	}
	dist[0] = Edge{
		weight:0,
		to: 0,
	}
	for i:=0; i<n; i++{
		minDist := INF
		u := 0
		changed:=false
		for j:=0; j<n; j++{
			if !used[j] && dist[j].weight < minDist{
				minDist = dist[j].weight
				u = j
				changed=true
			}
		}
		if changed {
			cost += minDist
			used[u] = true
			for v := 0; v < n; v++ {
				if w[u][v] < dist[v].weight && w[u][v] != 0 {
					dist[v].weight = w[u][v]
					dist[v].to = u
				}
			}
		}
	}
	return cost
}
