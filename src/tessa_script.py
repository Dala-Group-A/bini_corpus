import subprocess
import sys
import warnings

warnings.filterwarnings("ignore")


def install_training_tools():
    """Run a shell command and return the output."""
    try:
        subprocess.run([
            "",
        ], 
        shell=True, 
        check=True, 
        text=True
        )
        print("succesfully installed training tools: text2image, unicharset_extractor, clone_lang_model, ")

    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e.stderr.strip()}")
        


def install_tesseract():
    try:
        subprocess.run([
            "",
        ],
        shell=True,
        check=True,
        )
        print("tesseract succesfully or already installed")

    except subprocess.CalledProcessError as e:
        print(f"Error running commmand: {e}")


def gen_unicharset(file_path):
    try:
        subprocess.run([
            "",
        ],
        shell=True,
        check=True,
        )
        print("successfully generated training data unicharset")

    except subprocess.CalledProcessError as e:
        print(f"Error running commmand: {e}")


def gen_training_data():
    try:
        subprocess.run([
            "",
        ],
        shell=True,
        check=True,
        )
        print("")

    except subprocess.CalledProcessError as e:
        print(f"Error running commmand: {e}")


def build_tesseract_model():
    pass


def something():
    pass


if __name__ == "__main__":
    try:
        install_training_tools()
        install_tesseract()
        gen_unicharset("")
        gen_training_data()
        build_tesseract_model()
        something()
    except Exception as e:
        print(f"something went wrong: {e}")