print("Welcome to my fashion quiz!")

playing = input("Do you want to play? ")


if playing.lower() != "yes":
    quit()
print("Okay! Let's play : ) ")
score = 0
answer= input("What does JPG stands for? ")
if answer.lower() == "jean paul gaultier":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who was the creative director for Chanel until his death?  ")
if answer.lower() == "karl lagerfeld":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What british actress is the birkin bag name after ? ")
if answer.lower() == "jane birkin":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who is the founder of Off-White? ")
if answer == "virgil abloh":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What fashion house collaborated with H&M in 2015? ")
if answer.lower() == "balmain":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " +  str(score) +  " questions correct!")
print("You got " +  str((score / 5)* 100) +  "%.")

