import random
from collections import Counter

def getResponse():
  return input()

def doRoll(c):
  c = []
  for x in range(5):
    c.append(random.randint(1,6))
  return c

def printRoll(c):
  for x in range(4):
    print(c[x],", ",sep="",end="")
  print(c[4],".",sep="")

def correctResponseLoop(putin=''):
  acceptable = ["reroll","score"]
  j = 0
  while putin.lower() not in acceptable:    
    if j > 0:
      print()
      print("That didn't make sense. Try again.")
    putin = getResponse()
    j = 1
  return putin.lower()

def getRerollIndex(i):
  acceptable = ["1", "2", "3", "4", "5", "6"]
  i = list(i)
  a = 0
  for x in range(len(i)):
    spot = x - a
    if i[spot] in acceptable:
      i[spot] = int(i[spot]) - 1
    else:
      del i[spot]
      a += 1
  return i

def doReroll(c,i):
  for x in range(len(i)):
    c[i[x]] = random.randint(1,6)
  return c

def correctMethodLoop(l):
  acceptable = l
  j = 0
  putin = ''
  while putin not in acceptable:
    if j > 0:
      print("That's not available. Try again.")
      print()
    putin = getResponse()
    j = 1
  return putin

def getUpperScore(m,c):
  d = 0
  score = 0
  if m == "Aces":
    d = 1
  if m == "Twos":
    d = 2
  if m == "Threes":
    d = 3
  if m == "Fours":
    d = 4
  if m == "Fives":
    d = 5
  if m == "Sixes":
    d = 6
  for x in range(len(c)):
    if c[x] == d:
      score += d
  return score

def get3Kind(c):
  goodScore = 0
  score = 0
  for x in range(len(c)):
    if Counter(c)[x+1] >= 3:
      goodScore = 1
      break
  if goodScore == 0:
    return score
  if goodScore == 1:
    for x in range(len(c)):
      score += c[x]
    return score

def get4Kind(c):
  goodScore = 0
  score = 0
  for x in range(len(c)):
    if Counter(c)[x+1] >= 4:
      goodScore = 1
      break
  if goodScore == 0:
    return score
  if goodScore == 1:
    for x in range(len(c)):
      score += c[x]
    return score

def getSmallS(c):
  c = list(dict.fromkeys(c))
  c.sort()
  if len(c) >= 4:
    if c[1]-c[0] == 1 and c[2]-c[1] == 1 and c[3]-c[2] == 1:
      score = 30
    elif len(c) == 5:
      if c[2]-c[1] == 1 and c[3]-c[2] == 1 and c[4]-c[3] == 1:
        score = 30
    else:
      score = 0
  else:
    score = 0
  return score

def getLargeS(c):
  c = list(dict.fromkeys(c))
  c.sort()
  if len(c) == 5:
    if c[1]-c[0] == 1 and c[2]-c[1] == 1 and c[3]-c[2] == 1 and c[4]-c[3] == 1:
      score = 40
    return score
  else:
    score = 0
  score = 0
  return score

def getFullHouse(c):
  c.sort()
  occurrenceList = []
  for x in range(6):
    if c.count(x + 1) == 2 or c.count(x + 1) == 3:
      occurrenceList.append(c.count(x + 1))
  occurrenceList.sort()
  if occurrenceList == [2,3]:
    score = 25
    return score
  else:
    score = 0
    return score

def getYahtzee(c):
  goodScore = 0
  score = 0
  for x in range(len(c)):
    if Counter(c)[x] == 5:
      goodScore = 1
      break
  if goodScore == 0:
    return score
  if goodScore == 1:
    score = 50
    return score

def getChance(c):
  score = 0
  for x in range(5):
    score += c[x]
  return score
    

def getScore(m,c):
  if m in ["Aces","Twos","Threes","Fours","Fives","Sixes"]:
    addScore = getUpperScore(m,c)
    return addScore
  elif m == "3 of a kind":
    addScore = get3Kind(c)
    return addScore
  elif m == "4 of a kind":
    addScore = get4Kind(c)
    return addScore
  elif m == "Small Straight":
    addScore = getSmallS(c)
    return addScore
  elif m == "Large Straight":
    addScore = getLargeS(c)
    return addScore
  elif m == "Full House":
    addScore = getFullHouse(c)
    return addScore
  elif m == "Yahtzee":
    addScore = getYahtzee(c)
    return addScore
  elif m == "Chance":
    addScore = getChance(c)
    return addScore

def getBonusYahtzee(c):
  score = 0
  if getYahtzee(c) == 50:
    score = 100
    print("Another Yahtzee! 100 points will be added to your total.")
  return score


i = 0
scoreUpper = 0
scoreLower = 0
yahtzeeBonus = 0
currentRoll = []
scoreList = ["Aces", "Twos", "Threes", "Fours", "Fives", "Sixes","3 of a kind","4 of a kind","Small Straight","Large Straight","Full House","Yahtzee","Chance"]
scoreListAvailable = ["Aces", "Twos", "Threes", "Fours", "Fives", "Sixes","3 of a kind","4 of a kind","Small Straight","Large Straight","Full House","Yahtzee","Chance"]
scoreListUnavailable = ["","","","","","","","","","","","",""]
scoreHistory = ["","","","","","","","","","","","",""]

while scoreListAvailable != []:
  currentRoll = doRoll(currentRoll)
  
  if i == 0:
    print()
    print("Welcome to Yahtzee! Below is your first roll. Reroll or Score?")
  if i > 0:
    print()
    print("Here is your new roll. Reroll or Score?")
  printRoll(currentRoll)
  print()
  
  response = correctResponseLoop()
  print("You chose to",response.lower()+".")
  rerollCount = 0
  listmessage = 0
  while response in ["reroll"]:
    rerollCount += 1
    print("Indicate which dice you would like to reroll. e.g., if you want to reroll the third and fifth dice, type '3,5'.")
    rerollInput = getResponse()
    rerollIndex = getRerollIndex(rerollInput)
    currentRoll = doReroll(currentRoll,rerollIndex)
    if rerollCount < 2:
      print()
      print("Here is your current roll. Reroll again or Score?")
      printRoll(currentRoll)
      response = correctResponseLoop()
      print("You chose to",response.lower()+".")
    if rerollCount == 2:
      print()
      print("Here is your current roll. Now you must score.")
      printRoll(currentRoll)
      print("Choose from the list:")
      listmessage += 1
      break
  if listmessage == 0:
    print("Here is the score list:")
  print()
  for x in range(len(scoreList)):
    print(scoreList[x],end="")
    if scoreList[x] == scoreListUnavailable[x]:
      print("",scoreHistory[x],end="")
    print()
    if scoreList[x] == "Sixes":
      print()
  print()
  scoreMethod = correctMethodLoop(scoreListAvailable)
  addScore = getScore(scoreMethod,currentRoll)
  if scoreMethod in ["Aces","Twos","Threes","Fours","Fives","Sixes"]:
    scoreUpper += addScore
  else:
    scoreLower += addScore
  if scoreHistory[11] == 50:
    bonus = getBonusYahtzee(currentRoll)
    yahtzeeBonus += bonus

  scoreHistory[scoreList.index(scoreMethod)] = addScore
  scoreListUnavailable[scoreList.index(scoreMethod)] = scoreMethod
  scoreListAvailable.remove(scoreMethod)
  
  print("Your Upper Score is now",scoreUpper)
  print("Your Lower Score is now",scoreLower)
  if yahtzeeBonus > 0:
    print("Your Bonus Yahtzee Score is",yahtzeeBonus)

  if i == 0:
    i = 1

totalScore = scoreUpper + scoreLower + yahtzeeBonus
if scoreUpper >= 63:
  print("Your Upper Score is 63 or higher! Bonus 35 points added to Total.")
  totalScore += 35

print("Your final score is "+str(totalScore)+"!")
print("Thanks for playing! Bye.")
