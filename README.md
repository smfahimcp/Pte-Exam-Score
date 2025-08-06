# 📄 PTE Exam Score Breakdown Generator

Welcome to the **PTE Exam Score Breakdown Generator**, a lightweight Python tool for creating professional-grade documents from your Pearson Test of English (PTE) scores. Use it to generate polished PDF reports, flexible CSV/Markdown exports, or an interactive Jupyter Notebook—all with minimal setup.

## 🚀 Features

- **Polished PDF Reports**  
  Produces a visually appealing PDF (`PTE.pdf`) with custom headers, table styling, and alternating row colors to match high-end design standards.
- **Flexible Exports**  
  Outputs the same data as `PTE.csv` and `PTE.md` for easy sharing, analysis, or integration with other tools.
- **Interactive Notebook**  
  Includes a ready-to-run `PTE.ipynb` for live edits, previews, and direct PDF exports.
- **Minimal Dependencies**  
  Built with only `reportlab`, `nbformat`, and Python’s standard library—no heavy frameworks.
- **Replit & Local Friendly**  
  Works seamlessly on Replit or your local machine without path issues.


## 🛠️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/smfahimcp/Pte-Exam-Score
   cd Pte-Exam-Score
   ```
2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # Linux/macOS
   venv\Scripts\activate     # Windows
   ```
3. Install the required packages:

   ```bash
   pip install reportlab nbformat
   ```

## ⚙️ Quick Start

1. **Generate the PDF**:

   ```bash
   python pte_pdf.py
   ```
2. **Export CSV**:

   ```bash
   python pte_csv.py
   ```
3. **Generate the Interactive Notebook**:

   ```bash
   python pte_ipynb.py
   ```
4. **Run the Interactive Notebook**:

   ```bash
   jupyter notebook pte.ipynb
   ```

 
## 📂 Project Layout
```
├── pte_pdf.py      # Generate PDF
├── pte_csv.py      # Exports data to PTE.csv 
├── pte_ipynb.py    # Builds interactive Jupyter 
|                     Notebook
├── PTE.ipynb       # Interactive report notebook
├── PTE.md          # Markdown report
├── PTE.csv         # CSV data file
├── PTE.pdf         # Generated PDF report
├── LICENSE         # Project license
└── README.md       # Project overview and 
                      instructions
```

## 📄 License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.

---
## Author

Made with ❤️ by [@smfahimcp](https://github.com/smfahimcp)
