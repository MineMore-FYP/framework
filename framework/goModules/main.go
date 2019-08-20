package main

import (
    "log"
    "os"
    "os/exec"
)

func main() {
    cmd := exec.Command("python", "/home/rajini/Documents/framework/framework/goModules/test/script.py")
    cmd.Stdout = os.Stdout
    cmd.Stderr = os.Stderr
    log.Println(cmd.Run())
}
