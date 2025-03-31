def main():
    fehrenheit = float(input("\033[1;3m Enter temperature in Fehrenheit: \033[0m"))
    celsius = (fehrenheit - 32) * 5.0/9.0
    print(f"\033[1;3m temperature :{fehrenheit}F - {celsius}C \033[0m ")

if __name__ == "__main__":
    main()