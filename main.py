# Initialize 5 players. Set scores.
P1_Score = 0
P2_Score = 0
P3_Score = 0
P4_Score = 0
P5_Score = 0

def playerOneLost(P1_score):
    p1Score = P1_score + 1
    return p1Score

#just a test

def playerTwoLost(P2_score):
    p2Score = P2_score + 1
    return p2Score

def playerThreeLost(P3_score):
    p3Score = P3_score + 1
    return p3Score

def playerFourLost(P4_score):
    p4Score = P4_score + 1
    return p4Score

def playerFiveLost(P5_score):
    p5Score = P5_score + 1
    return p5Score




def beginRound():
    print(" ** Welcome to Beauty Contest!!! ** ")
    CPU_1 = int(input("Player One, please enter a number from 1 to 100: "))
    CPU_2 = int(input("Player Two, please enter a number from 1 to 100: "))
    CPU_3 = int(input("Player Three, please enter a number from 1 to 100: "))
    CPU_4 = int(input("Player Four, please enter a number from 1 to 100: "))
    CPU_5 = int(input("Player Five, please enter a number from 1 to 100: "))
    sum = (CPU_1 + CPU_2 + CPU_3 + CPU_4 + CPU_5)
    avg = (sum) / 5
    product_ans = (float)(avg) * 0.8
    print("The product answer is: ", product_ans)
    roundResults = [CPU_1, CPU_2, CPU_3, CPU_4, CPU_5, product_ans]
    return roundResults
    



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
    listA = []
    listA = beginRound()
    winner = compareInputsToProduct(listA[0], listA[1], listA[2], listA[3], listA[4], listA[5])
    print(listA)
    
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

    print(winningPlayer)
    return winningPlayer
    
  
""" def updateScores():
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
    return currentScores """
    


beginRound()
determineWinner()
# updateScores()



    
# Prompt each player for their number from 1 to 100

# Calculate player average and product answer (avg * 0.8)

# Compare player inputs to product answer. Determine loser. Update scores. 
