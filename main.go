package main

import (
	//"bufio"
	//"encoding/csv"
	"fmt"
	"os"
	"os/exec"
	"strconv"

	//"io"
	"log"
	"time"
)

func SendValue(s string, c chan string) {
	//send value through channel c
	c <- s
}

func work(messages chan<- string) {
	messages <- "golangcode.com"
}

func pythonCall(progName string, dataset string) {
	cmd := exec.Command("python3", progName, dataset)
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	log.Println(cmd.Run())
	//time.Sleep(2 * time.Millisecond)
}

func pythonCallOneParam(progName string, dataset string, para string) {
	cmd := exec.Command("python3", progName, dataset, para)
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	log.Println(cmd.Run())
	//time.Sleep(2 * time.Millisecond)
}

func main() {

	//get input dataset location
	cmd := exec.Command("python", "-c", "from workflow import userScript; print userScript.inputDataset")
	//fmt.Println(cmd.Args)

	out, err := cmd.CombinedOutput()
	if err != nil {
		fmt.Println(err)
	}
	//input dataset from disk
	inputDataset := string(out)[:len(out)-1]
	//fmt.Print(inputDataset)

	//get output dataset location
	cmd1 := exec.Command("python", "-c", "from workflow import userScript; print userScript.outputDataset")
	//fmt.Println(cmd1.Args)

	out1, err1 := cmd1.CombinedOutput()

	if err1 != nil {
		fmt.Println(err1)
	}
	//input dataset from disk
	outputDataset := string(out1)[:len(out1)-1]
	//fmt.Print(outputDataset)

	///////////////////////////*****************SELECTION************************////////////////////////

	//select user defined cols
	go pythonCall("workflow/selection/selectUserDefinedColumns.py", inputDataset)
	fmt.Println("test1")
	time.Sleep(10000 * time.Millisecond)
	fmt.Println("test2")
	fmt.Println("Select User Defined Columns Complete")

	//channel
	channel := make(chan string)
	defer close(channel)
	go SendValue(outputDataset, channel)
	output := <-channel
	time.Sleep(10000 * time.Millisecond)

	///////////////////////////*****************CLEANING************************////////////////////////

	//drop unique cols
	go pythonCall("workflow/cleaning/dropUniqueColumns.py", output)
	fmt.Println("test3")
	time.Sleep(10000 * time.Millisecond)
	fmt.Println("test4")
	fmt.Println("Drop unique columns complete")

	//channel
	channel1 := make(chan string)
	defer close(channel1)
	go SendValue(outputDataset, channel1)
	output1 := <-channel1
	time.Sleep(10000 * time.Millisecond)

	//drop one value cols
	go pythonCall("workflow/cleaning/dropOneValueColumns.py", output1)
	fmt.Println("test5")
	time.Sleep(10000 * time.Millisecond)
	fmt.Println("test6")
	fmt.Println("Drop one value columns complete")

	//channel
	channel2 := make(chan string)
	defer close(channel2)
	go SendValue(outputDataset, channel2)
	output2 := <-channel2
	time.Sleep(10000 * time.Millisecond)

	//Drop user defined cols
	go pythonCall("workflow/cleaning/dropUserDefinedColumns.py", output2)
	fmt.Println("test7")
	time.Sleep(10000 * time.Millisecond)
	fmt.Println("test8")
	fmt.Println("Drop user defined columns complete")

	//channel
	channel3 := make(chan string)
	defer close(channel3)
	go SendValue(outputDataset, channel3)
	output3 := <-channel3
	time.Sleep(10000 * time.Millisecond)

	//#drop columns according to user defined empty value percentage
	go pythonCall("workflow/cleaning/dropColumnsCriteria.py", output3)
	fmt.Println("test9")
	time.Sleep(10000 * time.Millisecond)
	fmt.Println("test10")
	fmt.Println("Drop user defined rows complete")

	/*//channel
	  channel4 := make(chan string)
	  defer close(channel4)
	  go SendValue(outputDataset, channel4)
	  output4 := <-channel4
	  fmt.Println("Drop columns criteria complete")
	  time.Sleep(10000 * time.Millisecond)

	  //#drop user defined rows
	  go pythonCall("workflow/cleaning/dropUserDefinedRows.py", output4)
	  time.Sleep(10000 * time.Millisecond)
	*/
	//channel
	channel5 := make(chan string)
	defer close(channel5)
	go SendValue(outputDataset, channel5)
	output5 := <-channel5
	time.Sleep(10000 * time.Millisecond)

	//drop rows according to user defined empty value percentage
	go pythonCall("workflow/cleaning/dropRowsCriteria.py", output5)
	fmt.Println("test11")
	time.Sleep(10000 * time.Millisecond)
	fmt.Println("test12")
	fmt.Println("Drop row criteria complete")

	//channel
	channel6 := make(chan string)
	defer close(channel6)
	go SendValue(outputDataset, channel6)
	output6 := <-channel6
	time.Sleep(10000 * time.Millisecond)

	//#remove duplicate rows
	go pythonCall("workflow/cleaning/removeDuplicateRows.py", output6)
	fmt.Println("test13")
	time.Sleep(10000 * time.Millisecond)
	fmt.Println("test14")
	fmt.Println("Remove duplicate rows complete")

	//channel
	channel7 := make(chan string)
	defer close(channel7)
	go SendValue(outputDataset, channel7)
	output7 := <-channel7
	time.Sleep(10000 * time.Millisecond)

	//missing value interpolation
	go pythonCall("workflow/cleaning/missingValuesInterpolate.py", output7)
	fmt.Println("test15")
	time.Sleep(10000 * time.Millisecond)
	fmt.Println("test16")
	fmt.Println("Missing values interpolate complete")

	//channel
	channel8 := make(chan string)
	defer close(channel8)
	go SendValue(outputDataset, channel8)
	output8 := <-channel8
	time.Sleep(10000 * time.Millisecond)

	//mode for user defined columns
	go pythonCall("workflow/cleaning/missingValuesMode.py", output8)
	fmt.Println("test17")
	time.Sleep(10000 * time.Millisecond)
	fmt.Println("test18")
	fmt.Println("Missing values mode complete")

	//channel
	channel9 := make(chan string)
	defer close(channel9)
	go SendValue(outputDataset, channel9)
	output9 := <-channel9
	time.Sleep(10000 * time.Millisecond)

	///////////////////////////*****************TRANSFORMATION************************////////////////////////
	//standardize user defined columns
	go pythonCall("workflow/transformation/standardize.py", output9)
	fmt.Println("test19")
	time.Sleep(10000 * time.Millisecond)
	fmt.Println("test20")
	fmt.Println("Standardize complete")

	//channel
	channel10 := make(chan string)
	defer close(channel10)
	go SendValue(outputDataset, channel10)
	output10 := <-channel10
	time.Sleep(10000 * time.Millisecond)

	//rescale user defined Columns
	go pythonCall("workflow/transformation/rescale.py", output10)
	fmt.Println("test21")
	time.Sleep(10000 * time.Millisecond)
	fmt.Println("test22")
	fmt.Println("Rescaling complete")

	//channel
	channel11 := make(chan string)
	defer close(channel11)
	go SendValue(outputDataset, channel11)
	output11 := <-channel11
	time.Sleep(10000 * time.Millisecond)

	//binarize user defined Columns
	go pythonCall("workflow/transformation/binarize.py", output11)
	fmt.Println("test23")
	time.Sleep(10000 * time.Millisecond)
	fmt.Println("test24")
	fmt.Println("Binarization complete")

	//channel
	channel12 := make(chan string)
	defer close(channel12)
	go SendValue(outputDataset, channel12)
	output12 := <-channel12
	time.Sleep(10000 * time.Millisecond)

	//encoding user defined Columns
	go pythonCall("workflow/transformation/encoding.py", output12)
	fmt.Println("test25")
	time.Sleep(10000 * time.Millisecond)
	fmt.Println("test26")
	fmt.Println("Encoding complete")

	//channel
	channel13 := make(chan string)
	defer close(channel13)
	go SendValue(outputDataset, channel13)
	output13 := <-channel13
	time.Sleep(10000 * time.Millisecond)

	///////////////////////////*****************MINING************************////////////////////////

	//get starting number of cluster from user script
	cmd3 := exec.Command("python", "-c", "from workflow import userScript; print userScript.startWithNumberOfClusters")
	//fmt.Println(cmd3.Args)
	out3, err3 := cmd3.CombinedOutput()
	if err3 != nil {
		fmt.Println(err3)
	}

	startWithNumberOfClusters := string(out3)[:len(out3)-1]
	fmt.Println(startWithNumberOfClusters)
	startWithNumberOfClustersInt, err5 := strconv.Atoi(startWithNumberOfClusters)
	if err5 == nil {
		fmt.Println(startWithNumberOfClustersInt)
	}

	//get starting number of cluster from user script
	cmd4 := exec.Command("python", "-c", "from workflow import userScript; print userScript.endWithNumberOfClusters")
	//fmt.Println(cmd4.Args)
	out4, err4 := cmd4.CombinedOutput()
	if err4 != nil {
		fmt.Println(err4)
	}

	endWithNumberOfClusters := string(out4)[:len(out4)-1]
	fmt.Println(endWithNumberOfClusters)
	endWithNumberOfClustersInt, err6 := strconv.Atoi(endWithNumberOfClusters)
	if err6 == nil {
		fmt.Println(endWithNumberOfClustersInt)
	}
	/*
		//get starting number of cluster from user script
		cmd7 := exec.Command("python", "-c", "from workflow import userScript; print userScript.plotLocation")
		//fmt.Println(cmd4.Args)
		out7, err7 := cmd7.CombinedOutput()
		if err7 != nil {
			fmt.Println(err7)
		}

		endWithNumberOfClusters := string(out4)[:len(out4)-1]
		fmt.Println(endWithNumberOfClusters)
	*/
	for i := startWithNumberOfClustersInt; i <= endWithNumberOfClustersInt; i++ {
		/////////////////KMEANS////////////////
		iStr := strconv.Itoa(i)
		go pythonCallOneParam("workflow/mining/kmeans.py", output13, iStr)
		//go pythonCall("workflow/mining/kmeans.py", output13)
		//time.Sleep(150000 * time.Millisecond)
		fmt.Println("Kmeans complete ", i)
	}
	time.Sleep(60000 * time.Millisecond)
	fmt.Println("Kmeans completed for all iterations")

	//////////////////LinearRegression/////////////////
	/*
		go pythonCall("workflow/mining/linearRegression.py", output13)
		time.Sleep(60000 * time.Millisecond)
	  fmt.Println("Linear Regression complete")*/


	//////////////////KNN///////////////// - TODO: loop

	go pythonCall("workflow/mining/KNN.py", output13)
	time.Sleep(60000 * time.Millisecond)
	fmt.Println("KNN complete")


	fmt.Println("test27")

	time.Sleep(60000 * time.Millisecond)
	fmt.Println("test28")
	fmt.Println("Workflow Complete")
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
