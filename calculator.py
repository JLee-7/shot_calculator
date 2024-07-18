def main():
    import math
    magsize = int(input("Rounds in Magazine: "))

    def fourth():
        print("---------------")
        print("FOURTH TIMES THE CHARM")
        x = magsize
        totalbullets = x
        while (x >= 4):
            x = x - 2
            totalbullets = totalbullets + 2
        print(totalbullets)
    fourth()

    def triple():
        print("---------------")
        print("TRIPLE TAP")
        y = magsize
        totalbullets = y
        while (y >= 3):
            y = y - 2
            totalbullets = totalbullets + 1
        print(totalbullets)
    triple()

    def both():
        print("---------------")
        print("4th TIMES + TRIPLE TAP")
        z = magsize
        totalbullets = (-1**(z+1)) - 12 + (6 * z)
        print(totalbullets)
    both()

    def rewind():
        print("---------------")
        print("REWIND ROUNDS")
        a = magsize
        totalbullets = a
        bullets = a
        while (bullets/magsize >= 0.2875):
            bullets = math.ceil(bullets * 0.6)
            totalbullets += bullets
        print(totalbullets)
    rewind()

main()
