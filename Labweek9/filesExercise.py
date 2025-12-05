def parse_students(path):
    students = []
    with open(path, "r", encoding="utf-8") as f:
        first = True
        for line in f:
            if first:
                first = False
                continue
            parts = [p.strip() for p in line.strip().split(",")]
            if len(parts) >= 2:
                students.append((parts[0], parts[1]))
    return students

def parse_scores(path):
    scores = {}
    with open(path, "r", encoding="utf-8") as f:
        first = True
        for line in f:
            if first:
                first = False
                continue
            parts = [p.strip() for p in line.strip().split(",")]
            if len(parts) >= 3:
                sid, score = parts[0], parts[2]
                try:
                    val = float(score)
                except ValueError:
                    continue
                scores.setdefault(sid, []).append(val)
    return scores

def compute_rows(students, scores_by_id):
    rows = []
    for sid, name in students:
        vals = scores_by_id.get(sid, [])
        total = len(vals)
        ssum = sum(vals)
        avg = (ssum / total) if total > 0 else 0.0
        rows.append([sid, name, str(total), str(int(ssum)), f"{avg:.1f}"])
    return rows

def write_grades(rows, out_path):
    header = ["Student ID", "Name", "Total Scores", "Sum of All Scores", "Score Average"]
    lines = [",".join(header)]
    for r in rows:
        lines.append(",".join(r))
    content = "\n".join(lines)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(content)

def main():
    students = parse_students("students.txt")
    scores = parse_scores("scores.txt")
    rows = compute_rows(students, scores)
    write_grades(rows, "grades.txt")

if __name__ == "__main__":
    main()
