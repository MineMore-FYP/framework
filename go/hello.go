package main

import (
	//"bufio"
    	//"encoding/csv"
    	//"os"
    	"fmt"
    	//"io"
	"time"
)
func print1(i1 int){
	fmt.Println("hi")
}

func print2(s1 int){
	fmt.Println(s1)
}


func main() {

	go print1(42)	
	time.Sleep(1000 * time.Millisecond)
	
	fmt.Println("test1")
	c := make(chan int)
	fmt.Println("test2")
	defer close(c)
  	fmt.Println("test3")
  	c <- 42    // write to a channel
  	fmt.Println("test4")
  	val := <-c // read from a channel
  	fmt.Println("test5")
  	println(val)

	go print2(val)
	time.Sleep(1000 * time.Millisecond)




  	
}
