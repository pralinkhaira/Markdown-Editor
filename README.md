# Markdown Editor CLI

A simple command-line interface for editing Markdown files.

## Installation

To use the Markdown editor CLI, you'll need to have Python 3 installed on your system. You can download Python from the official website: https://www.python.org/downloads/

Once you have Python installed, you can install the `argparse` and `subprocess` modules using pip:

```
pip install argparse subprocess
```

Alternatively, you can install the requirements using the `requirements.txt` file:

```
pip install -r requirements.txt
```

## Usage

To use the Markdown editor CLI, run the `markdown_editor.py` script and specify the filename of the Markdown file you want to edit as an argument:

```
python markdown_editor.py my_file.md
```

This will open `my_file.md` in the default text editor (which is `nano` by default, but can be changed by setting the `EDITOR` environment variable).

You can also specify the editor to use by setting the `EDITOR` environment variable. For example, to use `vim` as the editor, you can run:

```
export EDITOR=vim
python markdown_editor.py my_file.md
```

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request. Please make sure to document any changes you make and include test cases if possible.

## License

This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for details.
