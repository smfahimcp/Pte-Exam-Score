from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

pdf_path = "PTE.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4)
styles = getSampleStyleSheet()
elements = []

title = Paragraph("<b>PTE Exam Score Distribution and Section-wise Marking Guide</b>", styles["Title"])
elements.append(title)
elements.append(Spacer(1, 12))

intro = Paragraph("The Pearson Test of English (PTE) Academic is assessed out of <b>90 marks</b>. Your performance is scored across four main communicative skills: Speaking, Writing, Reading, and Listening. Below is a structured breakdown with indicative mark ranges for each task type.", styles["BodyText"])
elements.append(intro)
elements.append(Spacer(1, 12))

elements.append(Paragraph("<b>1. Speaking (Approx. 25–30 marks)</b>", styles["Heading2"]))
speaking_data = [
    ["Task Type", "Skills Tested", "Marks Contribution"],
    ["Read Aloud", "Speaking + Reading", "6-7"],
    ["Repeat Sentence", "Speaking + Listening", "7-8"],
    ["Describe Image", "Speaking", "3-4"],
    ["Re-tell Lecture", "Speaking + Listening", "4-5"],
    ["Answer Short Question", "Speaking + Listening", "2-3"],
]
speaking_table = Table(speaking_data, hAlign='LEFT')
speaking_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#d3d3d3")),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')
]))
elements.append(speaking_table)
elements.append(Spacer(1, 12))

elements.append(Paragraph("<b>2. Writing (Approx. 20–25 marks)</b>", styles["Heading2"]))
writing_data = [
    ["Task Type", "Skills Tested", "Marks Contribution"],
    ["Summarize Written Text", "Writing + Reading", "8-10"],
    ["Essay Writing", "Writing", "12-15"],
]
writing_table = Table(writing_data, hAlign='LEFT')
writing_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#d3d3d3")),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')
]))
elements.append(writing_table)
elements.append(Spacer(1, 12))

elements.append(Paragraph("<b>3. Reading (Approx. 15–20 marks)</b>", styles["Heading2"]))
reading_data = [
    ["Task Type", "Skills Tested", "Marks Contribution"],
    ["Multiple Choice (Single)", "Reading", "1-2"],
    ["Multiple Choice (Multiple)", "Reading", "1-2"],
    ["Re-order Paragraphs", "Reading", "2-3"],
    ["Reading: Fill in the Blanks", "Reading", "4-6"],
    ["Reading & Writing: Fill in Blanks", "Reading + Writing", "6-8"],
]
reading_table = Table(reading_data, hAlign='LEFT')
reading_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#d3d3d3")),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')
]))
elements.append(reading_table)
elements.append(Spacer(1, 12))

elements.append(Paragraph("<b>4. Listening (Approx. 20–25 marks)</b>", styles["Heading2"]))
listening_data = [
    ["Task Type", "Skills Tested", "Marks Contribution"],
    ["Summarize Spoken Text", "Listening + Writing", "8-10"],
    ["Multiple Choice (Multiple)", "Listening", "1-2"],
    ["Fill in the Blanks", "Listening + Writing", "4-6"],
    ["Highlight Correct Summary", "Listening", "1-2"],
    ["Multiple Choice (Single)", "Listening", "1-2"],
    ["Select Missing Word", "Listening", "1-2"],
    ["Highlight Incorrect Words", "Listening + Reading", "2-3"],
    ["Write from Dictation", "Listening + Writing", "6-8"],
]
listening_table = Table(listening_data, hAlign='LEFT')
listening_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#d3d3d3")),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold')
]))
elements.append(listening_table)
elements.append(Spacer(1, 12))

note = Paragraph("Note: The actual contribution of marks may vary slightly depending on test versions. Focus on improving integrated tasks to boost multiple areas simultaneously.", styles["Italic"])
elements.append(note)

doc.build(elements)
pdf_path
