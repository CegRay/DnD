# DnD parser and Obsidian-md converter

This is a simple parser of some of the directories on [DnD](https://dnd.su/).  
The parser also provides formatters to convert the resulting data into md format for Obsidian

### How to start

1. Edit code in a correspoing way

2. Clone this repository

3. Create virtualenv by command `python -m venv env`

4. Activate virtualenv by command

-   `env\Scripts\activate` for Windows
-   `source env/bin/activate` for Unix-systems

5. Update `pip` and `setuptools` packages

```shell
python -m pip install --upgrade pip
```

```shell
pip install -U setuptools
```

6. Install dependencies

```shell
pip install .
```

-   You can also install dependencies with base proxy (not recomended)

```shell
pip install .[proxy]
```

-   For development install it via command

```shell
pip install -e .[test,lint]
```

7. Edit `config.ini`

-   _base-path_ - basic directory for .md and additional files
-   _is-proxy_ - Bool flag to use/not use proxy
-   _max-concurence_ - The number of workers that will competitively gather information
-   _max-retries_ - The number of retry to get page content
-   _is-remove-additional-files_ - Bool flag to remove/not remove additional files after formatting
-   _[headers]_ - Browser headers

8. You can edit HTML or FILTER consts in `consts.py` file (Be careful)

9. Use command `scrap` to run parsing or `save` to run formatting

### The designation of some files

-   `cli.py` - Program entry points from the command line
-   `utils.py` - Some technical functions
-   `main.py` - Main functions for parsing/formatting
-   `consts.py` - Web consts
