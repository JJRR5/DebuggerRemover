import os

DEBUGGER_STATEMENTS = ["import pdb; pdb.set_trace()", "import ipdb; ipdb.set_trace()", "debugger"]

def find_files_with_debuggers(root_dir):
    for root, _, filenames in os.walk(root_dir):
        target_files = [f for f in filenames if f.endswith('.py') or f.endswith('.js')]
        for filename in target_files:
            file_path = os.path.join(root, filename)
            with open(file_path, 'r') as file:
                lines = file.readlines()
                modified = False

                for index, line in enumerate(lines):
                    for debugger in DEBUGGER_STATEMENTS:
                        if debugger in line:
                            print(f"Debugger found in {file_path} at line {index + 1} 😁")
                            lines[index] = line.replace(debugger, "")
                            modified = True

                if modified:
                    with open(file_path, 'w') as file:
                        file.writelines(lines)
    if not modified:
        print("No debuggers found 🤔")


if __name__ == "__main__":
    directory = os.getcwd()
    find_files_with_debuggers(directory)
