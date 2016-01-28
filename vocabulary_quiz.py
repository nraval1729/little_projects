import requests
from bs4 import BeautifulSoup
from random import shuffle

print "Getting your vocabulary superpowers ready....."
print

page = requests.get('https://www.randomlists.com/random-vocabulary-words', verify=False)   #get the randomlists page, timeout after 3 seconds

soup = BeautifulSoup(page.content)


list_of_word_tags = soup.find_all("span", class_ = "support")           #list of tags corresponding to the words

list_of_meaning_tags = soup.find_all("span", class_ = "subtle")         #list of tags corresponding to the meanings / definitions


words = []
meanings = []
word_option = ["a", "b", "c", "d", "e"]
meaning_option = ["p", "q", "r", "s", "t"]

# word_meaning_dict = {}
answer_list = ["ap", "bq", "cr", "ds", "et"]	


for word_tag, option in zip(list_of_word_tags, word_option):
	words.append((str(word_tag.string), option))

for meaning_tag, option in zip(list_of_meaning_tags, meaning_option):
	meanings.append((str(meaning_tag.string), option))


shuffle(words)          #shuffle them but remember the answers
shuffle(meanings)
fmt = '{:<1}) {:<25}{:<1}) {}'  #fancy printing

for word_tuple, meaning_tuple in zip(words, meanings):
	print (fmt.format(word_tuple[1], word_tuple[0], meaning_tuple[1], meaning_tuple[0]))

print 
print "Choose (word, meaning) tuple like so: "
print "If word's option is 'a', and its meaning's option is 's', your input should be 'as' (without the quotes)"
print "Enter 5 such inputs"
print

input_tuple_list = []
correct = 0

for input_num in range(0, 5):
	input_tuple = raw_input()
	input_tuple_list.append(input_tuple)

for input_tuple in input_tuple_list:
	if input_tuple in answer_list:
		print input_tuple, " is correct!"
		correct += 1
	else:
		print input_tuple, " is incorrect!"

print
print "Your score: ", correct, "/ 5 "