import os

ENTRY = "fix: I asked the bug to review my fix. it approved. we are both lying and we both know it"


def main():
    # An empty MAKEFUN_OUTPUT_DIR is the same as unset; fall back to /output.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write atomically via a temp file so a crash can never leave a
    # half-written entry behind.
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.replace(tmp_path, path)


if __name__ == "__main__":
    main()
