package main

import "fmt"
import "os/exec"
import "time"
import "log"
import "os"

func main() {
    cmd := exec.Command("python",  "-c", "import pythonfile; print pythonfile.df")
    fmt.Println(cmd.Args)
    out, err := cmd.CombinedOutput()
    if err != nil { fmt.Println(err); }
    dataframe := string(out)
    fmt.Println(dataframe)
    time.Sleep(100 * time.Millisecond)



    cmd1 := exec.Command("python3", "selectUserDefinedColumns.py", dataframe)
    cmd1.Stdout = os.Stdout
    cmd1.Stderr = os. Stderr
    log.Println(cmd1.Run())
    time.Sleep(2 * time.Millisecond)
}
