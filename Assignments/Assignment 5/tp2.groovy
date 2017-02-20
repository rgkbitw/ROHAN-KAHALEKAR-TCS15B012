/*
  Stacks And Queues using Linked_list 
 */


class Block{
    def data;
	Block next_link;
	Block(m){ data=m; next_link=null; }
	Block(m,n){ data=m;  next_link=n; }
    def get_link(){ return next_link; }    
	def get_data(){ return data; }
    def set_link(m){ next_link=m; }
    def set_data(m) { data=m; }	
    def print_this(){ print data+" "; }
	}

class Linked_list{
    def head;
	Linked_list() {}
	Linked_list(m){ head=m; }
	def print_this(){ print ":->" ; Block temp = head;  while (temp!= null ) { temp.print_this();  temp=temp.get_link(); };  println "";  } 
	def size_of_it(){ Block temp=head; def counter=0; while (temp!= null ) { temp=temp.get_link(); counter++; }; return counter;  }
	def add_to_front(m){ Block temp= new Block(m);  temp.set_link(head); head=temp; }
	def add_to_end(m){ Block temp= new Block(m); Block c= head;  while(c.get_link()!= null ) { c=c.get_link(); }; c.set_link(temp); }
    def read_it(){ return head.get_data(); }
    def del_at_head(){ Block temp = head;  head=head.next_link; return temp.data; }
	
	def stack_()  // to show implemenatation 
	{
	println "1:push"
	println "2:pop"
	println "3:print"
	println "4:return"
	def c=System.console().readLine();
	while (1)
	{
	if (c=="1")  { def temp= System.console().readLine(); this.add_to_front(temp);  c=System.console().readLine(); }	
	if (c=="2")  { def m=this.del_at_head(); println "deleted:"+m;  c=System.console().readLine(); }
	if (c=="3")  { this.print_this();  c=System.console().readLine();}
	if (c=="4")  { return ;} 
	} 
	}
	
	
	def queue_()  // to show implemenatation
	{
	println "1:add to queue"
	println "2:delete"
	println "3:print"
	println "4:return"
	
	def c=System.console().readLine();
	while (1)
	{
	if (c=="1") { def temp= System.console().readLine(); this.add_to_end(temp);  c=System.console().readLine(); }	
	if (c=="2") { def m=this.del_at_head(); println "deleted:"+m;  c=System.console().readLine(); }
	if (c=="3") { this.print_this();  c=System.console().readLine(); }
	if (c=="4") { return ;}
    }
	}
}

static void main(String[] args)
{
Block a = new Block( "null" )
Linked_list l = new Linked_list( a );
println "1: To Use Stack:"
println "2: To Use Queue:"
println "-----------------"
def c= System.console().readLine();
if (c=="1") { println "--Stack--"; l.stack_();}
if (c=='2') { println "--Queue--"; l.queue_();}
}	