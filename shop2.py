
print "Shopping Cart"
print "1. Colgate - Rs10"
print "2. CloseUp - Rs15" 


t1=0
t2=0
total1=0
total2=0
ty=0
pp=0
def default():
	while(True):
		print "1.Add colgate to your cart?"
		print "2.Add closeup to your cart?"
		print "3.Remove colgate from your cart?"
		print "4.Remove closeup from your cart?"
		print "5.checkout"
		print "6.Continue shopping"
		print "7. Admin account"
		print "Enter your choice"
		ch=input()
	
		if ch==1:
			global t1
			t1=cart_colgate()
			global total1
			total1=total1+t1	
			print total1
	
		if ch==2:
			global t2
			t2=cart_closeup()
			global total2
			total2=total2+t2
			print total2
	
		if ch==3:
			print "How many colgate you want to remove?"
			chh=input()
			total1=total1-chh

		if ch==4:
			print "How many closeup you want to remove?"
			chhh=input()
			total2=total2-chhh*15
	
		if ch==5:
			checkout()
			break
		if ch==6:
			default()
		if ch==7:
			print "Enter password"
			password=raw_input()
			if password == "12345":
				print "Enter name of product"
				name=raw_input()
				print "Enter its price"
				price=input()
				print "Enter quantity"
				quan=input()
				global pp
				pp=price*quan

def checkout():
		print "Do you want to apply offer on colgate?(BUY 2 GET 1 FREE)"
		choi=raw_input()
		if choi=="yes":
			global ty
			ty=(total1/3)*20 + (total1%3)*10
		else:
			ty=total1*10
		print t1
		print t2
		total=ty+total2
		print pp
		total= total +pp
		print "Your Total Amount is:-", total

	
	
def cart_colgate():	
	print "Enter how many colgate you want?"
	co=input()
	
	return co
	
def cart_closeup():
	
	print "Enter how many closeup you want?"
	cl=input()
	total1=cl*15
	return total1 


default()
