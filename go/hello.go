package main

import (
	"bufio"
    	"encoding/csv"
    	"os"
    	"fmt"
    	"io"
)

func main() {
    	f, _ := os.Open("/home/rajini/go/src/hello/FL_insurance_sample.csv")

    	r := csv.NewReader(bufio.NewReader(f))
   
    	r.Comma = ','

    	for {
        	record, err := r.Read()
        	if err == io.EOF {
            		break
        	}
        	
        	for value := range record {
            		fmt.Printf("%v\t", record[value])	
        	}

		fmt.Printf("\n")		
    	}
}
