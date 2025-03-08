# IP REAPER v1.0

**IP REAPER v1.0** is a Python-based tool designed to extract the sender's IP address from email headers. This tool is intended for educational purposes and works best with self-hosted email addresses. It does not work with emails sent through major email providers like Gmail, Outlook, or Yahoo, as these services mask the sender's IP address.

---

## **Features**
- Extracts the sender's IP address from email headers.
- Works with `.eml` files or raw email headers.
- Drag-and-drop functionality for easy file input.
- Hacker-themed UI for a cool, immersive experience.

---

## **Limitations**
- **Does not work with big email providers**: Emails sent through services like Gmail, Outlook, or Yahoo will only show the provider's server IP addresses, not the sender's actual IP address.
- **Works with self-hosted email addresses**: If the email is sent from a personal email server (e.g., using Postfix or Sendmail), the sender's IP address may appear in the headers.

---

## **Requirements**
- Python 3.x
- `tkinterdnd2` library (for drag-and-drop functionality)
- `email` and `re` libraries (included with Python)

---

## **Setup Instructions**

### **1. Install Python**
- **Linux**:
  ```bash
  sudo apt update
  sudo apt install python3 python3-pip