import click
import logging

from bot.orders import (
    place_market_order,
    place_limit_order
)

from bot.validators import (
    validate_side,
    validate_order_type
)


@click.command()
@click.option("--symbol", required=True)
@click.option("--side", required=True)
@click.option("--order_type", required=True)
@click.option(
    "--quantity",
    required=True,
    type=float
)
@click.option(
    "--price",
    required=False,
    type=float
)

def cli(
    symbol,
    side,
    order_type,
    quantity,
    price
):

    print("\n----- ORDER REQUEST -----")
    print(f"Symbol: {symbol}")
    print(f"Side: {side}")
    print(f"Type: {order_type}")
    print(f"Quantity: {quantity}")

    if price:
        print(f"Price: {price}")

    try:

        validate_side(side)
        validate_order_type(order_type)

        if order_type.upper() == "MARKET":

            response = place_market_order(
                symbol,
                side.upper(),
                quantity
            )

        else:

            if price is None:
                print(
                    "Price is required for LIMIT orders"
                )
                return

            response = place_limit_order(
                symbol,
                side.upper(),
                quantity,
                price
            )

        print("\n----- ORDER RESPONSE -----")
        print(
            f"Order ID: {response.get('orderId')}"
        )
        print(
            f"Status: {response.get('status')}"
        )
        print(
            f"Executed Qty: {response.get('executedQty')}"
        )

        if response.get("avgPrice"):
            print(
                f"Avg Price: {response.get('avgPrice')}"
            )

        print(
            "\n✓ Order placed successfully"
        )

    except Exception as e:

        logging.error(str(e))

        print(
            f"\n✗ Order Failed: {e}"
        )


if __name__ == "__main__":
    cli()