package main

import (
	"fmt"
	"log"
	"os"
	"os/exec"
	"time"
)

func pythonCall(progName string) {
	cmd := exec.Command("python3", progName)
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	log.Println(cmd.Run())
	time.Sleep(2 * time.Millisecond)
}

func main() {
	fmt.Printf("hello, world\n")
}
