package main

import (
	"fmt"
	"time"
	"log"
	"os"
	"os/exec"
	"strconv"
)

func sendValue(c chan int){
	//send value through channel c
	c <- 700
}

func pythonCall(progName string, value string){
	cmd := exec.Command("python3", progName, value)
	cmd.Stdout = os.Stdout
	cmd.Stderr = os. Stderr
	log.Println(cmd.Run())
	time.Sleep(2 * time.Millisecond)	
}

func main() {	
	//open channel of type string
	values := make(chan int)

	//declare closing of channel
	defer close(values)

	go sendValue(values)

	//Receive operator <= recieve a value from a channel
	value := <-values
	fmt.Println(value)

	valueStr := strconv.Itoa(value)

	time.Sleep(10 * time.Millisecond)

	go pythonCall("hello1.py", valueStr)

	go pythonCall("hello2.py", valueStr)

	time.Sleep(10 * time.Millisecond)
}
