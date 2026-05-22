# Tkinter Demos

A collection of Tkinter GUI examples. `1.py` is a multi-frame student/college login and account-creation interface, and `2.py` is a college-system window with a button menu and a database entry popup.

## Example

**`1.py`** — Student/college login demo:

1. The window opens with a "You are Student or College Authority?" prompt and two buttons.
2. Click "Student" or "College Authority" to proceed to the welcome screen.
3. Click "Create New Account" to open a form with fields for name, email, department, roll number, year, and gender.
4. Click "Login" to open a login form with name and password fields.

**`2.py`** — College system window:

1. A window titled "COLLEGE SYSTEM" opens with a menu of buttons (BOOK buy, BOOK sell, canteen, helpdesk, healthcare, notice, exit).
2. Click any button to print a confirmation message to the terminal (e.g. `success buy`).
3. Click "Database" to open a popup for entering a student name and roll number.

## How to run on localhost

```bash
python 1.py
python 2.py
```

## Dependencies

Standard library only (`tkinter`).
