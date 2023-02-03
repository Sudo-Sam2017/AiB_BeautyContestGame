# Initialize 5 players. Set scores.
print(" ** Welcome to Beauty Contest!!! ** ")

CPU1_Score = 10
CPU2_Score = 10
CPU3_Score = 10
CPU4_Score = 10
CPU5_Score = 10

currentScores = [CPU1_Score, CPU2_Score, CPU3_Score, CPU4_Score, CPU5_Score]


CPU_1 = int(input("Player One, please enter a number from 1 to 100: "))
CPU_2 = int(input("Player Two, please enter a number from 1 to 100: "))
CPU_3 = int(input("Player Three, please enter a number from 1 to 100: "))
CPU_4 = int(input("Player Four, please enter a number from 1 to 100: "))
CPU_5 = int(input("Player Five, please enter a number from 1 to 100: "))


print(CPU_1)
print(CPU_2)
print(CPU_3)
print(CPU_4)
print(CPU_5)

sum = (CPU_1 + CPU_2 + CPU_3 + CPU_4 + CPU_5)
avg = (sum) / 5
product_ans = (float)(avg) * 0.8
print("The product answer is: ", product_ans)

def showUpdatedScores():
    print("Player 1 Score: ", CPU1_Score)
    print("Player 2 Score: ", CPU2_Score)
    print("Player 3 Score: ", CPU3_Score)
    print("Player 4 Score: ", CPU4_Score)
    print("Player 5 Score: ", CPU5_Score)


def compareInputsToProduct(player1: int, player2: int, player3: int, player4: int, player5: int, productAnswer: int):
    playerOneDiff = abs(player1 - productAnswer)
    playerTwoDiff = abs(player2 - productAnswer)
    playerThreeDiff = abs(player3 - productAnswer)
    playerFourDiff = abs(player4 - productAnswer)
    playerFiveDiff = abs(player5 - productAnswer)

    diffArray = [round(playerOneDiff, 2), round(playerTwoDiff, 2), round(playerThreeDiff, 2), round(playerFourDiff, 2), round(playerFiveDiff, 2)]

    closestNumber = min(diffArray)
    closestNumberIndex = diffArray.index(closestNumber)

    print(diffArray)
    print(closestNumberIndex)

    return closestNumberIndex


def determineWinner():
    winner = compareInputsToProduct(CPU_1, CPU_2, CPU_3, CPU_4, CPU_5, product_ans)
    
    if winner == 0:
        print("Player 1 Wins!")
        winningPlayer = 1
    elif winner == 1:
        print("Player 2 Wins!")
        winningPlayer = 2
    elif winner == 2:
        print("Player 3 Wins!")
        winningPlayer = 3
    elif winner == 3:
        print("Player 4 Wins!")
        winningPlayer = 4
    elif winner == 4:
        print("Player 5 Wins!")
        winningPlayer = 5

    return winningPlayer
    
  
def updateScores():
    roundWinner = determineWinner()
    if roundWinner == 1:
        currentScores[0] = currentScores[0] - 1
        print(currentScores)
    elif roundWinner == 2:
        currentScores[1] = currentScores[1] - 1
        print(currentScores)
    elif roundWinner == 3:
        currentScores[2] = currentScores[2] - 1
        print(currentScores)
    elif roundWinner == 4:
        currentScores[3] = currentScores[3] - 1
        print(currentScores)
    elif roundWinner == 5:
        currentScores[4] = currentScores[4] - 1
        print(currentScores)
    



determineWinner()
updateScores()
showUpdatedScores()



    
# Prompt each player for their number from 1 to 100

# Calculate player average and product answer (avg * 0.8)

# Compare player inputs to product answer. Determine loser. Update scores. 
