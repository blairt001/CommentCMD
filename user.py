class Comments():
	def __init__(self,title,content):
		self.title=title
		self.content=content
		self.comments=[]

	def create_own_comment(self,title):
		comment=input("please enter comment:")
		self.comments.append(Comments(title,comment))
		print("successfully created")
		print(len(self.comments))

	def edit_own_comment(self):
		x=input("please enter the comment title:")
		for key,item in self.comments.items():
			pass
class User():

	def __init__(self, username, password, role="normal"):
		self.username=username
		self.password=password
		self.role=role
		

	def create_user(self):
		p=input("please enter your name:")
		w=input("please enter username:")
		x=input("please enter password:")
		p=User(w,x)
		print("user created successfully")

	
x=User("timo","lubs")
y=Comments("blog","politics")
x.create_user()
y.create_own_comment("title")

