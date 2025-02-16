import os
import json


async def extract_titles_from_markdown_files(input_folder, output_file_path):
    index = {}

    for dirpath, _, filenames in os.walk(input_folder):
        for filename in filenames:
            if filename.endswith(".md"):
                current_file_path = os.path.join(dirpath, filename)
                with open(current_file_path, "r", encoding="utf-8") as file:
                    for line in file:
                        if line.startswith("# "):
                            title = line[2:].strip()
                            relative_file_path = os.path.relpath(current_file_path, input_folder)
                            normalized_path = relative_file_path.replace("\\", "/")
                            index[normalized_path] = title
                            break

    with open(output_file_path, "w", encoding="utf-8") as output_file:
        json.dump(index, output_file, indent=4)


# Example usage
if __name__ == "__main__":
    input_directory = "/data/docs/"
    output_index_file = "/data/docs/index.json"
    extract_titles_from_markdown_files(input_directory, output_index_file)
