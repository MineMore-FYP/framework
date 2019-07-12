//unbuffered channel : communication will succeed between go routines only if sender and receiver are ready
//subsequently blocked till value is received

package main

import (
    "fmt"
)

func SendValue(c chan string){
	//send value through channel c
	c <- "Hello World"
}

func main() {
	fmt.Println("Go Channels")
	
	//open channel of type string
	values := make(chan string)

	//declare closing of channel
	defer close(values)
	
	go SendValue(values)

	//Receive operator <= recevice a value from a channel
	value := <-values
	fmt.Println(value)	
}
