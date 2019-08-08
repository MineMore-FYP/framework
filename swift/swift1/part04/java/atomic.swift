type file;

app (file bf) myproc (string s="foo") {
    args stdout = filename(bf);
}

file f <"sim.out">;
f = myproc();
