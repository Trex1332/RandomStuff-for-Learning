#the user is able to add questions and answers 
def main():
    suba = {"what time is it?": "idk",}
    subb = {}
    subc = {}

    while True:
        score = 0
        print("which subject would you like to study? ")
        start = input("a,b,c")
        if start.lower() == "a":
            for x in suba:
                print(x)
                answert = input("whats your guess? ")
                print(suba[x])
                if answert == suba[x]:
                    score =+ 1
            print(score)

            
#each subject will have its own area

#the user will say the difficulty of each questuion

#when testing on a quiz of a subject they will be random

#BONUS if that works see if you can make it so that questions that they struggle are introduced more oftern.

main()