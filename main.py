# Initialize 5 players. Set scores.
print(" ** Welcome to Beauty Contest!!! ** ")

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
# Prompt each player for their number from 1 to 100

# Calculate player average and product answer (avg * 0.8)

# Compare player inputs to product answer. Determine loser. Update scores. 
