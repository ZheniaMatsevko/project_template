import app.io.input as i
import app.io.output as o


def main():
    # Read from console
    console_input = i.read_from_console("Enter some text from console: ")
    print("Text read from console:", console_input)

    file_content = i.read_from_file("data/test.txt")
    if file_content is not None:
        print("Text read from file:")
        print(file_content)

        with open("output_from_file.txt", "w") as output_file:
            output_file.write(file_content)
            print("Text written to output_from_file.txt")

    # Read from file using Pandas
    dataframe = i.read_from_file_with_pandas("data/test.csv")
    if dataframe is not None:
        print("Data read from file using Pandas:")
        print(dataframe)

        # Write to file using Pandas
        dataframe.to_csv("output_from_pandas.csv", index=False)
        print("Data written to output_from_pandas.csv")

    output_text_file_name = './data/output.txt'
    output_csv_file_name = './data/output.csv'

    filepath = i.read_from_console('Enter a file path to read from: ')
    o.write_to_console(filepath)

    file_content = i.read_from_file(filepath)
    o.write_to_file(file_content, output_text_file_name)

    csv_filepath = i.read_from_console('Enter a .csv file path to read from: ')
    df = i.read_from_file_with_pandas(csv_filepath)
    o.write_dataframe_to_file(df, output_csv_file_name)


if __name__ == "__main__":
    main()
