from colorama import init, Fore
import os

init()

fixLoss = int(
    input(f"{Fore.YELLOW}>>> {Fore.RED}Please Enter your Fix Loss:\n{Fore.RED}").strip()
)

while True:
    inputValue = input(
        f"{Fore.YELLOW}>>> {Fore.GREEN} Please EnteryNumber, EntryPrices, SL :\n{Fore.RESET}"
    )
    # os.system('cls')
    if "," not in inputValue:
        continue
    else:
        splittedInput = inputValue.strip().split(",")
        # EntryNumber = splittedInput.remove(splittedInput[0])
        sl = float(splittedInput.pop())
        print(splittedInput)
        if len(splittedInput) == 1:
            value = float(splittedInput[0].strip())
            entryValue = 100 / (((value - sl) / value) * 100) * fixLoss
            # os.system('cls')
            print(
                f"{Fore.YELLOW}>>> {Fore.RED}\nEntry Value: {round(abs(entryValue))}\n"
            )
        if len(splittedInput) == 2:
            value2 = float(splittedInput.pop().strip())
            value1 = float(splittedInput.pop().strip())
            value = value1 * 0.4 + value2 * 0.6
            entryValue = 100 / (((value - sl) / value) * 100) * fixLoss
            print(
                f"{Fore.YELLOW}>>> {Fore.RED}\nEntry Value1: {round(abs(entryValue*0.4))}\nEntry Value2: {round(abs(entryValue*0.6))}\n"
            )

        if len(splittedInput) == 3:
            value3 = float(splittedInput.pop().strip())
            value2 = float(splittedInput.pop().strip())
            value1 = float(splittedInput.pop().strip())
            value = value1 * 0.2 + value2 * 0.3 + value3 * 0.5
            entryValue = 100 / (((value - sl) / value) * 100) * fixLoss
            print(
                f"{Fore.YELLOW}>>> {Fore.RED}\nEntry Value1: {round(abs(entryValue*0.2))}\nEntry Value2: {round(abs(entryValue*0.3))}\nEntry Value3: {round(abs(entryValue*0.5))}\n"
            )
