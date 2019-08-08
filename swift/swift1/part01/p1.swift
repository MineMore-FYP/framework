type file;

#output param file o. no input params.
#simulation invokes simulate executable passing the value of o as a command line arg
app (file o) simulation ()
{
  simulate stdout=filename(o);
}

file f <"sim.out">;
f = simulation();
