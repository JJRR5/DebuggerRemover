# 🐍 Python & JavaScript Debugger Remover 🛠️

A simple yet effective Python script that helps you clean up your Python and JavaScript code by automatically finding and removing debugger statements. 

## 🌟 Features

- Searches for debugger statements in `.py` and `.js` files
- Prints the path and line number where the debugger was found
- Automatically removes the debugger statements
- Runs in the current directory without requiring user input

## 🚀 Usage

1. Clone this repository or download the `remove_debuggers.py` script.
2. Create an alias for the script to easily run it from any directory. Depending on your operating system, follow the instructions below:

    ### Windows (using PowerShell)
    ```powershell
    Set-Alias -Name remove-debuggers -Value "path\to\remove_debuggers.py"
    ```

    ### macOS and Linux (using Bash)
    ```bash
    echo 'alias remove-debuggers="python /path/to/remove_debuggers.py"' >> ~/.bashrc
    source ~/.bashrc
    ```
3. Navigate to the directory containing your Python and JavaScript files in the terminal or command prompt.
4. Run the script with the following command:

```bash
remove-debuggers
```


The script will automatically search for and remove debugger statements in the current directory and its subdirectories.

⚠️ Warning
This script modifies the files in place. Please make sure you create a backup of your files before running this script to prevent any unintended data loss.

📃 Supported Debugger Statements
Currently, the script supports the following debugger statements:

import pdb; pdb.set_trace()
import ipdb; ipdb.set_trace()
debugger

📚 License
This project is released under the MIT License.

🤝 Contributing
If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request. Your contributions are always welcome! 😊
