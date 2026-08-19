grade_book = {
    "Paul": 85,
    "Jack": 78,
    "Cody": 89,
    "Corbin": 96,
    "Bob": 80
}

total_score = 0
for score in grade_book.values():
    total_score += score

class_average = total_score / len(grade_book)

top_scorer = max(grade_book, key=grade_book.get)
bottom_scorer = min(grade_book, key=grade_book.get)

print("--- Class Statistics ---")
print(f"Class Average: {class_average:.2f}")
print(f"Top Scorer: {total_score} ({grade_book[top_scorer]})")
print(f"Bottom Scorer: {bottom_scorer} ({grade_book}[bottom_scorer])")
print("-" * 24)
print("---------------------------------\n")

while True:
    search_name = input("Enter a students name to look up there grades ").strip()

    if search_name.lower