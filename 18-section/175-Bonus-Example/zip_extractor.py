# 175
# Bonus Example
# Backend

# Remarks
# 1. Design the Frontend
# 2. Code the Frontend
# 3. Code the Backend
# 4. Finish Up


# Target: create a program which extracts a zip file to a destination directory.

# follow-up:
# 165
# Bonus Example
# zip creator

########################################

import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("/home/stefkour/PycharmProjects/app1/pythonProject/18-section/175-Bonus-Example/compressed.zip",
                    "/home/stefkour/PycharmProjects/app1/pythonProject/18-section/175-Bonus-Example/extracted/")
