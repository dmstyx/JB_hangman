import requests

cache = dict()

currency = input().lower()

def get_json_from_server(currency, new_currency, amount):
    r = requests.get(f'http://www.floatrates.com/daily/{currency}.json')
    json_text = r.json()
    if  currency not in ['usd', 'eur']:
        cache['usd'] = json_text['usd']
        cache['eur'] = json_text['eur']
    cache[new_currency] = json_text[new_currency]

    exchange(new_currency, amount)
    get_json_from_cache(currency)

def get_json_from_cache(currency):
    new_currency = input().lower()
    if new_currency == "":
        quit()

    else:
        amount = input()
        print('Checking the cache...')
        if new_currency in cache:
            print('Oh! It is in the cache!')
            exchange(new_currency, amount)
            get_json_from_cache(currency)
        elif new_currency in ['usd', 'USD', 'eur', 'EUR' ]:
            print('Oh! It is in the cache!')
            get_json_from_server(currency, new_currency, amount)
        else:
            print('Sorry, but it is not in the cache!')
            get_json_from_server(currency, new_currency, amount)

def exchange(new_currency, amount):
    new_amount = round(cache[new_currency]['rate'] * float(amount), 2)
    print(f"{new_amount} {new_currency.upper()}")

get_json_from_cache(currency)
