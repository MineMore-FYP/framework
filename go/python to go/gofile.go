package main

import "fmt"
import "os/exec"

func main() {
    cmd := exec.Command("python",  "-c", "import pythonfile; print pythonfile.df")
    fmt.Println(cmd.Args)
    out, err := cmd.CombinedOutput()
    if err != nil { fmt.Println(err); }
    dataframe := string(out)
    fmt.Println(dataframe)

}
