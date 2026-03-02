def print_text_to_console(text):
    """
    Outputs text to the console.
    Args:
        text: Text to be printed."""
    print(text)

def write_text_file_builtin(file_path, text):
    """
    Writes text to a file using built-in Python functionality.
    Args:
        file_path: Path to the file.
        text: Text to write."""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)

def write_text_file_pandas(file_path, data):
    """
    Writes data to a file using the pandas library.

    Args:
        file_path (str): Path to the file.
        data (pandas.DataFrame): Data to be written using pandas.
    """
    data.to_csv(file_path, index=False)