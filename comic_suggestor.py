import requests


image_title = []
page_number = []

# here I'm only requesting 15 pages for the test purpose.
for i in range(1, 15):
	response = requests.get('https://xkcd.com/' + str(i) + "/" + 'info.0.json')

	#print response.json()["title"], response.json()["num"]
	image_title.append(str(response.json()["title"]))
	page_number.append(response.json()["num"])


finalDict = {}
for title, page in zip(image_title, page_number):
	for word in title.split(" "):
        	if word not in finalDict.keys():
            		finalDict[word] = [int(page)]
	    	
        	else:
            		finalDict[word] += [int(page)]
	    		

print finalDict


# checking entered user's words exist or not, if exists then return pages
user_words = raw_input("Enter text to filter images from XKCD: ").split(' ')
page_list = []

def search_words(words_list):
	global page_list
	for word in finalDict:	
		for i in user_words:			
			if i in finalDict:	
				page_list += finalDict[i]	
				
		return list(set(page_list))
	
		

print "pages:", search_words(user_words)

