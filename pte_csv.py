import csv

# File path (Replit friendly)
csv_path = "pte.csv"

# All sections and their tasks
sections = [
    {
        "section": "Speaking",
        "tasks": [
            ["Read Aloud", "Speaking + Reading", "6-7"],
            ["Repeat Sentence", "Speaking + Listening", "7-8"],
            ["Describe Image", "Speaking", "3-4"],
            ["Re-tell Lecture", "Speaking + Listening", "4-5"],
            ["Answer Short Question", "Speaking + Listening", "2-3"]
        ]
    },
    {
        "section": "Writing",
        "tasks": [
            ["Summarize Written Text", "Writing + Reading", "8-10"],
            ["Essay Writing", "Writing", "12-15"]
        ]
    },
    {
        "section": "Reading",
        "tasks": [
            ["Multiple Choice (Single)", "Reading", "1-2"],
            ["Multiple Choice (Multiple)", "Reading", "1-2"],
            ["Re-order Paragraphs", "Reading", "2-3"],
            ["Reading: Fill in the Blanks", "Reading", "4-6"],
            ["Reading & Writing: Fill in Blanks", "Reading + Writing", "6-8"]
        ]
    },
    {
        "section": "Listening",
        "tasks": [
            ["Summarize Spoken Text", "Listening + Writing", "8-10"],
            ["Multiple Choice (Multiple)", "Listening", "1-2"],
            ["Fill in the Blanks", "Listening + Writing", "4-6"],
            ["Highlight Correct Summary", "Listening", "1-2"],
            ["Multiple Choice (Single)", "Listening", "1-2"],
            ["Select Missing Word", "Listening", "1-2"],
            ["Highlight Incorrect Words", "Listening + Reading", "2-3"],
            ["Write from Dictation", "Listening + Writing", "6-8"]
        ]
    }
]

# Write CSV
with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Section", "Task Type", "Skills Tested", "Marks Contribution"])

    for section in sections:
        for task in section["tasks"]:
            writer.writerow([section["section"]] + task)

print(f"CSV file saved as: {csv_path}")
