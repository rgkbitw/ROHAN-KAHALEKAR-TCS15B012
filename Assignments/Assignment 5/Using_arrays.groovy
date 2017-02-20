/* 
  Stacks and Queues using Arrays
  
*/

class Stacks{
    def a;
	Stacks()         { a=[]; }
	def push_it(m)   { a.add(m); }
	def print_it()   { println ":->"+a; }
	def size_of_it() { return a.size(); }
	def pop_it()     { return a.pop(); }
}

class Queues{
   def a;
   Queues()         { a=[]; }
   def add(m)       { a.add(m); }
   def del()        { def t=a[0] ;  a=a-a[0] ;  return t; }
   def print_it()   { println ":->"+a; }
   def size_of_it() { return a.size(); }
}


static void main(String[] args)
{
// example
println "Stacks example->"
Stacks a= new Stacks();
a.push_it(12);
a.print_it();
println a.size_of_it();
a.pop_it();
a.print_it();
println "----------"
//example
println "Queues example->"
Queues b= new Queues();
b.add(23);
b.print_it();
b.add(45);
b.add(56);
b.del();
b.print_it();
}

