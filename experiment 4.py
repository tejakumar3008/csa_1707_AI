import itertools
def solve_cryptarithm():
    letters = "SENDMORY" 
    digits = "0123456789"
    for perm in itertools.permutations(digits, len(letters)):
        mapping = dict(zip(letters, perm))
        if mapping['S'] == '0' or mapping['M'] == '0':
            continue
        send = int("".join(mapping[ch] for ch in "SEND"))
        more = int("".join(mapping[ch] for ch in "MORE"))
        money = int("".join(mapping[ch] for ch in "MONEY"))
        if send + more == money:
            print("Solution Found!")
            print("SEND  =", send)
            print("MORE  =", more)
            print("MONEY =", money)
            return 
    print("No solution found.")
if __name__ == "__main__":
    solve_cryptarithm()
