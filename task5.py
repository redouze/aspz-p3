import os
import sys
import shutil

if len(sys.argv) != 3:
    print("Program need two arguments")
    sys.exit(1)

source_file = sys.argv[1]
destination_file = sys.argv[2]

if not os.access(source_file, os.R_OK):
    print(f"Cannot open file {source_file} for reading")
    sys.exit(1)

if not os.access(destination_file, os.W_OK):
    print(f"Cannot open file {destination_file} for writing")
    sys.exit(1)

try:
    max_file_size = 10 * 1024

    file_size = os.path.getsize(source_file)

    if file_size > max_file_size:
        print(f"File {source_file} exceeds size limit ({max_file_size} bytes)")
        sys.exit(1)

    shutil.copy(source_file, destination_file)
    print(f"File {source_file} successfully copied to {destination_file}")

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
