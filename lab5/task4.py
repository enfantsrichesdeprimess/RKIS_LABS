def transform_string(s):
    if s.startswith("abc"):
        return "www" + s[3:]
    else:
        return s + "zzz"

print(transform_string("abc123"))  # www123
print(transform_string("hello"))  # hellozzz
print("\n")