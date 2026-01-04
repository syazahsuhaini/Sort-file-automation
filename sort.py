# import modules
import sys
from shutil import move

from data_path import *
from category import categories

def sort_files():

    root_dir.mkdir(parents=True, exist_ok=True)
    timesheet_dir.mkdir(parents=True, exist_ok=True)

    print(f'\n📌 Scanning directory for files: {root_dir}')
    # appending files in Downloads into list
    files = []

    for f in root_dir.iterdir():
        if f.is_file() and not f.name.startswith('.'):
            print(f'Found: {f.name}')
            files.append(f.name)

    files_count = len(files)
    print(f'Uncategorized files found: {files_count}')

    if files_count > 1:
        print(f'\n📌 Move files into their directory')
        # move the files in list into respective folders
        for file in files:
            for category in categories.values():
                if file.lower().endswith(tuple(category['Extensions'])):
                    category['Path'].mkdir(exist_ok=True)

                    initial_path = root_dir / file
                    destination_path = category['Path'] / file

                    print(f'Moving: {file}')
                    print(f' → Into folder: {category['Path'].name}')

                    move(initial_path, destination_path)
                    break

    print(f'\n📌 Scanning directory timesheets: {documents_dir}')
    files = []

    for f in documents_dir.iterdir():
        if f.name.startswith('timesheet_'):
            print(f'Found: {f.name}')
            files.append(f.name)

    files_count = len(files)
    print(f'Timesheets found: {files_count}')

    if files_count > 1:
        print(f'\n📌 Move files into Timesheet')
        for file in files:
            initial_path = documents_dir / file
            destination_path = timesheet_dir / file

            print(f'Moving: {file}')
            print(f' → Into folder: {destination_path.name}')

            move(initial_path, destination_path)


    return

"""
if __name__ == '__main__':
    if len(sys.argv) != 1:
        print('Usage: python sort.py')
        sys.exit(1)

    sort_files()
"""