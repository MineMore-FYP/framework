package main

import (
	"log"
	"os"
    	"os/exec"
	"bytes"
)

func pythonCall(progName string, dataset string, parameters ...string){
	//var paramString string
	var b bytes.Buffer

	for i := 0; i < len(parameters); i++ {
		b.WriteString(parameters[i])
	}

	cmd := exec.Command("python3", progName, b.String())
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	log.Println(cmd.Run())
}

func main() {
	//drop unique columns here
	cmd1 := exec.Command("python3", "dropUniqueColumns.py","/home/amanda/FYP/testcsv/test.csv")
	cmd1.Stdout = os.Stdout
	cmd1.Stderr = os.Stderr
  	log.Println(cmd1.Run())

	//drop one value columns here
	cmd2 := exec.Command("python3", "dropOneValueColumns.py","/home/amanda/FYP/testcsv/cleanedDataset.csv")
	cmd2.Stdout = os.Stdout
	cmd2.Stderr = os.Stderr
  	log.Println(cmd2.Run())

	//drop user defined cols
	cmd3 := exec.Command("python3", "dropUserDefinedColumns.py","/home/amanda/FYP/testcsv/cleanedDataset.csv", "Actor2Geo_FullName", "ActionGeo_FullName")
	cmd3.Stdout = os.Stdout
	cmd3.Stderr = os.Stderr
  	log.Println(cmd3.Run())

	//drop columns according to user defined empty value percentage
	cmd4 := exec.Command("python3", "dropColumnsCriteria.py", "/home/amanda/FYP/testcsv/cleanedDataset.csv", "20")
	cmd4.Stdout = os.Stdout
	cmd4.Stderr = os.Stderr
	log.Println(cmd4.Run())

	//drop user defined rows
	cmd5 := exec.Command("python3", "dropUserDefinedRows.py", "/home/amanda/FYP/testcsv/cleanedDataset.csv", "Actor1Name", "BRAZIL", "UNITED STATES")
	cmd5.Stdout = os.Stdout
	cmd5.Stderr = os.Stderr
	log.Println(cmd5.Run())

	//drop rows according to user defined empty value percentage
	cmd6 := exec.Command("python3", "dropRowsCriteria.py", "/home/amanda/FYP/testcsv/cleanedDataset.csv", "20")
	cmd6.Stdout = os.Stdout
	cmd6.Stderr = os.Stderr
	log.Println(cmd6.Run())

	//remove duplicate rows
	cmd7 := exec.Command("python3", "removeDuplicateRows.py", "/home/amanda/FYP/testcsv/cleanedDataset.csv")
	cmd7.Stdout = os.Stdout
	cmd7.Stderr = os.Stderr
	log.Println(cmd7.Run())

	//missing values interpolation
	//missing value mode

	//encoding binning
	//standardize normalize --?
	//kmeans




}
