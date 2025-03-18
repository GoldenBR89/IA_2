import os

def setup_directories():
    os.makedirs("data", exist_ok=True)
    os.makedirs("processed_editais", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

def log_processed_file(filename):
    with open("processed_editais/processed.txt", "a") as f:
        f.write(f"{filename}\n")

def is_file_processed(filename):
    if not os.path.exists("processed_editais/processed.txt"):
        return False
    with open("processed_editais/processed.txt", "r") as f:
        return filename in f.read()