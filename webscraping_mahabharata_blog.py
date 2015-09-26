#!/bin/python

from BeautifulSoup import BeautifulSoup
import urllib2
from urllib import urlopen
import re
import os

#Get all the chapter links from the table-of-contents page
url = "https://themahabharata.quora.com/The-Mahabharata-A-Retelling"
html_page = urllib2.urlopen(url)
soup = BeautifulSoup(html_page)

allLinks = soup.findAll( 'a', attrs={'href' : re.compile("^http://themahabharata.quora.com/")} )

links=[]
titles=[]
for link in allLinks : 
	links.append(link['href']) 
	titles.append(link.string)

#Make a directory to store all the output files
DIR_NAME = "Mahabharata_A_Retelling"
if not os.path.exists(DIR_NAME):
    os.makedirs(DIR_NAME);

#Skip the first & last links, they are not related to the chapters.
totalLinks = len(links)
patFinder = re.compile( '<hr class="qtext_hr" />(.*)<hr class="qtext_hr" />' )

for i in range(1, totalLinks-1) :
	page=urlopen(links[i]).read()

        title = titles[i].replace(" ", "_")
	print title

	textList = re.findall(patFinder, page)

        #Convert the list type into string. Replace some of the special characters
        #by normal characters
	textString = ''.join(textList)
	textString = textString.replace("&quot;", "\"")
	textString = textString.replace("&#039;", "'")
	textString = textString.replace("<br />", "\n")
	textString = textString.replace("<i>", "")
	textString = textString.replace("</i>", "")

	markerString = "---------------------"
	fileName = DIR_NAME + "/" + title + ".txt"

	text_file = open(fileName, "w")

	text_file.write(titles[i] + "\n")
	text_file.write(markerString + "\n" ) 
	text_file.write(textString)
	text_file.close()

#TODO : 
#The o/p should be in pdf format.
#Put this code on some cloud to run.
