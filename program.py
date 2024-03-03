import shutil
from pathlib import Path

"""
Scripts to sort files in downloads folder based on their file prefix
'cc_' -> 'contemporary-civ-2' folder
'ai_' -> 'coms4701' folder
"""


# Move file to destination folder
def move_file(file, destination):
    try:
        if not destination.exists():
            destination.mkdir()
        shutil.move(file, destination)
    except shutil.Error as e:
        print(e)


# Sort files in folder based on their prefix
def sort_folder(folder_path):
    destinations = {
        'cc_': Path(f'{Path.home()}/Desktop/columbia/semester4/contemporary-civ-2'),
        'ai_': Path(f'{Path.home()}/Desktop/columbia/semester4/coms4701'),
    } 
    
    for file in folder_path.iterdir(): 
        if file.is_file() and not file.name.startswith('.'):
            first_three_chars = file.name[:3]
            if first_three_chars in destinations:
                move_file(file, destinations[first_three_chars])


if __name__ == '__main__':
    home_directory = str(Path.home())
    downloads_path = Path(f'{home_directory}/Downloads')

    sort_folder(downloads_path)