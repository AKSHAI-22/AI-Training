import sys

if len(sys.argv) < 2:
    print("No configuration provided")
    sys.exit()
print("Running with config:", sys.argv[1])
