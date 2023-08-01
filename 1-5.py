#prime or not 1a
def isprime(num):
    for i in range(2, int(num/2)+1):
        if num % i == 0: 
              return False;
    return True;

num = int(input("enter the number"));
if (isprime(num)) : 
     print(num , " is prime")
else : 
     print(num , " is not prime")

################################

#cal the sum of all even nums from an arr 1b
def even_num_sum(arr):
    sum = 0
    for i in arr:
        if i % 2 == 0:
            sum += i
    return sum;

arr  = []
num = int(input("enter the number of elements in the array"))
for i in range(num):
    element = int(input(f"enter the {i}th element in the array"));
    arr.append(element)

print("sum of all even nums from")
print(even_num_sum(arr));

##############################################

#fibonacci series 2a

def fib(n):
    if n== 0: return 0
    elif n== 1: return 0
    elif n==2: return 1
    else: return fib(n-1)+fib(n-2)

num = int(input("enter the number"))
for i in range(num):
    print(fib(i))

    ################################################

    #find the maximum value from the list 2b

arr = []
num = int(input("enter the length of the arr"))
for i in range(num):
    element = int(input("enter the element"))
    arr.append(element)

print(max(arr))


##############################################

#counting the number of occurence of a word in a sentence 3a

def countWord(sentence, word):
    sentence = sentence.lower()
    word = word.lower()
    words = sentence.split()
    count = words.count(word)
    return count

sentence = input('Sentence')
word = input('Word')
print(countWord(sentence, word))

##############################################

#comparing two strings 3b
def compare(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    set1 = set(str1)
    set2 = set(str2)

    intersection = set1.intersection(set2)
    union = set1.union(set2)

    ratio = len(intersection)/len(union)
    return ratio


str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
ratio = compare(str1, str2)
print(ratio)

##############################################

#4a
nums = []
n = int(input("enter the length of the arr"))
for i in range(n):
    ele = int(input("enter the num"))
    nums.append(ele)
print(sum(nums))

##############################################  
#word count in a sentence 4b
from collections import Counter

def count_words(sentence):
    sentence = sentence.lower()
    words = sentence.split()
    word_count = Counter(words)
    return word_count

sentence = input("Enter a sentence: ")
word_count = count_words(sentence)
for word, count in word_count.items():
    print(f"{word} : {count}")

##############################################  

#filter out words that start with a particular prefix 5a

def filter(sentence, prefix):
    sentence = sentence.lower()
    prefix = prefix.lower()
    words = sentence.split()

    filtered_words = []
    for word in words:
        if word.startswith(prefix):
            filtered_words.append(word)

    return filtered_words

sentence = input('Sentence')
prefix = input('Prefix')
filterWords = filter(sentence, prefix)
for word in filterWords:
    print(word)

    ################################################

    #extract email 5b
import re
def extract_email(sent_email):
    pattern = r'\b[A-Za-z0-9._]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    email_address = re.findall(pattern, sent_email)
    return email_address

sent_email = input('Enter email address')
extract_email = extract_email(sent_email)

print(extract_email)
