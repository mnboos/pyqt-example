from pathlib import Path
import subprocess


def main():
    for file in Path("ui").glob("*.ui"):
        print(f"Compiling: {file}")
        new_name = file.stem.replace(".", "_")
        target = file.parent / "build" / f"{new_name}.py"
        subprocess.call(f"python -m PyQt5.uic.pyuic {file} -o {target}")


if __name__ == '__main__':
    main()
