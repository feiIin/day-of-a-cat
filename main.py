from fsm import Cat

def main():
    princess = Cat("Princess")
    # current state of the cat
    # print('Princess is', princess.state)
    # transition to another state
    princess.wakeup()
    # current state of the cat
    princess.eat()
    princess.enter_a_box()


if __name__ == "__main__":
    main()