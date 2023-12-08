str = input()
trans_str = ""
for s in str:
    if s.isupper():
        trans_str += s.lower()
    else:
        trans_str += s.upper()
print(trans_str)
        