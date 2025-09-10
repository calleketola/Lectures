# Här uppe skapar du dina klasser Node och Stack
        






# Driver code
# Den här koden testar ditt program
import random

min_stack = Stack() # Skapar en stack
# Nu vill vi lägga till fem tal
# Vi printar vad som händer i varje steg
for i in range(5): 
    min_stack.push(random.randint(0,9))
    print(f"Stacken: {min_stack} (pushed to stack)")
# Nu plockar vi bort de fem talen
# Vi printar vad som händer i varje steg
for i in range(min_stack.size):
    min_stack.pop()
    print(f"Stacken: {min_stack} (popped from stack)")
    
    
