#!/usr/bin/env python3

import random

class Kostka:
    def hod(self):
        import random
        return random.randint(1,6)  

def main():
    k1 = Kostka()
    k2 = Kostka()
    print(k1.hod() + 100)

if __name__ == '__main__':
        main()