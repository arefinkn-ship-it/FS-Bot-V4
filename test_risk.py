from risk_manager import (
    build_trade,
    risk_reward
)

trade = build_trade(
    "BUY",
    3350.00,
    20
)

print(trade)

rr1 = risk_reward(
    trade["entry"],
    trade["sl"],
    trade["tp1"]
)

rr2 = risk_reward(
    trade["entry"],
    trade["sl"],
    trade["tp2"]
)

print()

print("RR TP1:", rr1)

print("RR TP2:", rr2)