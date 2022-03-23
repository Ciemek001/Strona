import random
print("Witaj w symulatorze rzutu koscia\n napisz krunia aby sie zadzialo")
rzut = random.randint(1,6)
def diceroll(rzut):
    if input() == (str('krunia')):
        print(rzut)
        print("rzucic jeszcze?")

for i in range (50):
    diceroll(rzut)
    rzut2 = random.randint(1, 6)
    rzut = rzut2//rzut*(rzut+1)+rzut2%rzut