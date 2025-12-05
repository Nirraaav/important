import os
import time

def generate_index(directory):
    # Create or overwrite the index.html file
    index_file_path = os.path.join(directory, 'index.html')
    with open(index_file_path, 'w') as f:
        f.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n')
        f.write('<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        f.write(f'<title>{os.path.basename(directory)}</title>\n')
        f.write('</head>\n<body>\n')
        
        # Set heading based on the directory name
        if directory == '.':
            # set the name as the name of the directory
            f.write(f'<h1>{os.path.basename(os.path.abspath(directory))}</h1>\n')

            # Add last updated date
            last_modified_time = os.path.getmtime(directory)
            last_updated_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(last_modified_time))
            f.write(f'<p>Last updated: {last_updated_date}</p>\n')
        else:
            # Subdirectories
            f.write(f'<h1>{os.path.basename(directory)}</h1>\n')
        
        f.write('<ul>\n')

        # List directories
        for entry in sorted(os.listdir(directory)):
            if (entry == '.git' or entry == '.github') and directory == '.':
                continue
            entry_path = os.path.join(directory, entry)
            if os.path.isdir(entry_path) and entry != 'index.html':
                f.write(f'<li><a href="{entry}/index.html">{entry}</a></li>\n')

        # List files
        for entry in sorted(os.listdir(directory)):
            if entry == '.git' or entry == 'generator.py':
                continue
            entry_path = os.path.join(directory, entry)
            if os.path.isfile(entry_path) and (
                    entry.endswith('.ipynb') 
                    or entry.endswith('.png') 
                    or entry.endswith('.jpg') 
                    or entry.endswith('.txt') 
                    or entry.endswith('.csv') 
                    # or entry.endswith('.py') 
                    or entry.endswith('.pdf')
                    ):
                f.write(f'<li><a href="{entry}">{entry}</a></li>\n')

        f.write('</ul>\n')

        # Add navigation link to previous directory
        if directory != '.':  
            f.write(f'<a href="../index.html">Back to previous page</a>\n')

        f.write('</body>\n</html>\n')

# Generate index.html files for all directories
for root, dirs, files in os.walk('.'):
    # Skip the .git directory in the main directory
    if root == '.' and ('.git' or '.github' in dirs):
        dirs.remove('.git')
    if 'index.html' not in files:  # Check if index.html already exists
        generate_index(root)
