package main

import (
	"lab4/net"
	"log"
)

func main(){
	net := net.CreateNet(6)
	err:=net.AddPath(0, 1, 2, true)
	if err != nil{
		print(err)
	}
	err =net.AddPath(0, 3, 5, true)
	if err != nil{
		print(err)
	}
	err=net.AddPath(0, 2, 10, true)
	if err != nil{
		print(err)
	}
	err=net.AddPath(1, 5, 4, true)
	if err != nil{
		print(err)
	}
	err=net.AddPath(2, 4, 8, true)
	if err != nil{
		print(err)
	}
	err=net.AddPath(2, 5, 7, true)
	if err != nil{
		print(err)
	}
	err=net.AddPath(3, 5, 6, true)
	if err != nil{
		print(err)
	}
	err=net.AddPath(4, 5, 3, true)
	if err != nil{
		print(err)
	}
	net.PrintNet()
	log.Print(net.FordFlakersonAlg())
	net.PrintNet()
}
