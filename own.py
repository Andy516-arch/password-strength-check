import re


def check_strength(password: str) -> dict:
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number")

    if re.search(r"[!@#$%^&*(),.?:<>{}]", password):
        score += 1
    else:
        feedback.append("Add at least one special character")

    return {
        "score": score,
        "feedback": feedback
    }


if __name__ == "__main__":
    password = input("Enter password: ")
    result = check_strength(password)

    print(f"\nScore: {result['score']}/5")

    if result["feedback"]:
        print("Suggestions:")
        for msg in result["feedback"]:
            print("-", msg)
    else:
        print("Strong password ✅")
