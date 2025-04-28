# Beginning: create variables
basketball_points = 0
football_points = 0

# Middle: Ask questions
# question 1:
answer = input("in basketball or football would you rather A) dunk on somebody, or B) moss somebody?/n")
if answer == "A":
    basketball_points += 1
elif answer == "B":
    football_points += 1

# question 2:
answer = input("in basketball or football would you rather A) throw a lob, or B) throw a touchdown?/n")
if answer == "A":
    basketball_points += 1
elif answer == "B":
    football_points += 1

#question 3:
answer = input("in basketball or football would you rather A) get an interception, or B) get a block?/n")
if answer == "A":
    football_points += 1
elif answer == "B":
    basketball_points += 1

#question 4:
answer = input("in basketball or football would you rather A) cross somebody, or B) juke somebody?/n")
if answer == "A":
    basketball_points += 1
elif answer == "B":
    football_points += 1

#question 5:
answer = input("in basketball or football would you rather A) throw an interception, or B) throw a turnover?/n")
if answer == "A":
    football_points += 1
elif answer == "B":
    basketball_points += 1

if basketball_points > football_points:
    print("You are a basketball person")
elif football_points > basketball_points:
    print("You are a basketball person")
elif basketball_points == football_points:
    print("You like basketball and football the same")