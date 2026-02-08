config = {"host","port","user"}
required = {"host","port","user","password"}

missing = required - config
extra = config - required

print("Missing:", missing)
print("Extra:", extra)
