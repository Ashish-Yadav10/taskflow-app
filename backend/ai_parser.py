import re

def mock_ai_parse(description: str) -> dict:
    original_text = description
    lower_text = description.lower()

    # Priority determination
    priority = "medium"
    high_keywords = ["urgent", "asap"]
    low_keywords = ["whenever", "low priority"]

    has_high = any(kw in lower_text for kw in high_keywords)
    has_low = any(kw in lower_text for kw in low_keywords)

    if has_high:
        priority = "high"
    elif has_low:
        priority = "low"

    # Due-date hint extraction (in strict priority order)
    date_candidates = [
        "today",
        "tomorrow",
        "next week",
        "next monday", "next tuesday", "next wednesday", "next thursday", "next friday", "next saturday", "next sunday",
        "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"
    ]

    due_date_hint = None
    matched_date_span = None

    for candidate in date_candidates:
        match = re.search(r'\b' + re.escape(candidate) + r'\b', lower_text)
        if match:
            due_date_hint = candidate
            matched_date_span = match.span()
            break

    # Title parsing
    # Spans to remove from original_text
    all_keywords_to_remove = high_keywords + low_keywords
    spans_to_remove = []

    for kw in all_keywords_to_remove:
        for match in re.finditer(r'\b' + re.escape(kw) + r'\b', lower_text):
            spans_to_remove.append(match.span())

    if matched_date_span:
        spans_to_remove.append(matched_date_span)

    # Sort spans by start index
    spans_to_remove.sort(key=lambda x: x[0])

    # Reconstruct title by omitting matched spans
    title_chars = []
    last_idx = 0
    for start, end in spans_to_remove:
        if start >= last_idx:
            title_chars.append(original_text[last_idx:start])
            last_idx = max(last_idx, end)
    title_chars.append(original_text[last_idx:])

    raw_title = "".join(title_chars)
    # Clean up multiple whitespaces
    clean_title = re.sub(r'\s+', ' ', raw_title).strip()

    if not clean_title:
        clean_title = "Untitled task"

    return {
        "title": clean_title,
        "priority": priority,
        "due_date_hint": due_date_hint
    }
