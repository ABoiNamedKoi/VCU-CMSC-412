from urllib.request import urlopen as request
from bs4 import BeautifulSoup as soup
import csv
import urllib.parse
import urllib.request


f1 = open('amazondata.csv')
csv_file = csv.reader(f1)
URLarray = []

for row in csv_file:
	URLarray.append(row[0])

filename = "amazonfakespot.csv"
f1 = open(filename, "w")
headers = "ProductName,Grade,PercentageScore,Users,URL\n"
f1.write(headers)

empty = ''
empty_array = []

for URL in URLarray:
	url_input = URL
	user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
	values = {'name' : 'Virginia Cwealth',
          'location' : 'Richmond',
          'language' : 'Python' }    
	headers = { 'User-Agent' : user_agent }

	data = urllib.parse.urlencode(values).encode("utf-8")
	req = urllib.request.Request(url_input, data, headers)
	#THIS IS WHERE WE ARE STUCK!

	response = request(req)
	the_page = response.read()

	page_soup = soup(the_page, "html.parser")

	product_name = page_soup.findAll("span", {"class":"product-link link-highlight"},{"itemprop":"name"})
	print(product_name)
	break
		

	# if product_name is not empty:
	# 	product_name = product_name[0].text.strip()
	
	# gradeA = page_soup.findAll("div",{"class":"grade-rating font-grade-a"})
	# gradeB = page_soup.findAll("div",{"class":"grade-rating font-grade-b"})
	# gradeC = page_soup.findAll("div",{"class":"grade-rating font-grade-c"})
	# gradeD = page_soup.findAll("div",{"class":"grade-rating font-grade-d"})
	# gradeF = page_soup.findAll("div",{"class":"grade-rating font-grade-f"})	
	
	# if gradeA is not None and gradeA is not empty_array and len(gradeA) > 0:
	# 	grade = gradeA[0].text.strip()

	# if gradeB is not None and gradeB is not empty_array and len(gradeB) > 0:
	#  	grade = gradeB[0].text.strip()
	
	# if gradeC is not None and gradeC is not empty_array and len(gradeC) > 0:
	#  	grade = gradeC[0].text.strip()

	# if gradeD is not None and gradeD is not empty_array and len(gradeD) > 0:
	# 	grade = gradeD[0].text.strip()

	# if gradeF is not None and gradeF is not empty_array and len(gradeF) > 0:
	#  	grade = gradeF[0].text.strip()


	# percentage_scoreA = page_soup.findAll("b",{"class":"font-grade-a"})
	# percentage_scoreB = page_soup.findAll("b",{"class":"font-grade-b"})
	# percentage_scoreC = page_soup.findAll("b",{"class":"font-grade-c"})
	# percentage_scoreD = page_soup.findAll("b",{"class":"font-grade-d"})
	# percentage_scoreF = page_soup.findAll("b",{"class":"font-grade-f"})
	
	# if percentage_scoreA is not None and percentage_scoreA is not empty_array and len(percentage_scoreA) > 0:
	# 	percentage_score = percentage_scoreA[0].text.strip()

	# if percentage_scoreB is not None and percentage_scoreB is not empty_array and len(percentage_scoreB) > 0:
	#  	percentage_score = percentage_scoreB[0].text.strip()

	# if percentage_scoreC is not None and percentage_scoreC is not empty_array and len(percentage_scoreC) > 0:
	# 	percentage_score = percentage_scoreC[0].text.strip()

	# if percentage_scoreD is not None and percentage_scoreD is not empty_array and len(percentage_scoreD) > 0:
	# 	percentage_score = percentage_scoreD[0].text.strip()

	# if percentage_scoreF is not None and percentage_scoreF is not empty_array and len(percentage_scoreF) > 0:
	#  	percentage_score = percentage_scoreF[0].text.strip()

	f1.write("product_name" + "," + "Grade" + "," + "PercentageScore" + "," + "Users" + "," + URL + "\n")

f1.close()
