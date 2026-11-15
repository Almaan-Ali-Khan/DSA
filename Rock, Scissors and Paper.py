#This code uses random library and creates a random outcome for first person named Alice, and then a code runs where Bob plays, the match continues until Bob doesn't wins or draws the entire match
import random as r

t = int(input())


while t != 0:

    #for alice
    x = int(input("Number of times Alice will play Rock:"))
    y = int(input("Number of times Alice will play Scissors:"))
    z = int(input("Number of times Alice will play Paper:"))

    num_rounds = x + y + z
    total_rounds = num_rounds
    x = "R"*x
    y = "S"*y
    z = "P"*z

    outcome = x+y+z
    outcome_a = "".join(r.sample(outcome, len(outcome)))
    won_a = 0
    won_b = 0
    while won_b >= won_a:
        #for bob
        choices = "RPS"
        num_rounds = total_rounds
        a = num_rounds
        outcome_b = ""
        while (a != 0):
            outcome_b += r.choice(choices)
            a -= 1

        # matches


        while (num_rounds != 0):
            if (outcome_b[num_rounds-1] == outcome_a[num_rounds-1]):
                num_rounds -= 1
            elif (outcome_b[num_rounds-1] == "R" and outcome_a[num_rounds-1] == "P") or (outcome_b[num_rounds-1] == "P" and outcome_a[num_rounds-1] == "S") or (outcome_b[num_rounds-1] == "S" and outcome_a[num_rounds-1] == "R"):
                won_a += 1
                num_rounds -= 1
            elif (outcome_b[num_rounds-1] == "P" and outcome_a[num_rounds-1] == "R") or (outcome_b[num_rounds-1] == "S" and outcome_a[num_rounds-1] == "P") or (outcome_b[num_rounds-1] == "R" and outcome_a[num_rounds-1] == "S"):
                won_b += 1
                num_rounds -= 1


    t -= 1
    print (outcome_b)
    print (won_a)
    print (won_b)
