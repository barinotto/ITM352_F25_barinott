import json
import sys
from pathlib import Path


def load_questions(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def main(argv):
    repo_dir = Path(__file__).resolve().parent
    default_saved = repo_dir / "quiz_questions_saved.json"
    fallback = repo_dir / "quiz_questions.json"

    if len(argv) > 1:
        in_path = Path(argv[1])
    elif default_saved.exists():
        in_path = default_saved
    elif fallback.exists():
        in_path = fallback
    else:
        print("No quiz JSON found. Expected one of:")
        print(f"  {default_saved}")
        print(f"  {fallback}")
        sys.exit(1)

    try:
        data = load_questions(in_path)
    except Exception as e:
        print(f"Failed to load JSON from {in_path}: {e}")
        sys.exit(2)

    # Pretty-print as JSON to stdout
    print(json.dumps(data, ensure_ascii=False, indent=4))


if __name__ == "__main__":
    main(sys.argv)
