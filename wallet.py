#"I have a dictionary where each name maps to a wallet.
# The user inputs a name.
# I look it up in the dictionary and print wallet."

name_tracker = input("Enter your first and last name: ")

wallets = {
    "Ben James" : {
        "address": "1T0v1", "balance": 5.2
    },
    "Rachel Smith" : {
    "address": "CC834", "balance": 9.9
    },
    "Sylvia Benson" : {
        "address": "0xABC", "balance": 8.1
    },
    "James LeBron" : {
        "address": "X0384", "balance": 2.3
    }
}



if name_tracker in wallets:
    print(f"{name_tracker}: {wallets[name_tracker]}")
else:
    print(f"{name_tracker} is not a registered user.")