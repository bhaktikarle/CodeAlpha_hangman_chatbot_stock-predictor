def stock_tracker():
    prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 2700, "AMZN": 3300}
    total = 0
    portfolio = {}

    while True:
        stock = input("Enter stock name (or 'done' to finish): ").upper()
        if stock == "DONE":
            break
        if stock in prices:
            qty = int(input(f"Enter quantity for {stock}: "))
            cost = prices[stock] * qty
            portfolio[stock] = (qty, cost)
            total += cost
        else:
            print("Stock not found.")

    print("\n--- Portfolio Summary ---")
    for stock, (qty, cost) in portfolio.items():
        print(f"{stock}: {qty} shares, ₹{cost}")

    print(f"\nTotal Investment Value: ₹{total}")

stock_tracker()