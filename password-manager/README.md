# Password Manager

A simple desktop password manager built with Python and Tkinter. Generates random passwords and saves website/email/password entries locally.

## Features

- Generate a random password (mix of letters, numbers, and symbols)
- Auto-copies the generated password to your clipboard
- Save website, email/username, and password entries to a local json file
- Search functionality for existing entries

## Requirements

- Python 3.x
- [`pyperclip`](https://pypi.org/project/pyperclip/)

Install dependencies:

```bash
pip install pyperclip
```

Tkinter usually ships with Python by default. If it's missing on your system (common on some Linux distros), install it via your package manager, e.g. `sudo apt install python3-tk`.

## Usage

1. Make sure `logo.png` is in the same folder as `main.py`.
2. Run the app:

```bash
python main.py
```

3. Enter a website name and email/username.
4. Click **Generate Password** to auto-fill a random password (also copied to your clipboard), or type your own.
5. Click **Add** to save the entry.

Saved entries are stored in `file.json` in the format:

```
{website:{
        "email": email_username,
        "password": password
    }}
```

## ⚠️ Security note

This is a learning project, **not a production-safe password manager**. Passwords are currently saved in **plain text** in `password.txt` — do not use this to store real, sensitive passwords. `password.txt` is excluded via `.gitignore` so your saved entries won't be pushed to GitHub, but the file itself on your machine is still unencrypted.

## Known limitations

- No password encryption at rest
- No way to view/edit/delete saved entries from the UI (must open `password.txt` manually)
- App will crash on launch if `logo.png` is missing

## Roadmap / possible improvements

- [ ] Encrypt stored passwords

