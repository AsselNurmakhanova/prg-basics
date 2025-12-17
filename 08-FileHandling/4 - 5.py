import re
file = 'email.txt'
with open(file, 'r') as f:
    email = f.read()
def email_sender(email):
    pattern = r'^From:.*<([^>]+)>'
    match = re.search(pattern, email, re.MULTILINE)
    if match:
        return match.group(1)
    return None
def email_recipient(email):
    pattern = r'^To:.*<([^>]+)>'
    match = re.search(pattern, email, re.MULTILINE)
    if match:
        return match.group(1)
    return None
def email_subject(email):
    pattern = r'^Subject:\s*(.*)'
    match = re.search(pattern, email, re.MULTILINE)
    if match:
        return match.group(1)
    return None
def email_body(email):
    # тело идёт после пустой строки после заголовков
    parts = email.split('\n\n', 1)
    if len(parts) > 1:
        return parts[1]
    return None
print("Sender:", email_sender(email))
print("Recipient:", email_recipient(email))
print("Subject:", email_subject(email))
print("Body:\n", email_body(email))