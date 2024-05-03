shares_held = [
    ("SHARE 1",  150.50, 100, 175.25),  
    ("SHARE 2",  2500.75, 50, 2600.50),
    ("SHARE 3",  300.25, 75, 320.00),
    ("SHARE 4",  3500.50, 30, 3800.75),
    ("SAHRE 5",   700.00, 20, 750.00)
]

total_cost = 0
total_amount_gained_or_lost = 0

for share in shares_held:
    cost_price = share[2]
    number_of_shares = share[3]
    selling_price = share[4]

    total_cost += cost_price * number_of_shares
    total_amount_gained_or_lost += (selling_price - cost_price) * number_of_shares

percentage_profit_or_loss = ((total_amount_gained_or_lost / total_cost) * 100) if total_cost != 0 else 0

print("Total cost of the portfolio: $", total_cost)
print("Total amount gained or lost: $", total_amount_gained_or_lost)
print("Percentage profit made or loss incurred: ", round(percentage_profit_or_loss, 2), "PERCENT")
