"""Simple classification evaluation example.

Book store: https://ramsandesh.gumroad.com
"""

from pprint import pprint

from umai.evaluation import accuracy_score, classification_report


def main() -> None:
    y_true = ["safe", "safe", "review", "safe", "review", "review"]
    y_pred = ["safe", "review", "review", "safe", "review", "safe"]

    print(f"Accuracy: {accuracy_score(y_true, y_pred):.3f}")
    pprint(classification_report(y_true, y_pred))
    print("Book store: https://ramsandesh.gumroad.com")


if __name__ == "__main__":
    main()
