while(True):	
	print "1. Buy 1 Colgate"
	print "2. Buy 10 Colgate"
	
	print "Enter your choice"
	ch=input()

	def bill_amount(total):
		print "Total amount is:-",total

	def colgate_1():
		colgate=1*10
		bill_amount(colgate)
	
	def colgate_10():
		colgate=10*10
		bill_amount(colgate)

	if ch==1:
		colgate_1()

	if ch==2:
		colgate_10()





