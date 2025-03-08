import tkinter as tk
from tkinter import messagebox
import email
import re
from tkinterdnd2 import TkinterDnD, DND_FILES
import os

# Hacker-themed colors
BG_COLOR = "#000000"
TEXT_COLOR = "#00FF00"
BUTTON_COLOR = "#003300"
FONT = ("Courier", 12)

def extract_ip_from_file(file_path):
    try:
        with open(file_path, "r") as f:
            content = f.read()

        # Try to parse the content as an email
        try:
            msg = email.message_from_string(content)
            headers = msg.as_string()
        except:
            # If parsing as email fails, treat the content as raw headers
            headers = content

        # Extract IP from Received headers
        ip_pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
        received_headers = re.findall(r"Received:.*", headers)
        for header in received_headers:
            ip_match = re.search(ip_pattern, header)
            if ip_match:
                return ip_match.group(0)
        return "IP not found in headers."
    except Exception as e:
        return f"Error: {str(e)}"

def on_drop(event):
    # Get the file path from the event
    file_path = event.data.strip("{}")  # Remove curly braces added by TkinterDnD
    file_path = file_path.strip()  # Remove any extra whitespace

    # Debug: Print the raw file path
    print(f"Raw file path: {file_path}")

    # Check if the file exists
    if not os.path.exists(file_path):
        messagebox.showerror("Error", f"File not found: {file_path}")
        return

    # Debug: Print the resolved file path
    print(f"Resolved file path: {os.path.abspath(file_path)}")

    try:
        ip_address = extract_ip_from_file(file_path)
        result_label.config(text=f"Sender's IP: {ip_address}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to process file: {str(e)}")

# Create the hacker-themed UI
root = TkinterDnD.Tk()  # Use TkinterDnD's Tk instead of tk.Tk
root.title("IP REAPER v1.0 - BY FRANK")
root.configure(bg=BG_COLOR)

# Title label
title_label = tk.Label(root, text="IP REAPER v1.0", font=("Courier", 16, "bold"), fg=TEXT_COLOR, bg=BG_COLOR)
title_label.pack(pady=10)

# Drag-and-drop instructions
instructions_label = tk.Label(root, text="Drag and drop an .eml or plain text file here:", font=FONT, fg=TEXT_COLOR, bg=BG_COLOR)
instructions_label.pack(pady=10)

# Result label
result_label = tk.Label(root, text="Sender's IP: ", font=FONT, fg=TEXT_COLOR, bg=BG_COLOR)
result_label.pack(pady=20)

# Enable drag-and-drop
root.drop_target_register(DND_FILES)
root.dnd_bind("<<Drop>>", on_drop)

# Run the UI
root.mainloop()