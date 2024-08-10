---
File: `requirements.txt`

vertexai==1.60.0
tabulate==0.9.0
pyperclip==1.9.0

---
File: `setup.py`

```
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="code-promptify",
    version="0.1",
    packages=find_packages(),
    install_requires=required,
    entry_points={
        "console_scripts": [
            "promptify=promptify.main:main",
        ],
    },
    author="Victor Dantas",
    author_email="vmehmeri@hotmail.com",
    description="A CLI utility for aggregating file contents",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/vmehmeri/code-promptify",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
```

---
File: `code_promptify.egg-info/SOURCES.txt`

LICENSE
README.md
setup.py
code_promptify.egg-info/PKG-INFO
code_promptify.egg-info/SOURCES.txt
code_promptify.egg-info/dependency_links.txt
code_promptify.egg-info/entry_points.txt
code_promptify.egg-info/requires.txt
code_promptify.egg-info/top_level.txt
promptify/__init__.py
promptify/main.py

---
File: `code_promptify.egg-info/entry_points.txt`

[console_scripts]
promptify = promptify.main:main


---
File: `code_promptify.egg-info/requires.txt`

vertexai==1.60.0
tabulate==0.9.0
pyperclip==1.9.0


---
File: `code_promptify.egg-info/top_level.txt`

promptify


---
File: `code_promptify.egg-info/dependency_links.txt`




---
File: `promptify/__init__.py`

```

```

---
File: `promptify/main.py`

```
#!/usr/bin/env python3

import os
import fnmatch
import pyperclip
import argparse

from tabulate import tabulate
from vertexai.generative_models import GenerativeModel

_supported_models = ['gemini-1.5-flash', 'gemini-1.5-pro']

def aggregate_file_contents(include_files, exclude_files, ignore_empty_files=False):
    result = []
    current_dir = os.getcwd()

    for root, dirs, files in os.walk(current_dir):
        if 'pyvenv.cfg' in files:
            dirs[:] = []
            continue

        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, current_dir)

            if any(fnmatch.fnmatch(relative_path, pattern) for pattern in include_files) and \
               not any(fnmatch.fnmatch(relative_path, pattern) for pattern in exclude_files):
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                except UnicodeDecodeError:
                    print(f"Warning: Unable to read {relative_path} as UTF-8. Skipping.")
                    continue

                if ignore_empty_files and not content.strip():
                    continue

                result.append(f"---\nFile: `{relative_path}`\n")
                
                code_extensions = ['.py', '.json', '.js', '.html', '.css', '.java', '.cpp', '.c', '.h', '.yaml', '.yml']
                if any(file.endswith(ext) for ext in code_extensions):
                    result.append(f"```\n{content}\n```")
                else:
                    result.append(content)
                
                result.append("")  # Add an empty line between files

    return "\n".join(result)

def get_metadata(model_name, content):
    if model_name not in _supported_models:
        raise ValueError("Model not supported. Supported models are 'gemini-1.5-flash' and 'gemini-1.5-pro'.")
    
    model_response = GenerativeModel(model_name).count_tokens(content)

    metadata = [["Model", model_name],
                ["Token Count", model_response.total_tokens],
                ["Billable Character Count", model_response.total_billable_characters]]
    
    return metadata



def main():
    parser = argparse.ArgumentParser(description="Aggregate file contents based on include and exclude patterns.")
    parser.add_argument('--model', default="gemini-1.5-flash",
                        help="Generative model to use (default: %(default)s)")
    parser.add_argument('--include', nargs='+', default=["*.py", "*.html", "*.js", "*.css", "*.json", "*.yaml", "*.txt", "*.md"],
                        help="File patterns to include (default: %(default)s)")
    parser.add_argument('--exclude', nargs='+', default=["*.pyc", "*egg-info*", "*tmp*"],
                        help="File patterns to exclude (default: %(default)s)")
    parser.add_argument('--ignore-empty', action='store_true',
                        help="Ignore empty files (default: False)")

    args = parser.parse_args()

    output = aggregate_file_contents(args.include, args.exclude, args.ignore_empty)
    metadata = get_metadata(args.model, output)

    print(tabulate(metadata))

    try:
        with open("output.md", "w", encoding="utf-8") as f:
            f.write(output)
        
        print("Output written to output.md")
    except Exception as e:
        print(f"Failed to write to file: {str(e)}")

    try:
        pyperclip.copy(output)
        spam = pyperclip.paste()
        print("Contents copied to clipboard")
    except Exception as e:
        print(f"Failed to copy contents to clipboard: {str(e)}")

if __name__ == "__main__":
    main()
```

---
File: `example/hello.py`

```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)

```

---
File: `example/utils.py/__init__.py`

```

```

---
File: `example/templates/index.html`

```
<!DOCTYPE html>
<html>
<head>
    <title>Hello, World!</title>
</head>
<body>
    <h1>Hello, World!</h1>
</body>
</html>

```

---
File: `build/lib/promptify/__init__.py`

```

```

---
File: `build/lib/promptify/main.py`

```
#!/usr/bin/env python3

import os
import fnmatch
import pyperclip
import argparse

from tabulate import tabulate
from vertexai.generative_models import GenerativeModel

_supported_models = ['gemini-1.5-flash', 'gemini-1.5-pro']

def aggregate_file_contents(include_files, exclude_files, ignore_empty_files=False):
    result = []
    current_dir = os.getcwd()

    for root, dirs, files in os.walk(current_dir):
        if 'pyvenv.cfg' in files:
            dirs[:] = []
            continue

        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, current_dir)

            if any(fnmatch.fnmatch(relative_path, pattern) for pattern in include_files) and \
               not any(fnmatch.fnmatch(relative_path, pattern) for pattern in exclude_files):
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                except UnicodeDecodeError:
                    print(f"Warning: Unable to read {relative_path} as UTF-8. Skipping.")
                    continue

                if ignore_empty_files and not content.strip():
                    continue

                result.append(f"---\nFile: `{relative_path}`\n")
                
                code_extensions = ['.py', '.json', '.js', '.html', '.css', '.java', '.cpp', '.c', '.h', '.yaml', '.yml']
                if any(file.endswith(ext) for ext in code_extensions):
                    result.append(f"```\n{content}\n```")
                else:
                    result.append(content)
                
                result.append("")  # Add an empty line between files

    return "\n".join(result)

def get_metadata(model_name, content):
    if model_name not in _supported_models:
        raise ValueError("Model not supported. Supported models are 'gemini-1.5-flash' and 'gemini-1.5-pro'.")
    
    model_response = GenerativeModel(model_name).count_tokens(content)

    metadata = [["Model", model_name],
                ["Token Count", model_response.total_tokens],
                ["Billable Character Count", model_response.total_billable_characters]]
    
    return metadata



def main():
    parser = argparse.ArgumentParser(description="Aggregate file contents based on include and exclude patterns.")
    parser.add_argument('--model', default="gemini-1.5-flash",
                        help="Generative model to use (default: %(default)s)")
    parser.add_argument('--include', nargs='+', default=["*.py", "*.html", "*.js", "*.css", "*.json", "*.yaml", "*.txt", "*.md"],
                        help="File patterns to include (default: %(default)s)")
    parser.add_argument('--exclude', nargs='+', default=["*.pyc", "*egg-info*", "*tmp*"],
                        help="File patterns to exclude (default: %(default)s)")
    parser.add_argument('--ignore-empty', action='store_true',
                        help="Ignore empty files (default: False)")

    args = parser.parse_args()

    output = aggregate_file_contents(args.include, args.exclude, args.ignore_empty)
    metadata = get_metadata(args.model, output)

    print(tabulate(metadata))

    try:
        with open("output.md", "w", encoding="utf-8") as f:
            f.write(output)
        
        print("Output written to output.md")
    except Exception as e:
        print(f"Failed to write to file: {str(e)}")

    try:
        pyperclip.copy(output)
        spam = pyperclip.paste()
        print("Contents copied to clipboard")
    except Exception as e:
        print(f"Failed to copy contents to clipboard: {str(e)}")

if __name__ == "__main__":
    main()
```