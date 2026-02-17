import platform
import sys

if platform.system() != "Windows":
    print("Unsupported environment")
    sys.exit()

print("Environment supported")
