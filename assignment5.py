# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 22:15:17 2022

@author: temel
"""

def count_letter_e(loc, count_accented = True, count_uppercase = True):

	# Open and read the file
	with open(loc+".txt", encoding = "utf-8") as test_file:
		text = test_file.read()

		# List of all e's to look for
		e_list = ['e', 'é', 'ê', 'è', 'E', 'É', 'Ê', 'È']

		# Create a dictionary with all e counts
		letter_counts = {}

		for e in e_list:
			letter_counts[e] = text.count(e)

		# Variable that will return the desired integer
		sum_counts = 0

		# Get counts according to conditions given
		if count_uppercase and count_accented:
			for e in e_list:
				sum_counts += letter_counts[e]

		elif count_accented == True and count_uppercase == False:
				to_count = e_list[0:4]
				for e in to_count:
					sum_counts += letter_counts[e]

		elif count_accented == False and count_uppercase == True:
				sum_counts += letter_counts['e']
				sum_counts += letter_counts['E']

		elif count_uppercase == False and count_accented == False:
				sum_counts += letter_counts['e']

		return(sum_counts)

# Test Case # 1
file_name = "pride"
pride_TT = count_letter_e(file_name, True, True)
pride_TF = count_letter_e(file_name, True, False)
pride_FT = count_letter_e(file_name, False, True)
pride_FF = count_letter_e(file_name, False, False)
print(pride_TT)
print(pride_TF)
print(pride_FT)
print(pride_FF)
print()

# Test Case # 2
file_name = "lenlevement"
lenlevement_TT = count_letter_e(file_name, True, True)
lenlevement_TF = count_letter_e(file_name, True, False)
lenlevement_FT = count_letter_e(file_name, False, True)
lenlevement_FF = count_letter_e(file_name, False, False)
print(lenlevement_TT)
print(lenlevement_TF)
print(lenlevement_FT)
print(lenlevement_FF)
print()

# Test Case # 3 (Our sentences)
file_name = "count_e_1"
count_e_1_TT = count_letter_e(file_name, True, True)
count_e_1_TF = count_letter_e(file_name, True, False)
count_e_1_FT = count_letter_e(file_name, False, True)
count_e_1_FF = count_letter_e(file_name, False, False)
print(count_e_1_TT)
print(count_e_1_TF)
print(count_e_1_FT)
print(count_e_1_FF)

# Test Case # 4 (Our sentences)
file_name = "count_e_1"
count_e_2_TT = count_letter_e(file_name, True, True)
count_e_2_TF = count_letter_e(file_name, True, False)
count_e_2_FT = count_letter_e(file_name, False, True)
count_e_2_FF = count_letter_e(file_name, False, False)
print(count_e_2_TT)
print(count_e_2_TF)
print(count_e_2_FT)
print(count_e_2_FF)

# Test Case # 5 (Our sentences)
file_name = "count_e_1"
count_e_3_TT = count_letter_e(file_name, True, True)
count_e_3_TF = count_letter_e(file_name, True, False)
count_e_3_FT = count_letter_e(file_name, False, True)
count_e_3_FF = count_letter_e(file_name, False, False)
print(count_e_3_TT)
print(count_e_3_TF)
print(count_e_3_FT)
print(count_e_3_FF)

# Test Case # 6 (Our sentences)
file_name = "count_e_1"
count_e_4_TT = count_letter_e(file_name, True, True)
count_e_4_TF = count_letter_e(file_name, True, False)
count_e_4_FT = count_letter_e(file_name, False, True)
count_e_4_FF = count_letter_e(file_name, False, False)
print(count_e_4_TT)
print(count_e_4_TF)
print(count_e_4_FT)
print(count_e_4_FF)

###
#Exercise 2: Pride and Prejudice Sentence Statistics
###

import string
def collect_statistics(loc):
    '''
    Function to determine the number of words in and average word length of each sentence of a text.
    The data are saved to a csv file.

    Input:
    - loc -- a string that is a file name, may or may not include '.txt' extentions
    - output_file -- a string that is a file name, may or may not include '.csv' extension

    Output:
    - None

    You should call your filename checker on the input strings.
    You might also want to break this long function into several smaller ones.
    Note that each row of the csv file will correspond to a sentence.
    Each row will have two columns, the first of which will contain the
    number of words, the second will contain the average word length.
    '''
from urllib import request
url = "http://www.gutenberg.org/files/1342/1342-0.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')  # reads all the bytes of the file in utf-8 format, a form of Unicode
    
    
    # Open and read text file
    #with open("pride.txt", encoding = "utf-8") as text_file:
        #text = tex_file.read()

    # Get rid of Chapter headers
for n in range(62):
        text = text.replace(f"Chapter {i}", "")

    # Get rid of Mrs. abbreviation
text.replace("Mrs.","Mrs")

    # Get rid of punctuation non-enders removed,
    # question marks replaced with periods
for p in string.punctuation:
        if p not in  "?.!":
            text = text.replace("",p)
        elif p == "?":
            text = text.replace("?",".")

    # Get rid of em-dash
text = text.replace('--',' ')

    # Split text into sentences
sents = text.split(".")

    # Loop through sentences
for i in len(sents):
        # Split sentence into words
        s = sents[i].split()
        num_chars = 0
        # Count total characters of words in sentences
        for j in len(s):
            num_chars += len(s[j])
        num_words = len(s)
        # Add data to list
        pride_count(i)=[num_words,num_chars]
    header = ['Word Count', "Average Characters"]
    # Write the rows to the csv file
    with open(output_file, "r", newline="") as pride_out:
    writer = csv.writer(output_file, delimiter=",")
    writer.writerow(i for i in header)
    writer.writerows(map(lambda x: [x],pride_count))
    return None
