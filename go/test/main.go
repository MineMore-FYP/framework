package main

import (
    "log"
    "os"
    "os/exec"
)

func main() {
    cmd := exec.Command("python", "script.py")
    cmd.Stdout = os.Stdout
    cmd.Stderr = os.Stderr
    log.Println(cmd.Run())

    cmd1 := exec.Command("python", "testargs.py", "hello")
    cmd1.Stdout = os.Stdout
    cmd1.Stderr = os.Stderr
    log.Println(cmd1.Run())
}
