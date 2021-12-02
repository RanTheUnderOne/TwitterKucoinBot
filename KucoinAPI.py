from kucoin.client import Client
from main import *

KC_KEY = '61a26ec8692c1c0001af2d2d'
KC_SECRET = '22379131-5537-41e6-b3f0-fd169c345e08'
KC_PASSPHRASE = 'kucoinbot123'

client = Client(KC_KEY, KC_SECRET, KC_PASSPHRASE)


def create_order(coin_pair, amount, stop_entry_percentage, stop_loss_percentage):
    current_price = float(client.get_24hr_stats(coin_pair)['buy'])
    converted_amount = round(amount / current_price, 3) # three digit number round

    # creating market "buy" order.
    client.create_market_order(symbol=coin_pair, side=client.SIDE_BUY, size=converted_amount)

    # creating stop-limit order.
    # Stop profit.
    stop_entry_price = current_price * (1 + stop_entry_percentage / 100)
    client.create_limit_order(symbol=coin_pair, side=client.SIDE_SELL, size=converted_amount, price=current_price,
                              stop=client.STOP_ENTRY, stop_price=stop_entry_price)
    print(f'The "stop for profit" price is {stop_entry_price}')

    # Stop loss.
    stop_loss_price = current_price * (1 - stop_loss_percentage / 100)
    client.create_limit_order(symbol=coin_pair, side=client.SIDE_SELL, size=converted_amount, price=current_price,
                              stop=client.STOP_LOSS, stop_price=stop_loss_price)
    print(f'The "stop loss" price is {stop_loss_price}')


def currency_check(currency):
    currencies_list = [x['name'] for x in client.get_currencies()]

    return currency in currencies_list


def final_action(currency1, currency2, AMOUNT):
    if currency_check(currency1):
        coin_pair = f"{currency1}-{currency2}"
        print(coin_pair)
        create_order(coin_pair, amount=AMOUNT, stop_entry_percentage=STOP_ENTRY_PERCENTAGE,
                     stop_loss_percentage=STOP_LOSS_PERCENTAGE)
