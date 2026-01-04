from shutil import move

from data_path import *

def rename_files(month, year):
    #print('for Timesheets.')
    #print(f'Path for timesheet: {timesheet_dir}')

    timesheet_dir.mkdir(parents=True, exist_ok=True)

    files = []

    print(f'\n📌 Scanning directory for timesheets: {timesheet_dir}')

    for f in timesheet_dir.iterdir():
        if f.name.startswith('timesheet_'):
            print(f'Found: {f.name}')
            files.append(f.name)

    files_count = len(files)
    print(f'Timesheets found: {files_count}')

    sorted_files = sorted(files)

    if files_count > 1:
        print(f'\n📌 Rename timesheets')
        for files_count, file in enumerate(sorted_files, start=1):
            new_name = f"SYAZA HAZWANI BINTI SUHAINI {month.upper()} {year} W{str(files_count)} FIELDGLASS.pdf"
            initial_path = timesheet_dir / file
            destination_path = timesheet_dir / new_name

            move(initial_path, destination_path)
            print(f"File renamed from '{initial_path.name}' to '{destination_path.name}' successfully.")    

    return