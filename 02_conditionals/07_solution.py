# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

def customizeOrder(orderSize, hasExtraShot):
    orderSize = orderSize.title()
    hasExtraShot = True if hasExtraShot.lower() == 'yes' else False
    if hasExtraShot:
        return orderSize + " coffee with extra shot of espresso"
    else:
        return orderSize + " coffee"

orderSize = input("Choose coffee size: Small | Medium | Large : ")
hasExtraShot = input("Want extra shot of espresso? Yes | No : ")
print(customizeOrder(orderSize, hasExtraShot))
