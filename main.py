from collections import Counter


def subtraction_from_change(change, coins_dict, coin_nominal):
    for i in range(coins_dict.get(coin_nominal) + 1):
        if change - (coin_nominal * i) > 0:
            new_change = change - (coin_nominal * i)
    return new_change


def remove_coin_nominal(sorted_coins, coin_nominal):
    while (coin_nominal in sorted_coins):
        sorted_coins.remove(coin_nominal)


def give_change(coins=[], change=0):
    coins_dict = {}
    sorted_coins = sorted(coins, reverse=True)
    coins_dict = Counter(sorted_coins)
    new_change = change

    for coin_nominal in coins_dict.keys():
        if change % coin_nominal == 0:
            if change // coin_nominal <= coins_dict.get(coin_nominal):
                #print("True")
                return True
            else:
                new_change = subtraction_from_change(change, coins_dict, coin_nominal)

            remove_coin_nominal(sorted_coins, coin_nominal)

            if len(sorted_coins) == 0:
                #print("False")
                return False

            give_change(sorted_coins, new_change)
        else:

            if change > coin_nominal:
                new_change = subtraction_from_change(change, coins_dict, coin_nominal)
            remove_coin_nominal(sorted_coins, coin_nominal)

            if len(sorted_coins) == 0:
                #print("False")
                return False

            give_change(sorted_coins, new_change)


def set_parameters():
    coins = [5, 10, 5, 50, 10, 20, 100, 200, 200, 5, 3]
    print(give_change(coins, 25))


if __name__ == '__main__':
    set_parameters()
