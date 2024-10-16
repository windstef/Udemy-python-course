# use for
# 165
# Bonus Example

# we're going to use zipfile.
# Zipfile gives you more flexibility
# to work with zip files.
# For example, shutil is limited

import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)       # assign the PosixPath from the string path
            archive.write(filepath, arcname=filepath.name)      # extract only the name of the file, not the absolut path

if __name__ == "__main__":
    make_archive(filepaths=["todos.txt","functions.py"], dest_dir="dest")