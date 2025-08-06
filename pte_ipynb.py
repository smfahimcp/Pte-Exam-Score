import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell

# Create a notebook with enhanced styling to mimic PDF design
nb = new_notebook(cells=[
    # Global CSS for overall styling
    new_markdown_cell("""\
<style>
body {
  font-family: Helvetica, Arial, sans-serif;
  line-height: 1.5;
  padding: 20px;
}
h1 {
  font-size: 28pt;
  margin-bottom: 12px;
}
h2 {
  font-size: 18pt;
  margin-top: 24px;
  margin-bottom: 8px;
  color: #333;
}
p.intro {
  font-size: 12pt;
  margin-bottom: 16px;
}
table {
  width: 90%;
  border-collapse: collapse;
  margin-top: 8px;
  margin-bottom: 16px;
}
th, td {
  border: 2px solid #666;
  padding: 12px 10px;
  text-align: center;
  font-size: 12pt;
}
th {
  background-color: #d3d3d3;
  font-weight: bold;
}
tbody tr:nth-child(odd) {
  background-color: #f2f2f2;
}
</style>"""),
    # Title
    new_markdown_cell("# 📄 PTE Exam Score Distribution and Section-wise Marking Guide"),
    # Intro paragraph
    new_markdown_cell('<p class="intro">The Pearson Test of English (PTE) Academic is assessed out of <b>90 marks</b>. Your performance is scored across four main communicative skills: Speaking, Writing, Reading, and Listening. Below is a structured breakdown with indicative mark ranges for each task type.</p>'),
    # Speaking section
    new_markdown_cell("""\
## 1. Speaking (Approx. 25–30 marks)
<table>
  <tr><th>Task Type</th><th>Skills Tested</th><th>Marks</th></tr>
  <tr><td>Read Aloud</td><td>Speaking + Reading</td><td>6–7</td></tr>
  <tr><td>Repeat Sentence</td><td>Speaking + Listening</td><td>7–8</td></tr>
  <tr><td>Describe Image</td><td>Speaking</td><td>3–4</td></tr>
  <tr><td>Re-tell Lecture</td><td>Speaking + Listening</td><td>4–5</td></tr>
  <tr><td>Answer Short Question</td><td>Speaking + Listening</td><td>2–3</td></tr>
</table>"""),
    # Writing section
    new_markdown_cell("""\
## 2. Writing (Approx. 20–25 marks)
<table>
  <tr><th>Task Type</th><th>Skills Tested</th><th>Marks</th></tr>
  <tr><td>Summarize Written Text</td><td>Writing + Reading</td><td>8–10</td></tr>
  <tr><td>Essay Writing</td><td>Writing</td><td>12–15</td></tr>
</table>"""),
    # Reading section
    new_markdown_cell("""\
## 3. Reading (Approx. 15–20 marks)
<table>
  <tr><th>Task Type</th><th>Skills Tested</th><th>Marks</th></tr>
  <tr><td>Multiple Choice (Single)</td><td>Reading</td><td>1–2</td></tr>
  <tr><td>Multiple Choice (Multiple)</td><td>Reading</td><td>1–2</td></tr>
  <tr><td>Re-order Paragraphs</td><td>Reading</td><td>2–3</td></tr>
  <tr><td>Reading: Fill in the Blanks</td><td>Reading</td><td>4–6</td></tr>
  <tr><td>Reading & Writing: Fill in Blanks</td><td>Reading + Writing</td><td>6–8</td></tr>
</table>"""),
    # Listening section
    new_markdown_cell("""\
## 4. Listening (Approx. 20–25 marks)
<table>
  <tr><th>Task Type</th><th>Skills Tested</th><th>Marks</th></tr>
  <tr><td>Summarize Spoken Text</td><td>Listening + Writing</td><td>8–10</td></tr>
  <tr><td>Multiple Choice (Multiple)</td><td>Listening</td><td>1–2</td></tr>
  <tr><td>Fill in the Blanks</td><td>Listening + Writing</td><td>4–6</td></tr>
  <tr><td>Highlight Correct Summary</td><td>Listening</td><td>1–2</td></tr>
  <tr><td>Multiple Choice (Single)</td><td>Listening</td><td>1–2</td></tr>
  <tr><td>Select Missing Word</td><td>Listening</td><td>1–2</td></tr>
  <tr><td>Highlight Incorrect Words</td><td>Listening + Reading</td><td>2–3</td></tr>
  <tr><td>Write from Dictation</td><td>Listening + Writing</td><td>6–8</td></tr>
</table>"""),
    # Note
    new_markdown_cell("> **Note:** The actual contribution of marks may vary slightly depending on test versions. Focus on improving integrated tasks to boost multiple areas simultaneously.")
])

# Write the notebook to disk
with open("PTE.ipynb", "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

"Generated styled notebook: PTE.ipynb"
