#the user is able to add questions and answers 
def main():
    #each subject will have its own area
    suba = {}
    subb = {}
    subc = {}

    while True:
        score = 0
        print("which subject would you like to study? ")
        start = input("a,b,c ")
        if start.lower() == "a":
            action = input("would you like to quiz or add? ")
            if action.lower() == "quiz":
                for x in suba:
                    print(x)
                    answert = input("whats your guess? ")
                    print(suba[x])
                    if answert == suba[x]:
                        score =+ 1
                print(score)
            elif action.lower() == "add":
                question = input("Question you would like to add? ")
                answer = input("The Answer? ")
                suba.update({question : answer})
        elif start.lower() == "b":
            action = input("would you like to quiz or add? ")
            if action.lower() == "quiz":
                for x in subb:
                    print(x)
                    answert = input("whats your guess? ")
                    print(subb[x])
                    if answert == subb[x]:
                        score =+ 1
                print(score)
            elif action.lower() == "add":
                question = input("Question you would like to add? ")
                answer = input("The Answer? ")
                subb.update({question : answer})
        elif start.lower() == "c":
            action = input("would you like to quiz or add? ")
            if action.lower() == "quiz":
                for x in subc:
                    print(x)
                    answert = input("whats your guess? ")
                    print(subc[x])
                    if answert == subc[x]:
                        score =+ 1
                print(score)
            elif action.lower() == "add":
                question = input("Question you would like to add? ")
                answer = input("The Answer? ")
                subc.update({question : answer})

#the user will say the difficulty of each questuion

#when testing on a quiz of a subject they will be random

#BONUS if that works see if you can make it so that questions that they struggle are introduced more oftern.


main()