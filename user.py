class Comments():
	def __init__(self,title,content):
		self.title=title
		self.content=title
class User(Comments):

	def __init__(self,title, content, username, password, role="normal"):
		Comments.__init__(self,title,content)
		self.username=username
		self.password=password
		self.role=role
		self.comments=[]

	def __repr__(self):
		print("{}".format(self.comments[0]))

	def create_own_comment(self,title):
		comment=input("please enter comment:")
		self.comments.append(Comments(title,comment))

	