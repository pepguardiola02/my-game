print("Välkommen till frågesport!")

print()

name = input("Vad är ditt namn?")
 
score = 0 
print()

questions = ( ["Fotbolls-EM 2016 avgjordes i Frankrike. Vilket land kammade hem guld?", "portugal"],
["Zlatan är den enda som vunnit Guldbollen fler än två gånger. Hur många guldbollar har han vunnit?", "11"],
["Friidrottaren Usain Bolt springer fortast i världen på kortdistanser. Vilket land kommer han ifrån?", "jamaica"],
["Vilket land vann Fotbolls-EM 2012?", "spanien"],
["Artisten har gjort låten för fotbolls-VM 2010 i Sydafrika. Vad hette låten?", "waka waka"],)

print()

for q in questions:
    print()
    if input(q[0]) == (q[1]):
        print("Correct") 
        score = score + 1
    else:
        print("Incorrect")


print("Grattis, " + name + " fick " + str(score) + " rätta svar!")
 
score_percentage = score/5 * 100
print("Detta är en poäng på " + str(score_percentage) + " procent")
