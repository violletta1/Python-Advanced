
#SOLUTION WITH COMPREHATION

# def grocery_store(**products):
#     products = sorted(products.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
#     return '\n'.join([f"{k}: {v}" for k,v in products])



def grocery_store(**products):
    products = sorted(products.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))# -X[1] because we want from largest to smallest number
    result = []

    for product , quantity in products:
        result.append(f"{product}: {quantity}")

    return "\n".join(result)






print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))

print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))