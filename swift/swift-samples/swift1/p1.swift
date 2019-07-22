type file;
file[] texts <FixedArrayMapper; files = "file1.txt, fileB.txt, file3.txt">;

foreach i in [0:2] {
   trace(i);
   
   file[i] = writeData(i);
  
}

