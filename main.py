import argparse,datetime
from puma_shoe import puma_shoe
from functools import reduce
comparison_list=[]
shoe_prices={}
size_product_number={}

def tester(runs=1):
	shoe=puma_shoe("000000")
	assert "000000" == shoe.product_number
	
	tests1=[("12",True),("365774",False),("365776",False),("000000",True),("594132",False)]
	
	for i in range(0,runs):
		for i,j in tests1:
			try:
				assert(puma_shoe(i).return_status() == j)
				print("--------------------CASE PASSED------------------")
			except AssertionError:
				print("--------------------CASE FAILED------------------")

def build_comparison(product):
		global comparison_list
		global shoe_prices
		global size_product_number
		s=puma_shoe(product)
		comparison_list.append(s)
		shoe_prices[product]=s.return_price()
		for i in s.return_sizes():
			if(i in size_product_number.keys()):
				l=size_product_number[i]
				if product not in l:
					l.append(product)
			else:
				size_product_number[i]=[]
				size_product_number[i].append(product)

""" mergesort code from:https://pythonandr.com/2015/07/05/the-merge-sort-python-code/"""

def merge(a,b):
	c = []
	while len(a) != 0 and len(b) != 0:
		if a[0] < b[0]:
			c.append(a[0])
			a.remove(a[0])
		else:
			c.append(b[0])
			b.remove(b[0])
	if len(a) == 0:
		c += b
	else:
		c += a
	return c

def mergesort(x):
	if len(x) == 0 or len(x) == 1:
				return x
	else:
		middle = int(len(x)/2)
		a = mergesort(x[:middle])
		b = mergesort(x[middle:])
		return merge(a,b)

def main():
	global shoe_prices
	global size_product_number
	global comparison_list
	parser=argparse.ArgumentParser(usage="This is a program to check the prices of and buy Puma shoes. The program is in honor of Rihanna, a true blessing to the Earth.")
	parser.add_argument(dest="p_no",help="a product number for Puma shoes")
	parser.add_argument("--h","--history",dest="p_his",action="store_true")
	parser.add_argument("--c","--compare",nargs='+',dest="cmp")
	parser.add_argument("--t","--tester",dest="tester",action="store_true")
	args=parser.parse_args()
	run_tester=args.tester
	product_number=args.p_no
	product_history=args.p_his
	comparisons=args.cmp
	
	if(run_tester == True):
		runs=input("How many times would you like to run the tester?")
		try:
			runs=int(runs)
			tester(runs)
		except ValueError:
			print("Invalid number of runs entered. Aborting testing...")

	s=puma_shoe(product_number)

		
	shoe_prices[product_number]=s.return_price()
	for i in s.return_sizes():
		size_product_number[i]=[]
		size_product_number[i].append(product_number)
		
	if(product_history != False):
		with open(str(product_number)+".log","a+") as f:
			f.seek(0)
			history=f.read()
			lst=s.return_sizes()
			sizes=reduce(lambda x,y: str(x)+ " "+str(y), lst)
			tup=(str(datetime.datetime.today()),sizes,s.return_price())
			f.write(str(tup)+"\n")
	if(comparisons != None):
		list(map(build_comparison,comparisons))
		mergesort(comparison_list)

	while(1):
		action=input("Press h to see product history for this shoe.\nPress i to see info about this shoe.\nPress p for size and budget analysis.\nPress c for comparisons.\nPress q to quit.\n")
		if(action == "h" and product_history==True):
			print(history)
		elif(action == "h" and product_history==False):
			print("Histories option not set in command line.")
		elif(action == "i"):
			res="(product number, sizes, price,available colors)="+str((s.product_number, s.return_sizes(),s.return_price(),s.return_colors()))
			print(res)
		elif(action == "p"):
			usr_size=input("What is your size?\n")
			usr_budget=input("What is your budget?\n")
			try:
				usr_budget=float(usr_budget)
			except ValueError:
				print("Not a valid number for budget")
			in_size=set()
			in_budget=set()
			for key in size_product_number:
				if key == usr_size:
					for element in size_product_number[key]:
						in_size.add(element)
	
			for key in shoe_prices:
				if shoe_prices[key] <=usr_budget:
					in_budget.add(key)	
			available=in_size.intersection(in_budget)
			if(len(available)>0):
				print("Shoes with product numbers: " + str(available)+ " are available in your size and are in your budget.")
			else:
				print("Nothing available in your size or budget...")
		elif(action == "c"):
			if(comparisons !=None):
				for i in comparison_list:
					print("(product number, sizes, price)="+str((i.product_number, i.return_sizes(),i.return_price())))
			else:
				print("No shoes to compare to")
		elif(action=='q'):
			exit(0)
		else:
			print("Invalid input. Please try again")

main()
