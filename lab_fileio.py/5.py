import json
from pathlib import Path
import sys

# The quiz dictionary (copied from Assignment 1 quiz_questions.json)
QUIZ_QUESTIONS = {
    "Normal": {
        "Where is Shilder College of Business located?": {
            "options": [
                "Honolulu, HI",
                "Kailua, HI",
                "Los Angeles, CA",
                "Salt Lake City, UT"
            ],
            "correct": "Honolulu, HI",
            "explanation": "Shidler College of Business is located in Honolulu, Hawaii at the University of Hawaii at Manoa campus."
        },
        "What is Hawaii's State Flower?": {
            "options": [
                "White Lotus",
                "Yellow Hibicus",
                "Pink Rose",
                "Dandelions"
            ],
            "correct": "Yellow Hibicus",
            "explanation": "The Yellow Hibiscus (Ma'o hau hele) has been Hawaii's state flower since 1988."
        },
        "Who was the US President in 1993?": {
            "options": [
                "George W. Bush",
                "Barack Obama",
                "Ronald Reagan",
                "Bill Clinton"
            ],
            "correct": "Bill Clinton",
            "explanation": "Bill Clinton served as the 42nd President of the United States from 1993 to 2001."
        },
        "When was Hawaii officially annexed by the US?": {
            "options": [
                "1905",
                "1898",
                "1895",
                "1912"
            ],
            "correct": "1898",
            "explanation": "Hawaii was officially annexed by the United States on August 12, 1898."
        },
        "How long ago was UH Manoa founded?": {
            "options": [
                "58 years ago",
                "118 years ago",
                "93 years ago",
                "142 years ago"
            ],
            "correct": "118 years ago",
            "explanation": "UH Manoa was founded in 1907, which is approximately 118 years ago from 2025."
        }
    },
    "Extra Credit!": {
        "How long does it take to travel to the moon?": {
            "options": [
                "20 seconds",
                "3 days",
                "6 lightyears",
                "6 months"
            ],
            "correct": "3 days",
            "explanation": "On average, it takes about 3 days for a spacecraft to reach the Moon from Earth."
        }
    }
}


def save_questions(questions: dict, out_path: Path) -> None:
    """Write the questions dict to out_path as pretty JSON.

    This uses indent=4 and ensures ASCII is not forced so Unicode is preserved.
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=4)


def main(argv):
    # Default output file
    repo_root = Path(__file__).resolve().parent
    default_out = repo_root / "quiz_questions_saved.json"

    out_path = Path(argv[1]) if len(argv) > 1 else default_out

    # If there's an existing json source file, prefer loading from it to preserve any edits
    source_file = repo_root / "quiz_questions.json"
    if source_file.exists():
        try:
            with source_file.open("r", encoding="utf-8") as f:
                questions = json.load(f)
            print(f"Loaded questions from existing file: {source_file}")
        except Exception as e:
            print(f"Failed to load {source_file}, falling back to embedded QUIZ_QUESTIONS. Error: {e}")
            questions = QUIZ_QUESTIONS
    else:
        questions = QUIZ_QUESTIONS

    save_questions(questions, out_path)
    # Basic verification output
    total_q = sum(len(cat) for cat in questions.values()) if isinstance(questions, dict) else 0
    print(f"Saved {total_q} questions to {out_path}")


if __name__ == "__main__":
    main(sys.argv)
