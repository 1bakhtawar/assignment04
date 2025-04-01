MINIMUM_HEIGHT:int = 50
def main():
    user:int = int(input('\033[1;3m How old are you?\033[0m'))
    if user >= MINIMUM_HEIGHT:
        print('You are tall enough to ride')
    else:
        print('You ae not tall enough to ride.May be next year.')

if __name__ == '__main__':
    main()