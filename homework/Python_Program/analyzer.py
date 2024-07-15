import os
import argparse


def find_text_in_file(file_path, search_text):
    results = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, 1):
            if search_text in line:
                words = line.split()
                search_indices = [i for i, word in enumerate(words) if search_text in word]
                for index in search_indices:
                    start_index = max(0, index - 5)
                    end_index = min(len(words), index + 6)
                    context = " ".join(words[start_index:end_index])
                    results.append((file_path, line_number, context))
    return results


def main():
    parser = argparse.ArgumentParser(description='Search for text in log files.')
    parser.add_argument('log_directory', nargs='?', default=None, help='Path to the log files directory')
    parser.add_argument('--text', type=str, required=True, help='Text to search for in log files')
    args = parser.parse_args()

    if args.log_directory:
        log_directory = args.log_directory
    else:
        base_path = os.path.dirname(__file__)
        log_directory = os.path.join(base_path, 'homework', 'eugene_okulik', 'data', 'logs')

    search_text = args.text

    if not os.path.isdir(log_directory):
        print(f"The directory {log_directory} does not exist")
        return

    all_results = []
    for filename in os.listdir(log_directory):
        file_path = os.path.join(log_directory, filename)
        if os.path.isfile(file_path):
            results = find_text_in_file(file_path, search_text)
            all_results.extend(results)

    if all_results:
        for result in all_results:
            file_path, line_number, context = result
            print(f"Found in {file_path}, line {line_number}: {context}")
    else:
        print(f"No occurrences of '{search_text}' found in the log files.")


if __name__ == "__main__":
    main()
