# Email Automation Configuration
# Developed by: Eroniyom

# Gmail SMTP Settings
GMAIL_SMTP_SERVER = "smtp.gmail.com"
GMAIL_SMTP_PORT = 587

# Outlook SMTP Settings
OUTLOOK_SMTP_SERVER = "smtp-mail.outlook.com"
OUTLOOK_SMTP_PORT = 587

# Yahoo SMTP Settings
YAHOO_SMTP_SERVER = "smtp.mail.yahoo.com"
YAHOO_SMTP_PORT = 587

# Default settings
DEFAULT_DELAY_SECONDS = 2  # Delay between emails (spam protection)
MAX_RECIPIENTS_PER_BATCH = 50  # Maximum recipients per batch

# Email templates
DEFAULT_TEMPLATES = {
    "welcome": {4
    9
        "subject": "Welcome - {name}",
        "body": """Hello {name},

Welcome to the {company} family!

We are sharing special information with you through this email.

Best regards,
Email Automation System""",
        "html_body": """
        <html>
        <body>
            <h2>Welcome - {name}</h2>
            <p>Hello <strong>{name}</strong>,</p>
            <p>Welcome to the <strong>{company}</strong> family!</p>
            <p>We are sharing special information with you through this email.</p>
            <p>Best regards.</p>
            <br>
            <p>Best regards,<br>
            Email Automation System</p>
        </body>
        </html>
        """
    },
    
    "newsletter": {
        "subject": "Weekly Newsletter - {date}",
        "body": """Hello {name},

This week's important developments:

• Information about our new products
• Special campaigns
• Event announcements

Visit our website for details.

Best regards,
Team""",
        "html_body": """
        <html>
        <body>
            <h2>Weekly Newsletter - {date}</h2>
            <p>Hello <strong>{name}</strong>,</p>
            <p>This week's important developments:</p>
            <ul>
                <li>Information about our new products</li>
                <li>Special campaigns</li>
                <li>Event announcements</li>
            </ul>
            <p>Visit our website for details.</p>
            <p>Best regards,<br>Team</p>
        </body>
        </html>
        """
    },
    
    "reminder": {
        "subject": "Reminder: {event}",
        "body": """Hello {name},

This is a reminder email for {event}.

Date: {date}
Time: {time}
Location: {location}

We look forward to your participation.

Best regards,
Organization Team""",
        "html_body": """
        <html>
        <body>
            <h2>Reminder: {event}</h2>
            <p>Hello <strong>{name}</strong>,</p>
            <p>This is a reminder email for <strong>{event}</strong>.</p>
            <table border="1" cellpadding="5">
                <tr><td><strong>Date:</strong></td><td>{date}</td></tr>
                <tr><td><strong>Time:</strong></td><td>{time}</td></tr>
                <tr><td><strong>Location:</strong></td><td>{location}</td></tr>
            </table>
            <p>We look forward to your participation.</p>
            <p>Best regards,<br>Organization Team</p>
        </body>
        </html>
        """
    }
}

# Error messages
ERROR_MESSAGES = {
    "smtp_not_configured": "SMTP settings not configured!",
    "no_recipients": "Recipient list is empty!",
    "template_not_found": "Template not found!",
    "invalid_email": "Invalid email address!",
    "connection_failed": "Could not connect to SMTP server!",
    "authentication_failed": "Email authentication failed!",
    "file_not_found": "File not found!",
    "permission_denied": "File access permission denied!"
}

# Success messages
SUCCESS_MESSAGES = {
    "smtp_configured": "SMTP settings configured successfully!",
    "recipients_loaded": "Recipient list loaded successfully!",
    "template_added": "Template added successfully!",
    "email_sent": "Email sent successfully!",
    "bulk_send_completed": "Bulk email sending completed!",
    "report_saved": "Report saved successfully!"
}