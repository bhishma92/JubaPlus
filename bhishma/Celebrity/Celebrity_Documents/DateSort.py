import csv


class BSTnode(object):

	def __init__(self, t, s):
		"""create a new value with key = time"""
		self.time = t
		self.session = s
		self.left = None
		self.right = None
		self.parent = None



class BST(object):

	def __init__(self):
		self.root = None
		self.size = 0

	def insert(self, t):
		self.size += 1
		if self.root is None:
			self.root = BSTnode(t, 1)
		else:
			self.insertNode(self.root, t)

	def insertNode(self, node, t):
		temp = node.time - t
		if node.left is None and node.right is None:
			if node.time < t:
				if abs(temp) < 3600:	
					newNode = BSTnode(t, node.session)
				else:
					newNode = BSTnode(t, node.session + 1) #new session
				node.left = newNode
				newNode.parent = node
			else:
				if abs(temp) < 3600:	
					newNode = BSTnode(t, node.session)
				else:
					newNode = BSTnode(t, node.session + 1) #new session
				node.right = newNode
				newNode.parent = node
		else:
			if node.time < t:
				if node.left is not None:
					self.insertNode(node.left, t)
				else:
					if abs(temp) < 3600:	
						newNode = BSTnode(t, node.session)
					else:
						newNode = BSTnode(t, node.session + 1) #new session
					node.left = newNode
					newNode.parent = node
			else:
				if node.right is not None:
					self.insertNode(node.right, t)
				else:
					if abs(temp) < 3600:	
						newNode = BSTnode(t, node.session)
					else:
						newNode = BSTnode(t, node.session + 1) #new session
					node.right = newNode
					newNode.parent = node


def getSeconds(day, time, rootTime):



	



def printSorted(node, row, csvout):

	if(node == None):
		return

	printSorted(node.left)

	csvout.writer(row[0], node.session, row[1:6])
	#csvout.writer(node.session)


	printSorted(node.right)


def main():

	#with open('exelate_celebrity_20160208.1.tsv','rb') as tsvin, open('output.csv','wb') as csvout:
	with open('example.txt','rb') as tsvin, open('output.csv','wb') as csvout:
    

    		tsvin = csv.reader(open('example.txt','rU'), dialect=csv.excel_tab)
    		csvout = csv.writer(csvout)

    		entry_list = dict()
    		session = dict()


    		for index, row in enumerate(tsvin,start=1):

    			sec = getSeconds(row[5], row[6], entry_list[row[0]].root.time) 

 				if(row[0] in entry_list):	
 					entry_list[row[0]].insert(sec) 
 				else:
 					entry_list[row[0]] = BST()	 
 					entry_list[row[0]].insert(sec)


 			for row in tsvin:

 				if(row[0] in entry_list):
 					printSorted(entry_list[row[0]].root, row, csvout)



     						




	

			

if __name__=="__main__": main()
