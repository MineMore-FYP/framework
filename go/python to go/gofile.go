package main

import "fmt"
import "os/exec"
import "time"
//import "log"
//import "os"

func main() {
    cmd := exec.Command("python",  "-c", "import pythonfile; print pythonfile.df['SQLDATE']")
    fmt.Println(cmd.Args)
    out, err := cmd.CombinedOutput()
    if err != nil { fmt.Println(err); }
    dataframe := string(out)
    fmt.Println("TEST1")
    fmt.Print(dataframe)
    fmt.Println("TEST2")
    time.Sleep(100 * time.Millisecond)


/*
    cmd1 := exec.Command("python3", "selectUserDefinedColumns.py", data)
    cmd1.Stdout = os.Stdout
    cmd1.Stderr = os. Stderr
    log.Println(cmd1.Run())
    time.Sleep(2 * time.Millisecond)
*/
}
