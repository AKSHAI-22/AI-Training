import os

folder = "results"

if not os.path.exists(folder):
    os.makedirs(folder)

print("Folder ready")
