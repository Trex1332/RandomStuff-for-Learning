import random
 


def main():
    questions = {"cats":{"Question": "What is the king of the jungle? a: Lion, b: sea lion, c tiger: ","Answer": "c", "a":"Lion", "b": "sea lion", "c": "tiger" },
    "dogs": {"Question": "What dog heards sheep? a: German Shepard, b: wolf, c: Border Collie ","Answer": "c", "a":"German Shepard", "b": "wolf", "c": "Border Collie" }}
    already = set()
    lengthofquiz = len(questions)
    score = 0
    for x in range(lengthofquiz):
        quiz_category = randomquestion(questions)

        while quiz_category in already:
            quiz_category = randomquestion(questions)

        already.add(quiz_category)

        quiz = questions[quiz_category]
        print(quiz["Question"])
        answet = input("guess a,b or c? ").lower()
        print(answet)
        if answet == quiz["Answer"]:
            print("correct it was",quiz["Answer"] )
            score += 1
        else:
            print("wrong")
    print("Your Score was ", score)

def randomquestion(b):
    quiz_category = random.choice(list(b.keys()))
    return quiz_category

main()