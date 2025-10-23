# Student Management System

A Python Tkinter-based Student Management System to manage student records, monthly payments, and export CSV/PDF reports.

## Features
- Add / Update / Delete / Search student records
- Track monthly payments (Jan–Dec)
- Export to CSV and PDF
- Print generated PDF reports
- Simple GUI using Tkinter

## Tech Stack
- Python 3
- Tkinter (GUI)
- SQLite3 (database)
- FPDF (PDF generation)

## Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/student-management-system.git
   cd student-management-system
2. (Optional)create a virtual environment:
   ```bash
    python -m venv venv
    source venv/bin/activate   # macOS/Linux
    venv\Scripts\activate      # Windows
3. (Optional) Create a virtual environment :
   ```bash
   python -m venv venv
   venv\Scripts\activate     # For Windows
   # or
   source venv/bin/activate  # For macOS/Linux
5. Install required dependencies :
   ```bash
   pip install fpdf reportlab

## Usage
Run the main Python file to start the application:
  ```bash
  python main.py
```
Once the program opens, use the GUI buttons to:
- Add or update student records
- Search student details
- Manage monthly payments
- Export or print reports

## Project Structure
``` brash
student-management-system/
│
├── main.py                 # Main Python application
├── database.db             # SQLite database file
├── requirements.txt        # Required packages
├── README.md               # Project documentation
└── assets/                 # Images, icons, etc.
```

## Contributing
Contributions are welcome!
If you’d like to improve this project, please:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Submit a pull request

## License
This project is licensed under the MIT License.
You’re free to use, modify, and distribute it with attribution.

## Author
Developed by: Sayon Mitra
📧 Email: sayonmitracode@gmail.com

🌐 GitHub: https://github.com/sayon_mitra024

