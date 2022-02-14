import requests
import json

currency_held = input().lower()
cache = {}

while True:

    currency_exchange = input().lower()

    if currency_exchange == '':
        break

    amount_to_exchange = int(input())

    URL = f'http://www.floatrates.com/daily/{currency_held}.json'

    exchange = json.loads(requests.get(URL).text)

    if currency_held == 'usd':
        cache.update(eur=exchange['eur']['rate'])
    elif currency_held == 'eur':
        cache.update(usd=exchange['usd']['rate'])
    else:
        cache.update(usd=exchange['usd']['rate'], eur=exchange['eur']['rate'])

    print("Checking the cache...")
    if currency_exchange in cache:
        rate = round(amount_to_exchange * cache[currency_exchange], 2)
        print("Oh! It is in the cache!")
        print(f"You received {rate} {currency_exchange.upper()}.")
    else:
        print("Sorry, but it is not in the cache!")
        cache[currency_exchange] = exchange[currency_exchange]['rate']
        rate = round(amount_to_exchange * cache[currency_exchange], 2)
        print(f"You received {rate} {currency_exchange.upper()}.")
