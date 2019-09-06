package main

import(
	"bytes"
	"fmt"
	"log"
	"os"
    	"os/exec"
)

func pythonCall(progName string, parameters ...string){
	//var paramString string
	var b bytes.Buffer

	for i := 0; i < len(parameters); i++ {
		b.WriteString(parameters[i])
		if (i != len(parameters)-1){
			//b.WriteString(",")
		}
	}

	fmt.Println(b.String())


	cmd := exec.Command("python3", progName, parameters[0], parameters[1])
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	log.Println(cmd.Run())
}

func main(){
	pythonCall("hello.py", "1", "2")


}

