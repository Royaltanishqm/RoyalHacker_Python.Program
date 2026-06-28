Numlist=list(int(x) for x in input("Enter numbers separated by commas: ").split(","))
print("sum of numbers:", sum(Numlist))
print("average of numbers:", sum(Numlist)/len(Numlist))