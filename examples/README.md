# Examples

This directory contains example files for the Email Automation System.

## Files

### 📄 `sample_recipients.csv`
Sample recipient list in CSV format with the following columns:
- `name`: Recipient's full name
- `email`: Email address
- `company`: Company name
- `position`: Job position

### 📄 `email_templates.json`
Pre-built email templates including:
- **Welcome**: New employee welcome email
- **Newsletter**: Weekly newsletter template
- **Reminder**: Event reminder template

## Usage

### Using Sample Recipients
1. Copy `sample_recipients.csv` to your project directory
2. Modify the data as needed
3. Load it in the program using option 2

### Using Email Templates
1. Copy `email_templates.json` to your project directory
2. Load templates programmatically or manually add them
3. Use template variables like `{name}`, `{company}`, `{position}`

## Template Variables

Available variables for personalization:
- `{name}`: Recipient's name
- `{email}`: Recipient's email
- `{company}`: Company name
- `{position}`: Job position
- `{date}`: Current date
- `{time}`: Current time
- `{location}`: Event location
- `{event}`: Event name

## Customization

You can customize these examples by:
1. Adding more columns to CSV files
2. Creating new template variables
3. Modifying HTML formatting
4. Adding more template types

## Best Practices

1. **Data Validation**: Always validate email addresses
2. **Personalization**: Use recipient-specific data
3. **Testing**: Test with small groups first
4. **Compliance**: Follow email marketing laws
5. **Security**: Never expose sensitive data
