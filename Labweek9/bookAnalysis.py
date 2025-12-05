def analyzeBook(filename):
    count = {}
    punct = '_,.".-?!\'():[];{}+*/\\<>|`~^#$%&@='
    table = str.maketrans({ch: " " for ch in punct})
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            s = line.translate(table).lower()
            for word in s.split():
                if word.isalpha():
                    count[word] = count.get(word, 0) + 1
    return count

def outputAnalysis(count, filename):
    title = filename.rsplit(".", 1)[0]
    outname = f"{title}_analysis.txt"
    keys = sorted(count.keys())
    with open(outname, "w", encoding="utf-8") as out:
        for word in keys:
            out.write(f"{word} {count[word]}\n")

def main():
    filename = "textFile_clean.txt"
    counts = analyzeBook(filename)
    outputAnalysis(counts, filename)

if __name__ == "__main__":
    main()
