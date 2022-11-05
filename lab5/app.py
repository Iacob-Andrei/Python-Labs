import utils

if __name__ == '__main__':
    while True:
        inp = input("Give input: ")
        if inp == 'q':
            exit()

        try:
            x = int(inp)
            print(utils.process_item(x))
        except ValueError as e:
            print("Wrong input.", e)
