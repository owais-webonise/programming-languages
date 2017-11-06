while(True):	
	print "1. Buy 1 Colgate"
	print "2. Buy 10 Colgates"
	print "3. Buy 5 Colgates and 2 CloseUp"	
	print "4. Colgate Offer(Buy 2 Get 1 Free)"
	print "5. Colgate(Offer) and CloseUp"
	
	print "Enter your choice"
	ch=input()

	def bill_amount(total):
		print "Total amount is:-",total

	def colgate_1(n):
		colgate=n*10
		bill_amount(colgate)
	
	def colgate_closeup():
		colgate=10*5
		closeup=15*2
		bill_amount(colgate + closeup)

	def offer_extra():
		print "Enter number of Colgates"
		co=input()
		total=(co/3)*20 + (co%3)*10
		return total

	def colgate_offer():
		t=offer_extra()
		bill_amount(t)	

	def colgate_closeup_offer():
		total1=offer_extra()
		print "Enter number of closeup"
		cl=input()
		total2= total1 + cl*15
		bill_amount(total2)

	

	if ch==1:
		colgate_1(1)

	if ch==2:
		colgate_1(10)
	
	if ch==3:
		colgate_closeup()
	
	if ch==4:
		colgate_offer()
	
	if ch==5:	
		colgate_closeup_offer()




