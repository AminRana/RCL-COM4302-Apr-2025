#Week 4
#Exercise 1
#Write a program to to calculate total 1 to 8
word=input ("Write any word in English :").lower()

for x in word:
    if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
        print (x, "Yes, it is a vowel.")

    else:
        print (x, "Sorry, it is not vowel")
