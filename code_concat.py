"""
Utility script for concating all code sections in a markdown file into a single file.
"""


import os

# import subprocess


md_files_with_python = [
    "docs/getting-started/logging-python.md",
    "docs/getting-started/python.md",
]
md_files_with_rust = ["docs/getting-started/logging-rust.md"]


def extract_strings_between(
    text: str, start_marker: str, end_marker: str, comment_chars: str
) -> str:
    result = ""
    start_index = text.find(start_marker)
    end_index = text.find(end_marker, start_index + len(start_marker))

    while start_index != -1 and end_index != -1:
        result += "\n\n" + comment_chars + " ------------------------------\n\n"
        result += text[start_index + len(start_marker) : end_index] + "\n"
        start_index = text.find(start_marker, end_index + len(end_marker))
        end_index = text.find(end_marker, start_index + len(start_marker))

    return result


def write_code(code: str, origin_file_path: str, extension: str) -> str:
    folder = ".concated_code"

    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = os.path.basename(origin_file_path)
    filename = filename.replace(".md", "." + extension)
    file_path = os.path.join(folder, filename)

    print("Writing out concated code of ", origin_file_path, " to ", file_path)
    with open(file_path, "w") as file:
        file.write(code)
    return file_path


for path in md_files_with_python:
    with open(path, "r") as file:
        contents = file.read()
    python_code = extract_strings_between(contents, "```python", "```", "#")
    code_file = write_code(python_code, path, "py")

    # print("Running ", code_file)
    # result = subprocess.run(["python", code_file], capture_output=True, text=True)
    # print(result.stdout)
    # print(result.stderr)
    # print(result.returncode)

for path in md_files_with_rust:
    with open(path, "r") as file:
        contents = file.read()
    rust_code = extract_strings_between(contents, "```rust", "```", "//")
    code_file = write_code(rust_code, path, "rs")
