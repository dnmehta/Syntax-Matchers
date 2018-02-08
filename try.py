import pycparser as pyc
from sys import argv

def DFS(node):
	#TypeDef , TypeDecl, Typename etc which had no use haven't been written- we needn't perform DFS on those.
	typeNode = type(node).__name__ ;
	if typeNode == "If":
		DFS(node.cond);
		DFS(node.iftrue);
		DFS(node.iffalse);
	elif typeNode == "Assignment":
		print "####WARNING####";  # After the necessary dict check
	elif typeNode=="Case":
		DFS(node.expr);
		for i in node.stmts:
			DFS(i)
	elif typeNode=="BinaryOp":
		if node.op=='==':
			print "Fine!"
		DFS(node.op);
		DFS(node.left);
		DFS(node.right);
	elif typeNode=="FuncDef":
		for i in node.body:
			DFS(i);
	elif typeNode=="Compound":
		for i in node.block_items:
			DFS(i);
	elif typeNode=="CompoundLiteral":
		DFS(node.init);    #type' won't need a DFS
	elif typeNode=="Decl":
		DFS(node.init);
	elif typeNode=="DeclList":
		for i in node.decls:
			DFS(i);
	elif typeNode=="Default":
		for i in node.stmts:
			DFS(i);
	elif typeNode=="DoWhile":
		DFS(node.cond);
		DFS(node.stmt);
	elif typeNode=="Enum":
		DFS(node.values);
	elif typeNode=="Enumerator":
		DFS(node.value);
	elif typeNode=="EnumeratorList":
		for i in node.enumerators:
			DFS(i);
	elif typeNode=="ExprList":
		for i in node.exprs:
			DFS(i);
	elif typeNode=="FileAST":
		for i in node.ext:
			DFS(i);
	elif typeNode=="For":
		DFS(node.init);
		DFS(node.cond);
		DFS(node.next);
		DFS(node.stmt);
	elif typeNode=="FuncCall":
		DFS(node.args);  #assuming name won't require a dfs
	elif typeNode=="FuncDecl":
		DFS(node.args);

	elif typeNode=="InitList":
		for i in node.exprs:
			DFS(i);
	elif typeNode=="Label":
		DFS(node.stmt);
	elif typeNode=="NamedInitializer":
		for i in node.name:
			DFS(i);
		DFS(node.expr);
	elif typeNode=="ParamList":
		for i in node.params:
			DFS(i);
	elif typeNode=="Return":
		DFS(node.expr);
	elif typeNode=="Struct":
		for i in node.decls:
			DFS(i);
	elif typeNode=="TernaryOp":
		DFS(node.cond);
		DFS(node.iftrue);
		DFS(node.iffalse);
	elif typeNode=="UnaryOp":
		DFS(node.expr);
	elif typeNode=="Union":
		for i in node.decls:
			DFS(i);
	elif typeNode=="While":
		DFS(node.cond);
		DFS(node.stmt);


	
	
		





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