expected = set(input("Expected vocab: ").split())
n = int(input("Documents count: "))

found = set()

for _ in range(n):
    found |= set(input().lower().split())

covered = expected & found
missing = expected - found

percent = len(covered) / len(expected) * 100

print("Coverage %:", percent)
print("Missing words:", missing)
