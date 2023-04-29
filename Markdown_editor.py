import argparse
import os
import subprocess

def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description='A simple Markdown editor CLI.')
    parser.add_argument('filename', help='the filename of the Markdown file')
    args = parser.parse_args()

    # Check if the file exists
    if not os.path.exists(args.filename):
        print(f"File '{args.filename}' does not exist.")
        return

    # Open the file in the default text editor
    subprocess.call([os.environ.get('EDITOR', 'nano'), args.filename])

if __name__ == '__main__':
    main()
