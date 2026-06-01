from bot.client import client
import logging


def place_market_order(symbol, side, quantity):

    logging.info(
        f"Market Order Request: {symbol} {side} {quantity}"
    )

    response = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="MARKET",
        quantity=quantity,
        recvWindow=10000
    )

    logging.info(f"Order Response: {response}")

    return response


def place_limit_order(symbol, side, quantity, price):

    logging.info(
        f"Limit Order Request: {symbol} {side} {quantity} {price}"
    )

    response = client.futures_create_order(
        symbol=symbol,
        side=side,
        type="LIMIT",
        quantity=quantity,
        price=price,
        timeInForce="GTC",
        recvWindow=10000
    )

    logging.info(f"Order Response: {response}")

    return response