from transitions import Machine, State
import random


class Cat(object):
    states = [State(name='asleep'), State(name='hungry'), State(name='catching_the_intruder'),
              State(name='annoying_the_human'), State(name='tired'), State(name='sit_on_pc'), State(name='satisfied')]

    # same as:
    # states = ['asleep', 'hungry', 'catch_the_intruder', 'annoying_the_human', 'tired', 'sit_on_pc']

    def __init__(self, name):
        self.name = name
        self.mice_catched = 0
        self.fallen_object = 0
        # initialize fsm
        self.machine = Machine(model=self, states=Cat.states, initial='asleep')

        # Add transitions
        # from asleep
        self.machine.add_transition('wakeup', 'asleep', 'hungry')
        # from hungry
        self.machine.add_transition('eat', 'hungry', 'satisfied', conditions='is_ok_with_The_food')
        self.machine.add_transition('eat', 'hungry', 'annoying_the_human')
        # from annoying_the_human
        self.machine.add_transition('food_in_bowl', 'annoying_the_human', 'satisfied', conditions='is_ok_with_The_food')
        self.machine.add_transition('food_in_bowl', 'annoying_the_human', 'annoying_the_human')
        self.machine.add_transition('mouse_nearby', 'annoying_the_human', 'catching_the_intruder')
        self.machine.add_transition('ignored', 'annoying_the_human', 'sit_on_pc')

        # from satisfied
        self.machine.add_transition('pc_is_on', 'satisfied', 'sit_on_pc')
        self.machine.add_transition('enter_a_box', 'satisfied', 'asleep')
        self.machine.add_transition('yawns', 'satisfied', 'asleep')

        # can happen ALWAYS, literally A L W A Y S
        self.machine.add_transition('pc_is_on', '*', 'sit_on_pc', after='send_bad_emails')
        self.machine.add_transition('enter_a_box', '*', 'asleep')
        self.machine.add_transition('cat_food_opening_sound', '*', 'annoying_the_human')

        # from tired
        self.machine.add_transition('yawns', 'tired', 'asleep', before='clean_up')

        # from sit_on_pc
        self.machine.add_transition('humans_is_looking', 'sit_on_pc', 'asleep')

        # from catch_the_intruder
        self.machine.add_transition('run', 'catching_the_intruder', 'tired')
        self.machine.add_transition('catched', 'catching_the_intruder', 'tired')

        # Messages to print when enter/exit a state
        self.machine.on_enter_satisfied('is_eating')
        self.machine.on_enter_hungry('is_hungry')
        self.machine.on_exit_asleep('is_up')
        self.machine.on_enter_asleep('is_sleeping')
        self.machine.on_enter_annoying_the_human('is_annoying')

    def is_ok_with_The_food(self):
        print("The human gives the food, \nbut", self.name, 'doesn\'t look satisfied...Miao? Will', self.name, 'eat?')
        return random.random() < 0.5

    def send_bad_emails(self):
        names = ['Boss', 'Wife', 'Big client', 'client', 'Important client', 'Landlord', 'Granny', 'Mum']
        effects = [' will not be happy', ' answered back. Good luck.', ' looks delighted!']
        name = random.choice(names)
        effect = random.choice(effects)
        print('Human\'', name, 'received a bad email. ', name, effect)

    def clean_up(self):
        print("Bath time! Slurp, slurp, slurp")

    def food_in_bowl(self):
        print()

    #================ ENTER/EXIT STATES MESSAGES =============

    # enters satisfied
    def is_eating(self):
        print(self.name, "is eating!", "Gnom gnom gnom,", self.name, "is satisfied!")

    # enters hungry
    def is_hungry(self):
        print(self.name, "is soooo hungry! Maow maow MAAAAOOOWWW!")

    # exit asleep
    def is_up(self):
        numbers = ['two', 'three', 'four', 'five', 'nine', 'seven', 'twelve', 'a looooot of']
        times = ['minutes', 'hours', 'seconds', 'days(????)']
        adventures = ['adventure.', 'day.', 'discovery.', 'mug to break.', ]
        number = random.choice(numbers)
        tims = random.choice(times)
        adventure = random.choice(adventures)
        print('It\'s a new day for our cat,', self.name,'\nAfter', number, tims, 'of sleeping,', self.name,
              'is ready for a new', adventure)

    # enters asleep
    def is_sleeping(self):
        print("Time to a small (or maybe long?) nap. Good night", self.name)

    # enters annoying_the_human
    def is_annoying(self):
        print("Maooowwww, maow maow maow, maaaaooow, MAAAAOW!! Our", self.name, "wants more!")
