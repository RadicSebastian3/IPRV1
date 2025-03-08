import tkinter as tk
from tkinter import messagebox
import smtplib
import re

# Hacker-themed colors
BG_COLOR = "#000000"
TEXT_COLOR = "#00FF00"
BUTTON_COLOR = "#003300"
FONT = ("Courier", 12)

def get_ip_from_email(email):
    try:
        # Extract domain from email
        domain = email.split('@')[1]
        
        # Connect to the domain's mail server
        server = smtplib.SMTP(domain)
        server.set_debuglevel(1)  # Enable debug to capture headers
        
        # Send a test email to trigger header logging
        server.sendmail(email, email, "Subject: IP Extraction Test")
        
        # Capture the debug output
        debug_output = server.get_debuglevel()
        server.quit()
        
        # Extract IP from debug output
        ip_pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
        ip_match = re.search(ip_pattern, str(debug_output))
        
        if ip_match:
            return ip_match.group(0)
        else:
            return "IP not found in headers."
    except Exception as e:
        return f"Error: {str(e)}"

def on_submit():
    email = entry.get()
    if "@" not in email:
        messagebox.showerror("Error", "Invalid email address.")
        return
    
    ip_address = get_ip_from_email(email)
    result_label.config(text=f"IP Address: {ip_address}")

# Create the hacker-themed UI
root = tk.Tk()
root.title("FRANK'S EMAIL IP EXTRACTOR")
root.configure(bg=BG_COLOR)

# Title label
title_label = tk.Label(root, text="FRANK'S EMAIL IP EXTRACTOR", font=("Courier", 16, "bold"), fg=TEXT_COLOR, bg=BG_COLOR)
title_label.pack(pady=10)

# Email entry
entry_label = tk.Label(root, text="Enter Email Address:", font=FONT, fg=TEXT_COLOR, bg=BG_COLOR)
entry_label.pack(pady=5)
entry = tk.Entry(root, font=FONT, bg=BG_COLOR, fg=TEXT_COLOR, insertbackground=TEXT_COLOR)
entry.pack(pady=10)

# Submit button
submit_button = tk.Button(root, text="Extract IP", font=FONT, bg=BUTTON_COLOR, fg=TEXT_COLOR, command=on_submit)
submit_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="IP Address: ", font=FONT, fg=TEXT_COLOR, bg=BG_COLOR)
result_label.pack(pady=20)

# Run the UI
root.mainloop()