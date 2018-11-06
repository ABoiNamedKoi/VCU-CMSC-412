from urllib.request import urlopen as request
from bs4 import BeautifulSoup as soup
import sys
filename = "info@amazon&fakespot.csv"
f = open(filename, "a+")

headers = "ProductName,Grade,PercentageScore,Users,AmazonURL,FakeSpotURL\n"
f.write(headers)
print("----------------------------------------------------------------------------")
print("welcome to the fakespot.com data scraper.\n")

url_input = input("input fakespot review report url |OR| input" + " 'q' " + "to quit the program.\n");

if url_input == 'q' or url_input == "q" or url_input == 'Q' or url_input == "Q" :
		print("...exiting!")
		sys.exit()
while url_input != 'q' or url_input != "q" or url_input != 'Q' or url_input != "Q" :
		
		#url_input = input("input fakespot review report url |OR| input" + " 'q' " + "to quit the program.\n");
		if url_input == 'q' or url_input == "q" or url_input == 'Q' or url_input == "Q" :
			print("...exiting!")
			sys.exit()

		url = url_input
		# opening up connection, grabbing the page
		client = request(url)
		page = client.read()
		client.close()

		# html parser
		page_soup = soup(page, "html.parser")

		# grabs fakespot review grades based on if it has that certain grade
		try:
			empty = ''
			empty_array = []
			product_name = page_soup.findAll("span", {"class":"product-link link-highlight"},{"itemprop":"name"})
			if product_name is not empty:
				product_name = product_name[0].text.strip()


			gradeA = page_soup.findAll("div",{"class":"grade-rating font-grade-a"})
			gradeB = page_soup.findAll("div",{"class":"grade-rating font-grade-b"})
			gradeC = page_soup.findAll("div",{"class":"grade-rating font-grade-c"})
			gradeD = page_soup.findAll("div",{"class":"grade-rating font-grade-d"})
			gradeF = page_soup.findAll("div",{"class":"grade-rating font-grade-f"})	
			
			if gradeA is not None and gradeA is not empty_array and len(gradeA) > 0:
				grade = gradeA[0].text.strip()

			if gradeB is not None and gradeB is not empty_array and len(gradeB) > 0:
			 	grade = gradeB[0].text.strip()
			
			if gradeC is not None and gradeC is not empty_array and len(gradeC) > 0:
			 	grade = gradeC[0].text.strip()

			if gradeD is not None and gradeD is not empty_array and len(gradeD) > 0:
				grade = gradeD[0].text.strip()

			if gradeF is not None and gradeF is not empty_array and len(gradeF) > 0:
			 	grade = gradeF[0].text.strip()


			percentage_scoreA = page_soup.findAll("b",{"class":"font-grade-a"})
			percentage_scoreB = page_soup.findAll("b",{"class":"font-grade-b"})
			percentage_scoreC = page_soup.findAll("b",{"class":"font-grade-c"})
			percentage_scoreD = page_soup.findAll("b",{"class":"font-grade-d"})
			percentage_scoreF = page_soup.findAll("b",{"class":"font-grade-f"})
			
			if percentage_scoreA is not None and percentage_scoreA is not empty_array and len(percentage_scoreA) > 0:
				percentage_score = percentage_scoreA[0].text.strip()

			if percentage_scoreB is not None and percentage_scoreB is not empty_array and len(percentage_scoreB) > 0:
			 	percentage_score = percentage_scoreB[0].text.strip()

			if percentage_scoreC is not None and percentage_scoreC is not empty_array and len(percentage_scoreC) > 0:
				percentage_score = percentage_scoreC[0].text.strip()

			if percentage_scoreD is not None and percentage_scoreD is not empty_array and len(percentage_scoreD) > 0:
				percentage_score = percentage_scoreD[0].text.strip()

			if percentage_scoreF is not None and percentage_scoreF is not empty_array and len(percentage_scoreF) > 0:
			 	percentage_score = percentage_scoreF[0].text.strip()

			
			f.write(product_name + "," + grade + "," + percentage_score + "," + "User" + "," + "AmazonURL" + "," + url_input +"\n")
			#f.write(product_name + "," + grade + "," + percentage_score)
		
			url_input = input("\ninput fakespot review report url |OR| input" + " 'q' " + "to quit the program.\n");
			

		except: "fakespot scrape failed!"
f.close()