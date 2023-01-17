string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = "  bEautiful"
string1 = string1.lower()
string3 = string3.lower()
string4 = string4.lstrip()
string4 = string4.lower()
print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))
print(string4.startswith("be"))