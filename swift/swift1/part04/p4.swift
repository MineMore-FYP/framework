type file;
#string s[] = [ "a.txt", "b.txt", "c.txt" ];

#file f[] <array_mapper;files=s>;

type student {
  file name;
  file age;
  file gpa;
}

student stus[] <csv_mapper;file="stu.csv">;


// A simple app that echo's a string to a file
app (file output) echo (string s) {
   echo s stdout=@output ;
}

// Map a filename to a variable of type file


// Call the app
stus[0].name = echo("hi");

