import pycparser as pyc
from sys import argv

def DFS(node):
	typeNode = type(node).__name__ ;
	if typeNode == "If" or typeNode=="Switch" or typeNode=="While" or typeNode=="DoWhile":
		DFS(node.cond);
	elif typeNode == "Assignment":
		print "####WARNING####";  # After the necessary dict check
	
	elif typeNode=="BinaryOp":
		#No need for a DFS here? Just check the type.
		if node.op=='==':
			print "Fine!"
	elif typeNode=="FuncDef":
		for i in node.body:
			DFS(i);

	
	
		





class visitor(pyc.c_ast.NodeVisitor):

	def __init__(self, funcname):
		self.funcname = funcname

	def visit_FuncDef(self,node): # Our entry point , now I can do custom DFS :D
		# print "HI";
		DFS(node);
		# DFS(node);
	# def visit_ID(self,node):
	# 	print "ID: " + node.name;

	# def visit_Constant(self,node):
	# 	print "CONSTANT: " + node.type +"  "+ node.value;

	# def visit_Return(self,node):
	# 	print "HEY"
	# 	# print type(node.expr)
	# 	# print node.expr;
	# 	# v.visit(node.expr);

	# def visit_If(self,node):
	# 	print "IF"
	# 	DFS(node);
	# 	#print node.cond;

	# def visit_FuncDef(self, node):
	# 	#print "hello"
	# 	#node.body is a compound object.
	# 	#node.body.block_items has Return, Decl,etc.
	# 	for i in node.body.block_items:
	# 		v.visit(i)



if len(argv) < 2:
	print "Enter file name in command line";
	exit()
ast = pyc.parse_file(argv[1], use_cpp=True)
ast.show()
v = visitor("main")
v.visit(ast)