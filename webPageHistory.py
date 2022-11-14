

# Stack implementation

class Stack:
	def __init__(self):
		self._data=[]

	def Length(self):
		return len(self._data)
	
	def isEmpty(self):
		return len(self._data)==0
	
	def push(self,e):
	 self._data.insert(0,e)
	
	def top(self):
		if self.isEmpty():
			return
		return self._data[0]
	
	def pop(self):
		if self.isEmpty():
			return
		return self._data.pop(0)
	
	def content(self):
		print(self._data)


# Functions for the webpage history

undo = Stack()    
redo = Stack()


def openWebPage(link): # function that pushes newly opened web pages to redo stack
	redo.push(link)



def MoveForward():   
	if undo.isEmpty():   
		return (f"you are on the recent page at---> {redo.top()}, there is no other recent page.")
	elif undo.Length() < 2:   
		page = undo.pop()
		redo.push(page)
		return (f" you are now at:--> {page}")
	else:
		redo.push(undo.pop())
		return (f" you are now at:--> {redo.top()}")


def MoveBackward():
	if redo.isEmpty():
		return  "you didn't opened any page "
	elif redo.Length() < 2:
		if undo.isEmpty():
			return f"There is no previously opened page.you open only:-->  {redo.top()}"
		return f"There is no other page you reached to firstly opened page at:--> {redo.top()}"
	else:
		undo.push(redo.pop())
		return (f"you are now at:--> {redo.top()}")

# Main function


def main():
	print("*****---------------------------------------------------------------------------------*****")
	print("Options: \n  'N' to open new webpage \n 'B' to move back to the previous page \n 'F' to move forward the webpage ")
	print(" 'Exit'  whenever you finish  your request ")
	print("____________________________________________________________________________________________")
	userRequest = ""
	while userRequest != "EXIT" :
		userRequest =  (input("enter your request\n")).upper()
		print("____________________________________________________________________________________________")
		if userRequest == "N":
			link = input("enter the webpage address\n")
			print("____________________________________________________________________________________________")
			print("you are now visiting",link)
			openWebPage(link)
		elif userRequest == "B":
			print(MoveBackward())
		elif userRequest == "F":
			print(MoveForward())
		elif userRequest == "EXIT":
			verification = (input("Are you sure ? [y/n]: \n")).upper()
			print("____________________________________________________________________________________________")
			if verification == "Y":
				print("you terminated the program")
				userRequest = "EXIT"
			elif verification == "N":
				userRequest = ""	
			else:
				print("Ambiguous command, program terminated")

main()
