def read_file(filename):
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def removeNonASCII(text):
    clean = ""
    for ch in text:
        if ord(ch) <= 127:
            clean += ch
    return clean

def write_clean(content, original_filename):
    base = original_filename.rsplit(".", 1)[0]
    new_filename = base + "_clean.txt"
    with open(new_filename, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    filename = "textFile.txt"
    contents = read_file(filename)
    cleaned = removeNonASCII(contents)
    write_clean(cleaned, filename)
    
if __name__ == "__main__":
    main()
