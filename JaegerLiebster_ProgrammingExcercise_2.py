from typing import List, Tuple, Set

# list of 30 common spam keywords and phrases
SPAM_KEYWORDS = [
    "action required", "account suspended", "security alert", "confirm your account",
    "unauthorized transaction", "password reset", "invoice attached", "payment due",
    "final notice", "you've won", "congratulations", "lottery", "claim your prize",
    "free gift", "special offer", "limited time", "risk-free", "significant profit",
    "crypto", "bitcoin", "shipping notification", "tracking number", "order #",
    "unsubscribe", "view details", "not junk", "dear friend", "miracle",
    "weight loss", "pharmacy"
]


def scan_message(message: str, spam_keywords: List[str]) -> Tuple[int, List[str]]:
    # scans message for spam keywords, returning a score and list of found words
    score = 0
    found_keywords: Set[str] = set()
    normalized_message = message.lower()

    for keyword in spam_keywords:
        occurrences = normalized_message.count(keyword.lower())
        if occurrences > 0:
            score += occurrences
            found_keywords.add(keyword)

    return score, sorted(list(found_keywords))


def rate_likelihood(score: int) -> str:
    # rates likelihood of message being spam based on its score
    if score == 0:
        return "Very low likelyhood"
    if 1 <= score <= 2:
        return "Low likelihood"
    if 3 <= score <= 5:
        return "Medium likelihood"
    if 6 <= score <= 15:
        return "High likelihood"
    return "Very ligh likelihood!"


def main():
    # runs the main spam checker application
    print("--- Email Spam Checker ---")
    print("Paste your email below (press Enter on an empty line to finish):")

    lines = []
    while True:
        try:
            line = input()
            if not line: break
            lines.append(line)
        except EOFError:
            break

    user_message = "\n".join(lines)
    if not user_message.strip():
        print("\nAnalysis complete: No message entered.")
        return

    spam_score, detected_words = scan_message(user_message, SPAM_KEYWORDS)
    likelihood = rate_likelihood(spam_score)

    print("\n--- Analysis Complete ---")
    print(f"Spam Score: {spam_score}")
    print(f"Likelihood: {likelihood}")
    print(f"Trigger Words Found: {', '.join(detected_words) if detected_words else 'None'}")


if __name__ == "__main__":
    main()