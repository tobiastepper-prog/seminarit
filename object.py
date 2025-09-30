#!/usr/bin/env python3

#import random

class Kostka:
    def __init__(self, pocet_sten = 6):  
        self.pocet_sten = pocet_sten

    def hod(self):
        import random
        return random.randint(1,self.pocet_sten)

def main():
    k1 = Kostka(6)
    k2 = Kostka(120)
    print(k1.hod())
    print(k2.hod())
    
if __name__ == '__main__':
    main()