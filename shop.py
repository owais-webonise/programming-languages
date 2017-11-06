while(True):	
	print "1. Buy 1 Colgate"
	print "2. Buy 10 Colgates"
	print "3. Buy 5 Colgates and 2 CloseUp"	
	
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

	def colgate_closeup():
		colgate=10*5
		closeup=15*2
		bill_amount(colgate + closeup)

	if ch==1:
		colgate_1()

	if ch==2:
		colgate_10()
	
	if ch==3:
		colgate_closeup()




