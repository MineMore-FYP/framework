package main

import (
	"bufio"
    	"encoding/csv"
    	"os"
    	"fmt"
    	"io"
)

func SendValue(s string, c chan string){
	//send value through channel c
	c <- s
	fmt.Println("Sent through Go Channel...")
}

func main() {
	//create channel
	instances := make(chan string)
	defer close(instances)

	f, _ := os.Open("/home/rajini/go/src/hello/FL_insurance_sample.csv")
    	r := csv.NewReader(bufio.NewReader(f))
    	r.Comma = ','

    	for {
        	record, err := r.Read()
        	if err == io.EOF {
            		break
        	}

        	for value := range record {
			go SendValue(record[value],instances)	
			attribute := <-instances
			fmt.Println(attribute)
        	}

		fmt.Printf("\n")		
    	}
}
