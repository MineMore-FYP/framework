#check how simple mapper works

type messagefile;

(messagefile t) greeting(string m) {
    app {
        echo m stdout=@filename(t);
    }
}

messagefile outfile[] <simple_mapper;prefix="baz",suffix=".txt", padding=2>;

outfile[0] = greeting("hello");
outfile[1] = greeting("middle");
outfile[2] = greeting("goodbye");
