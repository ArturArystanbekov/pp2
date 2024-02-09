#Ex3.
def farm(heads, legs):
    r=(legs-(heads*2))/2
    ch=heads-r
    print("rabbits =",r, "chikens =",ch)
heads=int(input("How many heads?"))
legs=int(input("How many legs?"))
farm(heads, legs)