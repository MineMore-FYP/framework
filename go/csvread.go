package main

import (
	"bufio"
    	"encoding/csv"
    	"os"
    	"fmt"
    	"io"
)

func main() {
    	//load a CSV file
	f, _ := os.Open("/home/rajini/go/src/hello/FL_insurance_sample.csv")

	//create a bew reader
    	r := csv.NewReader(bufio.NewReader(f))
   
	//define seperator
    	r.Comma = ','

    	for {
        	record, err := r.Read()
        	if err == io.EOF {
			//stop at EOF
            		break
        	}
        	
		//fmt.Println(record)

        	for value := range record {
            		fmt.Printf("%v\t", record[value])	
        	}

		fmt.Printf("\n")		
    	}
}
