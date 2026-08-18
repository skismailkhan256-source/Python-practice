dict1=["apple","banana","cherry"]
prices=[0.5,0.3,0.2]
dict_prices = {dict1[i]:prices[i] for i in range(len(dict1))}
print(dict_prices)