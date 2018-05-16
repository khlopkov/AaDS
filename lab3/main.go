package main

import (
	"AaDSLab3/graph"
	"time"
	"AaDSLab3/kruskal"
	"AaDSLab3/prima"
)

func main(){
	n:= 100
	for n <= 10000{
		gr:=graph.InitRandomGraph(n, n*n, 1, 1000000)
		edgeList:=kruskal.ConvertToEdgeList(gr)
		kruskallStart:=time.Now()
		edgeList.KruskalAlg(n)
		kruskallEnd:=time.Now().Sub(kruskallStart).Nanoseconds()/1000000
		primaStart:=time.Now()
		prima.PrimaAlg(gr)
		primaEnd:=time.Now().Sub(primaStart).Nanoseconds()/1000000
		println (n, kruskallEnd, primaEnd)
		n+=100
	}

}