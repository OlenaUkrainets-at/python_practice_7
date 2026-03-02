import pandas as pd

def text_console() -> str:
    """
    Reads text from the console.
    Returns:
        str: Text entered by the user."""
    return input("Введіть текст: ")

def read_file_builtin(file_path:str) -> str:
    """
    Reads text from a file using Python built-in functionality.
    Args:
        file_path: Path to the input file.
    Returns:
        str: Content of the file as a string."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def read_file_pandas(file_path):
    """
    Reads data from a file using the pandas library.
    Args:
        file_path: Path to the input file.
    Returns:
        pandas.DataFrame: Data read from the file."""
    return pd.read_csv(file_path)
