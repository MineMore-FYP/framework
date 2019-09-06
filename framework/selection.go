package main

import (
	//"bufio"
  //"encoding/csv"
  "os"
	"os/exec"
  "fmt"
  //"io"
	"log"
	"time"
)

/*func SendValue(s []string, c chan []string){
	//send value through channel c
	c <- s
}
*/
func pythonCall(progName string, dataset string){
	cmd := exec.Command("python3", progName, dataset)
	cmd.Stdout = os.Stdout
	cmd.Stderr = os. Stderr
	log.Println(cmd.Run())
	time.Sleep(2 * time.Millisecond)
}

func main() {
	//create
	cmd := exec.Command("python",  "-c", "from workflow import userScript; print userScript.inputDataset")
	fmt.Print(cmd.Args)
	out, err := cmd.CombinedOutput()
	if err != nil { fmt.Println(err); }
	//input dataset from disk
	inputDataset := string(out)[:len(out)-1]
	fmt.Print(inputDataset)

	//read_line = read_line[:len(read_line)-1]

	go pythonCall("workflow/selection/selectUserDefinedColumns.py", inputDataset)


/*
	instances := make(chan []string)
	defer close(instances)

	csvfile, err := os.Create("test.csv")

	if err != nil {
		log.Fatalf("failed creating file: %s", err)
	}

	csvwriter := csv.NewWriter(csvfile)

	f, _ := os.Open("/home/rajini/Desktop/go/propertyData.csv")
    	r := csv.NewReader(bufio.NewReader(f))

    	for {
        	record, err := r.Read()

		if err == io.EOF {
            		break
        	}

		go SendValue(record,instances)
		instance := <-instances
		fmt.Println(instance)
		_ = csvwriter.Write(instance)

		//fmt.Printf("\n")
    	}
	csvwriter.Flush()

	csvfile.Close()
	*/
}
