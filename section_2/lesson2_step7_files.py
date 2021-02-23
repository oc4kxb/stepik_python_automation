import os

print("\nos.path.abspath(__file__): " + os.path.abspath(__file__))
print("\nos.path.abspath(os.path.dirname(__file__)): " + os.path.abspath(os.path.dirname(__file__)))
print("\nos.path.dirname(__file__): " + os.path.dirname(__file__))

current_dir = os.path.abspath(os.path.dirname(__file__))
new_file_path = os.path.join(current_dir, "file.txt")
print("\nnew_file_path: " + new_file_path)

