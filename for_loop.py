count=0
print("Enter your name:")
name=input()
for letter in name:
    if (letter in ['A','E','I','O','U','a','e','i','o','u']):
        count+=1
print("You have ", count ," Vowels in your name")
