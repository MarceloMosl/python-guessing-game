from numbers import Number
import random


def getChosenNumber(low: int, high: int):
  question = "Enter your guess from {lowestPossibleGuess} to {highestPossibleGuess}: "
  inputNumber = input(question.format(lowestPossibleGuess=low, highestPossibleGuess=high))
  while(inputNumber.isnumeric() == False or int(inputNumber) > high or int(inputNumber) < low):
    print("\nChose a valid number!! Your number needs to be a Number (duh...) and it needs to be between the range {low} - {high}".format(low=low, high=high))
    inputNumber = input(question.format(lowestPossibleGuess=low, highestPossibleGuess=high))
  
  return int(inputNumber)
    


def main():
  hiddenNumber = random.randint(1, 1000)

  guessCounter = 1

  lowestPossibleGuess: int = 1
  highestPossibleGuess: int = 1000


  chosenNumber = getChosenNumber(low=lowestPossibleGuess, high=highestPossibleGuess)

  while(chosenNumber != hiddenNumber and guessCounter < 10):
    
    if(chosenNumber > hiddenNumber):
       highestPossibleGuess = chosenNumber - 1
    else:
      lowestPossibleGuess = chosenNumber + 1
            
    print("Wrong! Guess count {guessCounter} \n".format(guessCounter=guessCounter))

    chosenNumber = getChosenNumber(low=lowestPossibleGuess, high=highestPossibleGuess)
  
    guessCounter = guessCounter + 1


  if(guessCounter == 10):
   return print("You failed! The number was {hiddenNumber} But you can always try again :)".format(hiddenNumber=hiddenNumber))
  else:
   return print("You got it! The hidden number was {hiddenNumber} \n It took you {guessCounter} guess(es).".format(hiddenNumber=hiddenNumber, guessCounter=guessCounter))



main()