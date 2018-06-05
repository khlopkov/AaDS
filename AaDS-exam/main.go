package main

import "AaDS-exam/tree"

func main()  {
	treeOfOfficers := tree.GenerateRandomTree(100)
	treeOfOfficers.PrintTree()
	minBribe:=treeOfOfficers.DFS(0)
	print(minBribe)
}
