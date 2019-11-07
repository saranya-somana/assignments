char=input()
if ord(char)>=65 and ord(char)<=90:
    print("You entered an uppercase alphabet")
    if char in ['A', 'E', 'I', 'O', 'U']:
        print("You entered an vowel")
    else:
        print("You entered a consonant")
elif ord(char)>=97 and ord(char)<=122:
    print("You entered a lowercase alphabet")
    if char in ['a', 'e', 'i', 'o', 'u']:
        print("Yau entered an vowel")
    else:
        print("You entered a consonant")
else:
    print("The entered character is not a alphabet")
