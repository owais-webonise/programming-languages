while(True):	
	print "1. Buy 1 Colgate"
	print "2. Buy 10 Colgates"
	print "3. Buy 5 Colgates and 2 CloseUp"	
	print "4. Colgate Offer(Buy 2 Get 1 Free)"
	
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

	def colgate_offer():
		print "Enter number of Colgates"
		co=input()
		total=(co/3)*20 + (co%3)*10
		bill_amount(total)
	

	if ch==1:
		colgate_1()

	if ch==2:
		colgate_10()
	
	if ch==3:
		colgate_closeup()
	
	if ch==4:
		colgate_offer()




