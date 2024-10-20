import os

for i in range(10):
    file_path = str(i) + ".jpg"  # Replace with the actual path to your file
    os.remove(file_path)
