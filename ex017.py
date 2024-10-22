from os.path import exists

from_file = "test.txt"
to_file = "new_test.txt"

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
in_data = in_file.read()
# in_data = open(from_file).read()

# print(f"The input file is {len(in_data)} bytes long")

# print(f"Does the output file exist? {exists(to_file)}")
# print(f"Ready, hit RETURN to continue, CTRL-C to abort.")
# input()

out_file = open(to_file, 'w')
out_file.write(in_data)

print("Alright, all done.")

in_file.close()
out_file.close()

# one liner
open("new_test.txt", 'w').write(open("test.txt").read())