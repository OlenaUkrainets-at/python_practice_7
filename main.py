from app.io.input import text_console, read_file_builtin, read_file_pandas
from app.io.output import print_text_to_console, write_text_file_builtin, write_text_file_pandas

def main():
    user_text = text_console()
    print_text_to_console(f"Ваш текст: {user_text}")
    write_text_file_builtin("console_output.txt", user_text)
    try:
        file_content = read_file_builtin("test.txt")
        print_text_to_console(f"Вміст файлу: {file_content}")
        write_text_file_builtin("copy_test.txt", file_content)
    except FileNotFoundError:
        print("Файл test.txt не знайдено")

    try:
        df = read_file_pandas("data.csv")
        print_text_to_console("Дані з Pandas:")
        print_text_to_console(df.to_string()) # Виводимо таблицю
        write_text_file_pandas("output_pandas.csv", df)
    except FileNotFoundError:
        print("Файл data.csv не знайдено")

if __name__ == '__main__':
    main()
