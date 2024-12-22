from collections import Counter

secrets = []
for line in open("input.txt"):
    secrets.append(int(line))


def mix(value, secret):
    return value ^ secret


def prune(secret):
    return secret % 16777216


def get_next_secret(secret):
    secret = prune(mix(secret * 64, secret))
    secret = prune(mix(int(secret / 32), secret))
    secret = prune(mix(secret * 2048, secret))

    return secret


ans1 = 0
for secret in secrets:
    for _ in range(2000):
        secret = get_next_secret(secret)

    ans1 += secret

print("Part1: ", ans1)

all_prices = []
all_changes = []
for secret in secrets:
    prices = [0]
    changes = []
    for _ in range(2000):
        prices.append(secret % 10)
        nxsecret = get_next_secret(secret)
        changes.append(prices[-1] - prices[-2])
        secret = nxsecret
    del prices[0]
    del changes[0]
    all_prices.append(prices)
    all_changes.append(changes)

values = Counter()
for price_ind, changes in enumerate(all_changes):
    seen = set()
    for i in range(3, len(changes)):
        sequence = tuple(changes[i - 3 : i + 1])
        if sequence not in seen:
            values[sequence] += all_prices[price_ind][i + 1]
            seen.add(sequence)

print("Part2: ", max(values.values()))
