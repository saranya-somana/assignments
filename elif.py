sp=100
cp=100
if (sp>cp):
    print("COngratulations!")
    print("You made a profit of ", sp-cp,"bucks")
elif (cp>sp):
    print("Oops!")
    print("You made a loss of ", cp-sp,"bucks")
else:
    print("You didn't make or loose money.")
