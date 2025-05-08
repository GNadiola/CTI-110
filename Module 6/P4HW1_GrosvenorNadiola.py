# Nadiola Grosvenor
# 4/24/2025
# P4Lab2
# program is to display a letter grade for the calculated average.

score_num = int(input("How many scores do you want to enter? "))
print()

# list
scores = []
for num in range(1, score_num + 1):
    score = float(input("Enter score #" + str(num)+ ":"))
    while score < 0 or score > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input("Enter score #"+ str(num)+ " again:"))

    scores.append(score)
    print()

    #low score calculation
lowest = min(scores)
scores_modified = scores
scores_modified.remove(lowest)
avg = sum(scores_modified)/len(scores_modified)

# grades from prev code

if avg >= 90:
    print('Your grade is: A')

elif avg >= 80:
         print('Your grade is: B')

elif avg >= 70:
         print('Your grade is: C')

elif avg >= 60:
         print('Your grade is: D')
else:  
    print('Your grade is: F') 
