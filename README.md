# Factory Worker Attendance System

A command-line program written in Python that helps track the attendance of factory workers. You can add workers, mark them present, view worker details, check an individual attendance summary, and get an alert for workers whose attendance is below 75%.

## Features

- Add a worker (ID, name, department, shift)
- Mark attendance for a worker by ID
- Display all workers with their present and absent days
- View the attendance summary and percentage of one worker
- Attendance alert for all workers (below 75% is flagged)

## Requirements

- Python 3.8 or higher
- No external libraries are needed (only Python's built-in features are used)

Check your Python version:

```bash
python --version
```

## Setup and Run

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
   cd YOUR-REPO-NAME
   ```

2. (Optional) Create a virtual environment:

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux / macOS
   source venv/bin/activate
   ```

3. Install dependencies (there are none, but this keeps the setup standard):

   ```bash
   pip install -r requirements.txt
   ```

4. Run the program:

   ```bash
   python vityarthi1.py
   ```

   On some Linux/macOS systems use `python3 vityarthi1.py`.

## Configuration

No configuration or environment variables are needed. All data is stored in memory while the program runs and is cleared when you exit.

## How to Use

When the program starts, a menu is shown:

```
1. Add worker
2. Mark Attendance
3. Display Workers
4. Attendance Summary
5. Attendance Alert
6. Exit
```

Type the number of the option and press Enter.

### Sample run

```
Enter your choice1
Enter worker ID:101
Enter worker name:Ravi
Enter department:Assembly
Enter shift:Morning
Worker added successfully!:

Enter your choice2
Enter worker ID :101
Enter attendance (P/A)P
Attendance marked present sucessfully:

Enter your choice4
Enter worker id:101
==========ATTENDANCE SUMMARY===========
Worker name: Ravi
Present Days: 1
Absent Days ; 0
Total Days: 1
Attendance 100.0 %
```

## Project Structure

```
.
├── vityarthi1.py      # main program
├── requirements.txt   # dependencies (none required)
├── README.md          # this file
└── .gitignore         # files Git should ignore
```

## Limitations

- Data is not saved to a file, so it is lost when the program closes.
- Worker IDs are not checked for duplicates.
