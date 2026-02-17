import platform
import sys
version = platform.python_version()
print("Python Version:", version)

if not version.startswith("3"):
    print("Unsupported Python version")
    sys.exit()

print("Environment supported")
