class Red:
    health=5

    def attack(self):
        print('Skaddooosh')
        self.health -= 2

    def dead(self):
        if self.health <= 0:
            print('Tango Down')
        else:
            print(str(self.health)+ " health left")


class Blue:
    life=8

    def attack1(self):
        print('Wooosh!')
        self.life -=3

    def dead1(self):
        if self.life <= 0:
            print('Need a Medic')
        else:
            print(str(self.life)+ " left")
    def medic(self):
        if self.life <= 0:
            print('Medic is HERE!!!')


blue1 = Blue()
blue1.attack1()
blue1.dead1()
blue1.attack1()
blue1.dead1()
blue1.attack1()
blue1.dead1()
blue1.medic()

red1 = Red()
red1.attack()
red1.dead()
red1.attack()
red1.dead()
red1.attack()
red1.dead()