package main

import (
	"bufio"
    	"encoding/csv"
    	"os"
    	"fmt"
    	"io"
)

func main() {
    cmd := exec.Command("python", "helloworld.py")
    stdout, err := cmd.StdoutPipe()
    if err != nil {
        panic(err)
    }
    stderr, err := cmd.StderrPipe()
    if err != nil {
        panic(err)
    }
    err = cmd.Start()
    if err != nil {
        panic(err)
    }

    go copyOutput(stdout)
    go copyOutput(stderr)
    cmd.Wait()
}

func copyOutput(r io.Reader) {
    scanner := bufio.NewScanner(r)
    for scanner.Scan() {
        fmt.Println(scanner.Text())
    }

}

