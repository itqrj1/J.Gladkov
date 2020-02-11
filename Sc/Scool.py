s = list (range(10))

print(s)
s[0:0] = [-1,-1,-1]
print(s)


del s[:3]
print(s)
print("---------")

a = (1,2,3,4,5,6,7,8,9)
b =(3,2,1)
print(b <= a)
print("__________")

f = dict.fromkeys(["a", "b"])
print(f)

f["c"] = 3
f["a"] = 1
print(f.pop("a"))

print(f)
print(f.keys())
print(f.values())
print(f.items())
