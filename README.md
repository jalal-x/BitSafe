<div align="center">
<pre>
██████╗░██╗████████╗░██████╗░█████╗░███████╗███████╗
██╔══██╗██║╚══██╔══╝██╔════╝██╔══██╗██╔════╝██╔════╝
██████╦╝██║░░░██║░░░╚█████╗░███████║█████╗░░█████╗░░
██╔══██╗██║░░░██║░░░░╚═══██╗██╔══██║██╔══╝░░██╔══╝░░
██████╦╝██║░░░██║░░░██████╔╝██║░░██║██║░░░░░███████╗
╚═════╝░╚═╝░░░╚═╝░░░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚══════╝
---------------------------------------------------
python secure password manager
</pre>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

Welcome to the BitSafe, a python password manager that allows you to securely manage your passwords using encryption.

## Setup
To use the password manager, make sure you have the required dependencies installed. You can install them using:

```bash
pip install cryptography
pip install getpass
```

# Getting Started

1) Run the script by executing the following command in your terminal:

```bash
python password_manager.py
```

2) Follow the on-screen instructions to set up your master password and initialize the password manager.



# Features
### Add Password

To add a new password entry to your manager, select option 'a' and follow the prompts.
### Edit Passwords

Option 'e' allows you to edit your passwords. You will need to enter your master password and follow the prompts to make changes.
### Generate Password

Generate strong and secure passwords with option 'g'. The generated password can be added to your manager if desired.
### Read Passwords

Option 'r' lets you decrypt and view your stored passwords. Enter your master password to access the decrypted data.

# File Structure

    password_manager.py: The main script file.
    data.json: JSON file to store metadata about the password manager (e.g., whether a master password has been set).
    phrase_key.key: Key file for encrypting the master password.
    secretphrase.txt: File containing the encrypted master password.
    thekey.key: Key file for encrypting the passwords.
    passwords.txt: File containing encrypted password entries.

## Security

This password manager uses the Fernet symmetric key encryption from the cryptography library. The master password and stored passwords are encrypted to enhance security.
# License

Distributed under the MIT license. See ```LICENSE``` for more information.
