"""
audit/generate_git_diff_summary.py
Generates a structured line-by-line summary of git diff for all modified files.
"""
import subprocess

TARGET_FILES = [
    "README.md",
    "PROJECT_MASTER_GUIDE.md",
    "paper/abstract.md",
    "paper/main.tex",
    "paper/sections/paper_draft.md",
    "paper/related_work_table.md",
    "paper/literature_comparison.csv",
    "reports/experiment_log.md",
]

def get_diff_summary():
    out_lines = []
    out_lines.append("# Per-File Git Diff Summary (Part 1 & Gap 3 Corrections)\n")
    
    for f in TARGET_FILES:
        res = subprocess.run(["git", "diff", "-U0", f], capture_output=True, text=True)
        diff_text = res.stdout.strip()
        out_lines.append(f"## `{f}`\n")
        if not diff_text:
            out_lines.append("*(No modifications)*\n")
            continue
        
        diff_chunks = []
        curr_chunk = []
        for line in diff_text.splitlines():
            if line.startswith("@@"):
                if curr_chunk:
                    diff_chunks.append("\n".join(curr_chunk))
                    curr_chunk = []
                curr_chunk.append(line)
            elif curr_chunk and (line.startswith("-") or line.startswith("+")):
                curr_chunk.append(line)
        if curr_chunk:
            diff_chunks.append("\n".join(curr_chunk))
        
        for ch in diff_chunks:
            out_lines.append("```diff")
            out_lines.append(ch)
            out_lines.append("```\n")
            
    summary_text = "\n".join(out_lines)
    with open("audit/GIT_DIFF_SUMMARY.md", "w", encoding="utf-8") as out:
        out.write(summary_text)
    print("Written to audit/GIT_DIFF_SUMMARY.md")
    print(summary_text)

if __name__ == "__main__":
    get_diff_summary()

