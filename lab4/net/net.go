package net

import "errors"

const INF int = int(^(uint(0))>>1)

type Net struct{
	vertexes []Vertex
}

type Vertex struct{
	childs []Path
}

type Path struct{
	to int
	backEdge bool
	flow int
	capacity int
}

func CreateNet(vertexesCount int) *Net{
	return &Net{
		vertexes:make([]Vertex, vertexesCount),
	}
}

func (net *Net)AddPath(from int, to int, capacity int, twosided bool) error{
	vertexCount := len(net.vertexes)
	if from < 0 || to < 0 || from >= vertexCount || to >= vertexCount{
		return errors.New("No such vertex")
	}
	if from == vertexCount - 1 && !twosided{
		return errors.New("You can't add path to sink")
	}
	if to == 0 && !twosided{
		return errors.New("You can't add path to source")
	}
	if twosided && (from == len(net.vertexes) - 1 || to == 0){
		var temp int
		temp = to
		to = from
		from = temp
		twosided = false
	}
	if twosided && (to == len(net.vertexes) - 1 || from == 0){
		twosided = false
	}
	if net.vertexes[from].childs == nil{
		net.vertexes[from].childs = make([]Path, 0)
	}
	net.vertexes[from].childs = append(net.vertexes[from].childs,
		Path{
			to: to,
			backEdge: false,
			flow: 0,
			capacity:capacity,
		})
	if net.vertexes[to].childs == nil{
		net.vertexes[to].childs = make([]Path, 0)
	}
	backEdge := true
	if twosided {
		backEdge = false
	}
	net.vertexes[to].childs = append(net.vertexes[to].childs,
		Path{
			to: from,
			backEdge: backEdge,
			flow: 0,
			capacity:capacity,
		})
	return nil
}

func fillFalse(arr []bool){
	for i:=0; i < len(arr); i++{
		arr[i] = false
	}
}

func (net *Net)FordFlakersonAlg() int{
	vertexCount := len(net.vertexes)
	visited := make([]bool, vertexCount)
	fillFalse(visited)
	maxFlow:=0
	itterationResult:=net.dfs(0, INF, visited)
	for itterationResult > 0{
		fillFalse(visited)
		maxFlow+=itterationResult
		itterationResult=net.dfs(0, INF, visited)
	}
	return maxFlow;
}
func min(a int, b int) int{
	if a > b {
		return b
	}else {
		return a
	}
}
func (net *Net) dfs(u int, Cmin int, visited []bool) int{
	if u == len(net.vertexes) - 1{
		return Cmin
	}
	visited[u] = true
	for i:=0; i < len(net.vertexes[u].childs); i++{
		v := &net.vertexes[u].childs[i]
		if !visited[(*v).to] && (*v).flow < (*v).capacity{
			delta := net.dfs((*v).to, min(Cmin, (*v).capacity - (*v).flow), visited)
			if delta > 0 {
				if !(*v).backEdge{
					(*v).flow+=delta
				}else{
					(*v).flow-=delta
				}
				return delta
			}
		}
	}
	return 0
}
func (net *Net)PrintNet()  {
	for i:=0; i < len(net.vertexes); i++{
		for j:=0; j < len(net.vertexes[i].childs); j++{
			if !net.vertexes[i].childs[j].backEdge{
				println(i, net.vertexes[i].childs[j].to, net.vertexes[i].childs[j].flow)
			}
		}
	}
}