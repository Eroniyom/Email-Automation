# Email Automation System 📧

Advanced email automation system with bulk email sending, template management, and scheduled sending features.

## 🚀 Features

### ✨ Core Features
- **SMTP Support**: Gmail, Outlook, Yahoo and other SMTP servers
- **Bulk Email**: Load recipient lists from CSV/Excel files
- **Template System**: Customizable email templates
- **Scheduled Sending**: Automatic email sending at specific times
- **Reporting**: Sending status and statistics
- **Security**: Spam protection and delay system

### 📊 Supported Formats
- **CSV**: Comma-separated values
- **Excel**: .xlsx and .xls files
- **HTML**: Rich text format emails
- **Attachments**: Email attachment support

### 🎯 Personalization
- **Variable System**: Dynamic fields like `{name}`, `{email}`, `{company}`
- **Multiple Templates**: Ready templates for different purposes
- **HTML Support**: Rich formatted emails

## 📦 Installation

### Requirements
```bash
pip install -r requirements.txt
```

### Required Libraries
- `smtplib` - Email sending
- `pandas` - Data processing
- `schedule` - Scheduled tasks
- `colorama` - Colored terminal output
- `openpyxl` - Excel file support

## 🚀 Usage

### 1. Start the Program
```bash
python email_automation.py
```

### 2. SMTP Settings
```
SMTP Server: smtp.gmail.com
SMTP Port: 587
Email: your-email@gmail.com
Password: your-app-password
```

### 3. Prepare Recipient List

#### CSV Format:
```csv
name,email,company
John Smith,john@example.com,ABC Company
Jane Doe,jane@example.com,XYZ Ltd.
```

#### Excel Format:
| name | email | company |
|------|-------|---------|
| John Smith | john@example.com | ABC Company |
| Jane Doe | jane@example.com | XYZ Ltd. |

### 4. Create Email Template
```
Subject: Welcome - {name}
Content: Hello {name}, welcome to the {company} family!
```

## 📋 Menu Options

1. **SMTP Settings** - Email server configuration
2. **Load Recipient List** - Load recipients from CSV/Excel file
3. **Add Email Template** - Create new template
4. **Send Single Email** - Send email to single recipient
5. **Send Bulk Emails** - Send to all recipients
6. **Schedule Email** - Automatic sending at specific time
7. **Save Report** - Save sending statistics
8. **Create Sample CSV** - Create sample recipient list

## 🔧 Gmail Setup

### 1. Enable 2FA
- Enable 2-Factor Authentication in your Google Account

### 2. Create App Password
1. Google Account Settings → Security
2. Select "App passwords"
3. Create password for "Email" application
4. Use this password in the program

### 3. SMTP Settings
```
SMTP Server: smtp.gmail.com
SMTP Port: 587
Security: STARTTLS
```

## 📊 Example Use Cases

### 1. Welcome Email
```python
# Template
subject = "Welcome - {name}"
body = "Hello {name}, welcome to the {company} family!"

# CSV data
name,email,company
John Smith,john@example.com,ABC Company
```

### 2. Weekly Newsletter
```python
# Scheduled sending
schedule.every().monday.at("09:00").do(send_newsletter)
```

### 3. Event Reminder
```python
# Personalized content
subject = "Reminder: {event}"
body = "Hello {name}, reminder for {event}..."
```

## 🛡️ Security Measures

### Spam Protection
- Delay between emails (1-5 seconds)
- Maximum recipient limit
- SMTP connection limits

### Error Handling
- Automatic retry on connection errors
- Filter invalid email addresses
- Detailed error logs

## 📈 Reporting

### Sending Report
```json
{
  "sent_emails": [...],
  "failed_emails": [...],
  "total_sent": 150,
  "total_failed": 5,
  "timestamp": "2024-01-15T10:30:00"
}
```

### Statistics
- Successful sending count
- Failed sending count
- Sending duration
- Error details

## 🔧 Advanced Features

### HTML Emails
```html
<html>
<body>
    <h2>Welcome - {name}</h2>
    <p>Hello <strong>{name}</strong>!</p>
    <p>Welcome to the {company} family!</p>
</body>
</html>
```

### Attachments
```python
attachments = ["document.pdf", "image.jpg"]
send_single_email(to, subject, body, attachments=attachments)
```

### Scheduled Tasks
```python
# Every day at 09:00
schedule.every().day.at("09:00").do(send_daily_report)

# Every Monday
schedule.every().monday.do(send_weekly_newsletter)
```

## 🚨 Important Notes

### Legal Warnings
- Don't spam
- Get recipient consent
- Follow email laws
- Protect personal data

### Technical Limits
- Gmail: 500 emails per day
- Outlook: 300 emails per day
- Yahoo: 100 emails per day

### Best Practices
- Send in small groups
- Personalized content
- Regular cleanup
- Feedback tracking

## 🐛 Troubleshooting

### Common Errors

#### "Authentication Failed"
- Enable 2FA
- Use app password
- Check SMTP settings

#### "Connection Refused"
- Check internet connection
- Check firewall settings
- Check SMTP port

#### "Invalid Email"
- Check email format
- Clean invalid characters
- Check DNS records

## 📞 Support

### Developer
- **Eroniyom**
- GitHub: [https://github.com/Eroniyom](https://github.com/Eroniyom)

### Contributing
1. Fork the repository
2. Create feature branch
3. Commit your changes
4. Send pull request

## 📄 License

This project is licensed under the MIT License.

---

**⚠️ Warning**: This tool should only be used for legal purposes. Spamming is prohibited and may result in account closure.