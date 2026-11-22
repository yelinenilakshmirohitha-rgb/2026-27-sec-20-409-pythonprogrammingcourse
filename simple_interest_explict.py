def simple_interest(p, t, r=5):
    si = (p * t * r) / 100
    return si

print("Default rate:", simple_interest(1000, 2))
print("Explicit rate:", simple_interest(1000, 2, 10))