###########################################################
#                                                         #
# Problem: given an amount of cents and a list of coins,  #
# find the fewest number of coins necessary to make that  #
# amount.                                                 #
# 							                              #
###########################################################

def greedy_fewest_coins(amt_in_cents, coin_value_list = [1,5,10,25]):
    # Sort and reverse coin list
    coin_value_list.sort()
    coin_value_list.reverse()

    # Iterate through coin list, biggest value first
        # Use as many largest coins as possible
        # deduct that value from the amount remaining

    num_coins = 0
    for coin in coin_value_list:
        num_coins += amt_in_cents // coin # 63 // 25 = 2
        amt_in_cents %= coin # 63 % 25 = 13

            # while amt_in_cents >= coin:
            #     num_coins += 1
            #     amt_in_cents -= coin



    # Return number of coins
    return num_coins





print("Fewest coins to make $0.63 using only:")
print("\tpennies: ", end = '')
print(greedy_fewest_coins(63, [1]))

print("\tpennies and nickles: ", end = '')
print(greedy_fewest_coins(63, [1, 5]))

print("\tpennies, nickles, and dimes: ", end = '')
print(greedy_fewest_coins(63, [1, 5, 10]))

print("\tpennies, nickles, dimes, and quarters: ", end = '')
print(greedy_fewest_coins(63, [1, 5, 10, 25]))


################################### Quiz ###################################
# Will this give the correct answer (fewest coins) for any amount and      #
# any list of coins?                                                       #
#    1) yes                                                                #
#    2) NO                                                                 #
############################################################################



# print("\tpennies, $0.21 pieces, and quarters: ", end = '')
# print(greedy_fewest_coins(63, [1, 21, 25]))