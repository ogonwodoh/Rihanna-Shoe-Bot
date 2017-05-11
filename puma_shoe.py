import requests,json,bs4,re

class puma_shoe(object):
	__failed=False
	__price=-1
	product_number=None
	url=None
	__sizes=[]

	def __init__(self,product_number):
		self.product_number=product_number
		self.build()
	def __getitem__(self,key):
		return self[key]
	def __setitem__(self,key,value):
		self[key]=value
	def __iter__(self):
		t=(self.product_number,self.__checked,self.__price,self.__failed)
		return t
	def __eq__(self,other):
		return self.__price == other.__price
	def __lt__(self,other):
		return self.__price < other.__price
	def __gt__(self,other):
		return self.__price > other.__price
	def __le__(self,other):
		return self.__price <= other.__price
	def __ge__(self,other):
		return self.__price >= other.__price

	def status(self):
		if(self.__checked == False):
			return "Shoe hasn't been checked yet...."
		else:
			return self.__failed

	def build(self):
		fake_url=builder.build(self,self.product_number)
		url_and_response=self.request_and_verify(fake_url)
		if(url_and_response != None and url_and_response[2] in range(200,300)):
			self.url=url_and_response[0]
			self.__get_size(url_and_response[1])
			self.__get_price(url_and_response[1])

	def request_and_verify(self,url):
		res=requests.get(url)
		status=res.status_code
		if(status in range(200,300)):
			self.__checked=True
			self.__failed=False
			return (res.url,res.text,res.status_code)
		elif(status in range(300,400)):
			self.__checked=True
			self.__failed=False
			return request_and_verify(res.history)
		elif(status in range(400,500)):
			self.__checked=True
			self.__failed=True
			return None
		else:
			self.__checked=True
			self.__failed=True
			return None

	def return_sizes(self):
		return self.__sizes

	def return_price(self):
		return self.price
	
	def return_status(self):
		return self.__failed

	def __get_size(self,response_text):
		page=bs4.BeautifulSoup(response_text, "lxml")
		raw_sizes=page.select('#va-size')
		to_be_processed=raw_sizes[0].getText()
		size_string=str(to_be_processed).replace('\n'," ")
		lst=size_string.split()
		lst=lst[2:]		
		self.__sizes=lst

	def __get_price(self,response_text):
		page=bs4.BeautifulSoup(response_text, "lxml")
		raw_price=page.select(".stdPrice")
		raw_price_str=str(raw_price)
		price_str=re.sub("^.*data-price=\"","",raw_price_str)
		price_str=re.sub("\".*$","",price_str)
		try:
			self.price=float(price_str)
		except ValueError:
			self.price=-1
	
class builder(puma_shoe):
	def build(self,product_number):
		start="http://us.puma.com/en_US/pna"
		end=".html"
		complete=start+product_number+end
		return complete

