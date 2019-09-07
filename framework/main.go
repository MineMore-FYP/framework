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

func SendValue(s string, c chan string){
	//send value through channel c
	c <- s
}

func work(messages chan<- string) {
    messages <- "golangcode.com"
}

func pythonCall(progName string, dataset string){
	cmd := exec.Command("python3", progName, dataset)
	cmd.Stdout = os.Stdout
	cmd.Stderr = os. Stderr
	log.Println(cmd.Run())
	time.Sleep(2 * time.Millisecond)
}

func main() {
	//get input dataset location
	cmd := exec.Command("python",  "-c", "from workflow import userScript; print userScript.inputDataset")
	fmt.Println(cmd.Args)
	out, err := cmd.CombinedOutput()
	if err != nil { fmt.Println(err); }
	//input dataset from disk
	inputDataset := string(out)[:len(out)-1]
	fmt.Print(inputDataset)

	//get output dataset location
	cmd1 := exec.Command("python",  "-c", "from workflow import userScript; print userScript.outputDataset")
	fmt.Println(cmd1.Args)
	out1, err1 := cmd1.CombinedOutput()
	if err1 != nil { fmt.Println(err1); }
	//input dataset from disk
	outputDataset := string(out1)[:len(out1)-1]
	fmt.Print(outputDataset)

  //select user defined cols
	go pythonCall("workflow/selection/selectUserDefinedColumns.py", inputDataset)
	time.Sleep(10000 * time.Millisecond)

  //channel
	channel := make(chan string)
	defer close(channel)
  go SendValue(outputDataset, channel)
  output1 := <-channel
  fmt.Println(output1)
  time.Sleep(10000 * time.Millisecond)

  //drop unique cols
	go pythonCall("workflow/cleaning/dropUniqueColumns.py", output1)
	time.Sleep(10000 * time.Millisecond)

  //channel
	channel1 := make(chan string)
	defer close(channel1)
  go SendValue(outputDataset, channel1)
  output1 := <-channel1
  fmt.Println(output1)
  time.Sleep(10000 * time.Millisecond)


}
/*
func csvWriter(){

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

}*/
