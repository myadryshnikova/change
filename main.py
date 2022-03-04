from collections import Counter


def subtraction_from_change(change, coins_dict, coin_nominal):
    for i in range(coins_dict.get(coin_nominal) + 1):
        if change - (coin_nominal * i) > 0:
            new_change = change - (coin_nominal * i)
    return new_change


def remove_coin_nominal(sorted_coins, coin_nominal):
    while coin_nominal in sorted_coins:
        sorted_coins.remove(coin_nominal)
    return sorted_coins


def give_change(coins=[], change=0):
    coins_dict = {}
    sorted_coins = sorted(coins, reverse=True)
    coins_dict = Counter(sorted_coins)
    new_change = change

    for coin_nominal in coins_dict.keys():
        if change % coin_nominal == 0:
            if change // coin_nominal <= coins_dict.get(coin_nominal):
                return True
            else:
                new_change = subtraction_from_change(change, coins_dict, coin_nominal)

            remove_coin_nominal(sorted_coins, coin_nominal)

            if len(sorted_coins) == 0:
                return False

            give_change(sorted_coins, new_change)
        else:

            if change > coin_nominal:
                new_change = subtraction_from_change(change, coins_dict, coin_nominal)
            remove_coin_nominal(sorted_coins, coin_nominal)

            if len(sorted_coins) == 0:
                return False

            give_change(sorted_coins, new_change)


def main():
    try:
        coins = [int(coin) for coin in input("Enter the coins you have: ").split()]
        change = int(input("Enter the change to be returned: "))
    except ValueError:
        print("\nYou must enter integer numbers.")

    try:
        if give_change(coins, change):
            print("\nYou CAN give the change.")
        else:
            print("\nYou CAN'T give the change.")
    except NameError:
        print("Try again.")


if __name__ == '__main__':
    main()
