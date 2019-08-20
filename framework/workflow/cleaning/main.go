package main

import (
	"log"
	"os"
    	"os/exec"
)

func main() {
	//cmd := exec.Command("python3", "dropUserDefinedColumns.py","/home/amanda/FYP/ds/combined.csv", "Actor2Geo_FullName", "ActionGeo_FullName")
    	cmd := exec.Command("python3", "dropUserDefinedColumns.py","/home/amanda/FYP/testcsv/test.csv", "Actor2Geo_FullName", "ActionGeo_FullName")
	cmd.Stdout = os.Stdout
    	cmd.Stderr = os.Stderr
    	log.Println(cmd.Run())

	cmd1 := exec.Command("python3", "dropColumnsCriteria.py", "/home/amanda/FYP/testcsv/cleanedDataset.csv", "20")
	cmd1.Stdout = os.Stdout
	cmd1.Stderr = os.Stderr
	log.Println(cmd1.Run())

	cmd2 := exec.Command("python3", "dropUserDefinedRows.py", "/home/amanda/FYP/testcsv/cleanedDataset.csv", "Actor1Name", "BRAZIL", "UNITED STATES")
	cmd2.Stdout = os.Stdout
	cmd2.Stderr = os.Stderr
	log.Println(cmd2.Run())

	cmd3 := exec.Command("python3", "removeDuplicateRows.py", "/home/amanda/FYP/testcsv/cleanedDataset.csv")
	cmd3.Stdout = os.Stdout
	cmd3.Stderr = os.Stderr
	log.Println(cmd3.Run())
}
