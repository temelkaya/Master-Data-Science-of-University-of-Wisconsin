# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 23:18:11 2022

@author: temel
"""

#TASK2
#Subtask 2.1 Reverse

my_tuple= (1,1,1,1,1,9,7,2) #My birthday
reversed_my_tuple=my_tuple[::-1]
print(my_tuple)
print(reversed_my_tuple)

#Subtask 2.2 Content Swap

tuple1=(1,1,2,3,5,8,13)
tuple2=("a","b","c","d")
print(tuple1)
print(tuple2)
tuple1, tuple2 = tuple2, tuple1
print(tuple1)
print(tuple2)

#TASK3
#Subtask 3.1: Counting letters

txt = "I meet so many ambitious young politicians and leaders who want to jump to the head of the line. They do not know how we arrived at this point in our history as a nation, but they believe they should be appointed to lead us into the future. They think that because they are educated, articulate, and talented someone should usher them down the red carpet to a throne of leadership. But real leaders are not appointed. They emerge out of the masses of the people and rise to the forefront through the circumstances of their lives. Either their inner journey or their human experience prepares them to take that role. They do not nominate themselves. They are called into service by a spirit moving through a people that points to them as the embodiment of the cause they serve."

letter_counts = [0]*52
letter_counts_ignore_case = [0]*26

small_letter_status = [0]*26
capital_letter_status = [0]*26


for x in txt:
  if x>='a' and x<='z':
    small_letter_status[ord(x)%ord('a')] += 1
  elif x>='A' and x<='Z':
            capital_letter_status[ord(x)%ord('A')] += 1

print("\nSmall Letter status")
for x in range(len(small_letter_status)):
  print("Count of ", chr(x+(ord('a'))), ' = ', small_letter_status[x])


print("\nCapital Letter status")
for x in range(len(capital_letter_status)):
  print("Count of ", chr(x+(ord('A'))), ' = ', capital_letter_status[x])


small_letter_status = [0]*26

full_lower_case = txt.lower()

for x in full_lower_case:
  if x>='a' and x<='z':
    small_letter_status[ord(x)%ord('a')] += 1

print("\nTotal letter counts:")
for x in range(len(small_letter_status)):
  print("Count of ", chr(x+(ord('a'))), ' = ', small_letter_status[x])

#Subtask 3.2: Average word length
average_word_length = 0
total_word_length = 0
number_of_words = 0

words = txt.split()

for word in words:
  letter_count = 0
  for x in word:
    if (x>='A' and x<='Z') or (x>='a' and x<='z') or (x>='0' and x<='9'):
      letter_count += 1
  
  total_word_length += letter_count
  number_of_words +=1
average_word_length = (total_word_length/number_of_words)

print("Average word length = {:.2f}".format(average_word_length))


#Subtask 3.3: Unique words
words = (txt.lower()).split()
num_unique_words = 0 

unique_words = set({})

for x in words:
  unique_words.add(x)

num_unique_words = len(unique_words)


print("\nNumber of unique words = ", num_unique_words)


words.sort(reverse=True, key= lambda x: len(x))

#Subtask 3.4: Longest word
longest_words = []

longest_words.append(words[0])

for x in range(1, len(words)):
  if len(words[x]) == len(longest_words[0]):
    longest_words.append(words[x])
  else:
    break

print("\nLongest word(s):")
print(longest_words)

#TASK4
import csv
input_file = csv.DictReader(open("airport.csv"))
airports = []
for row in input_file:
    airports.append(row)

#Subtask 4.1: Import a csv and converting numerical values to correct data type
for airport in airports:
    for key in ['Scheduled Departures', 'Performed Departures', 'Passengers']:
        airport[key] = int(airport[key])
    for key in ['Freight (tons)', 'Mail (tons)']:
        airport[key] = float(airport[key])


#Subtask 4.2: Scheduled vs Actual Departures
less_scheduled = []
for airport in airports:
    if airport['Scheduled Departures'] < airport['Performed Departures']:
        less_scheduled.append(airport)


#Subtask 4.3: Mean of a Subset
total_pass = 0
for airport in less_scheduled:
    total_pass += airport['Passengers']
mean_pass = total_pass / len(less_scheduled)