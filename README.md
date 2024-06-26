# Invoice PDF Generator

This project is a simple script to convert Excel invoices into PDF format. It reads invoice data from Excel files located in the `invoices` directory and generates corresponding PDF files in the `PDFs` directory.

## Requirements

To install the required packages, run:

```bash
pip install -r requirements.txt
```
## Project Structure
- `invoices/`: Directory containing Excel invoice files.
- `PDFs/`: Directory where the generated PDF files will be saved.
- `pythonhow.png`: Image file used in the PDF generation.
- `requirements.txt`: File containing the required Python packages.
- `lets_code.py`: Main script to generate PDFs from Excel files.

## How to Run
1. Ensure you have all the required packages installed by running the following command:

```sh
pip install -r requirements.txt
```
2. Place your Excel invoice files in the invoices directory. The filenames should follow the format invoiceNr-date.xlsx (e.g., 1234-2023-01-01.xlsx).

3. Run the script:

```sh
python generate_pdfs.py
```
4. The generated PDF files will be saved in the PDFs directory.
