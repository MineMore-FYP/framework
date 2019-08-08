type file;

string x;
x = readData("newline0.txt");

app (string o) simulation ()
{
  rand stdout=x(o);
}

file f <"preprocessed.out">;
f = simulation();
