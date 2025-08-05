def battery_charge(charge):
    # charge=100
    bars = charge // 10
    if charge % 10 > 5:
        bars += 1

    print("[" + bars * "❚" + (10 - bars) * " " + "]")
    print(str(charge) + "%")
