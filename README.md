# Code Promptify

Code-Promptify is a command-line utility for aggregating code repository contents into a single string based on include and exclude patterns. It also provides metadata information, such as token count and billable characters. It is designed to help you prepare prompts for large language models (LLMs). The output is written to a file and also copied to your clipboard automatically.

**Note**: To count tokens, this tool uses the OpenAI tiktoken tokenizer library and should give you accurate results for most GPT models. For other models (Gemini, Llama, Mistral, etc.) the token count may not be 100% precise but it will be a good approximation. That is because the exact token count depends on the specific tokenizer used by the model, which differs among models. 

See [example_output.md](example_output.md) for what the output looks like for this repo when running with default settings.

Example metadata output:
```
| Field                   | Value           |
|-------------------------|-----------------|
| Tokenizer               | openai/tiktoken |
| Token Count             | 4763            |
| Character Count         | 15695           |
---------------  ---------------
Files included:
└── .
    ├── README.md
    ├── build
    │   └── lib
    │       └── promptify
    │           ├── __init__.py
    │           └── main.py
    ├── example_output.md
    ├── output.md
    ├── promptify
    │   └── __init__.py
    └── requirements.txt
```

## Features

- Aggregate file contents based on include and exclude patterns (glob strings)
- Automatically ignores virtual environment files
- Automatically ignores files where an API key was found 
- Option to ignore empty files 
- Output results to the clipboard automatically (May not work on Linux or Windows)
- Optionally output results to a file

## Installation using PIP
To install promptify, simply run:

```
pip install code-promptify
```

## Installation from Source 

To install Promptify, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/vmehmeri/promptify.git
   cd promptify
   ```

2. Install the package and its dependencies:
   ```
   pip install -e . -r requirements.txt
   ```


## Usage

After installation, you can run Promptify using the following command:

```
promptify [args]
```


### Arguments
- `--include`: File patterns to include (default: `["*.py", "*.html", "*.js", "*.css", "*.json", "*.yaml", "*.txt", "*.md"]`)
- `--exclude`: File patterns to exclude (default: `["*.pyc", "*egg-info*", "*tmp*"]`)
- `--output`: File to write the output to (Optional. Output will be automatically written to a file called `output.promptify` if clipboard copy fails)
- `--ignore-empty`: Flag to Ignore empty files (default: False)
- `--no-skip`: Force-include files where potential API keys are detected (default: False)
- `--export-profile`: Save current filters and options to a named profile
- `--profile`: Load filters and options from a saved profile


### Examples

1. Use default settings:
   ```
   promptify
   ```

2. Include only Python and JavaScript files:
   ```
   promptify --include "*.py" "*.js"
   ```

3. Include all files but exclude test files and ignore empty files:
   ```
   promptify --exclude "*test*" --ignore-empty
   ```

4. Include all Python files except any inside a specific directory:
   ```
   promptify --include "*.py" --exclude "config/*" 
   ```

5. Save current configuration as a profile:
   ```
   promptify --include "*.py" "*.js" --exclude "*test*" --export-profile my-js-py-app
   ```

6. Apply the configuration from a saved profile:
   ```
   promptify --profile my-js-py-config
   ```


## Output
See [example_output.md](example_output.md)

## Dependencies

- pyperclip
- tabulate
- token-count

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

