import smtplib
import csv
import pandas as pd
import schedule
import time
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import colorama
from colorama import Fore, Style, init
import json
from typing import List, Dict, Optional

# Initialize colorama
init()

class EmailAutomation:
    def __init__(self):
        self.smtp_server = None
        self.smtp_port = None
        self.email = None
        self.password = None
        self.recipients = []
        self.templates = {}
        self.sent_emails = []
        self.failed_emails = []
        
    def setup_smtp(self, smtp_server: str, smtp_port: int, email: str, password: str):
        """Configure SMTP settings"""
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email = email
        self.password = password
        print(f"{Fore.GREEN}[+] SMTP settings configured{Style.RESET_ALL}")
        
    def load_recipients_from_csv(self, csv_file: str):
        """Load recipient list from CSV file"""
        try:
            df = pd.read_csv(csv_file)
            self.recipients = df.to_dict('records')
            print(f"{Fore.GREEN}[+] {len(self.recipients)} recipients loaded{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[ERROR] Error loading CSV file: {e}{Style.RESET_ALL}")
            
    def load_recipients_from_excel(self, excel_file: str, sheet_name: str = None):
        """Load recipient list from Excel file"""
        try:
            df = pd.read_excel(excel_file, sheet_name=sheet_name)
            self.recipients = df.to_dict('records')
            print(f"{Fore.GREEN}[+] {len(self.recipients)} recipients loaded{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[ERROR] Error loading Excel file: {e}{Style.RESET_ALL}")
            
    def add_template(self, name: str, subject: str, body: str, html_body: str = None):
        """Add email template"""
        self.templates[name] = {
            'subject': subject,
            'body': body,
            'html_body': html_body
        }
        print(f"{Fore.GREEN}[+] Template added: {name}{Style.RESET_ALL}")
        
    def personalize_email(self, template: Dict, recipient: Dict) -> Dict:
        """Personalize email"""
        subject = template['subject']
        body = template['body']
        html_body = template.get('html_body', '')
        
        # Replace personalization variables
        for key, value in recipient.items():
            placeholder = f"{{{key}}}"
            subject = subject.replace(placeholder, str(value))
            body = body.replace(placeholder, str(value))
            if html_body:
                html_body = html_body.replace(placeholder, str(value))
                
        return {
            'subject': subject,
            'body': body,
            'html_body': html_body
        }
        
    def send_single_email(self, to_email: str, subject: str, body: str, 
                         html_body: str = None, attachments: List[str] = None):
        """Send single email"""
        try:
            msg = MIMEMultipart('alternative')
            msg['From'] = self.email
            msg['To'] = to_email
            msg['Subject'] = subject
            
            # Text version
            text_part = MIMEText(body, 'plain', 'utf-8')
            msg.attach(text_part)
            
            # HTML version (if available)
            if html_body:
                html_part = MIMEText(html_body, 'html', 'utf-8')
                msg.attach(html_part)
                
            # Attachments (if any)
            if attachments:
                for attachment in attachments:
                    if os.path.exists(attachment):
                        with open(attachment, "rb") as f:
                            part = MIMEBase('application', 'octet-stream')
                            part.set_payload(f.read())
                            encoders.encode_base64(part)
                            part.add_header(
                                'Content-Disposition',
                                f'attachment; filename= {os.path.basename(attachment)}'
                            )
                            msg.attach(part)
            
            # Send email
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.email, self.password)
            text = msg.as_string()
            server.sendmail(self.email, to_email, text)
            server.quit()
            
            print(f"{Fore.GREEN}[+] Email sent: {to_email}{Style.RESET_ALL}")
            return True
            
        except Exception as e:
            print(f"{Fore.RED}[ERROR] Failed to send email ({to_email}): {e}{Style.RESET_ALL}")
            return False
            
    def send_bulk_emails(self, template_name: str, delay_seconds: int = 1):
        """Send bulk emails"""
        if template_name not in self.templates:
            print(f"{Fore.RED}[ERROR] Template not found: {template_name}{Style.RESET_ALL}")
            return
            
        template = self.templates[template_name]
        success_count = 0
        fail_count = 0
        
        print(f"{Fore.CYAN}[*] Starting bulk email sending...{Style.RESET_ALL}")
        
        for recipient in self.recipients:
            if 'email' not in recipient:
                print(f"{Fore.YELLOW}[!] Email address not found: {recipient}{Style.RESET_ALL}")
                continue
                
            personalized = self.personalize_email(template, recipient)
            
            if self.send_single_email(
                recipient['email'],
                personalized['subject'],
                personalized['body'],
                personalized.get('html_body')
            ):
                success_count += 1
                self.sent_emails.append({
                    'email': recipient['email'],
                    'subject': personalized['subject'],
                    'timestamp': datetime.now().isoformat()
                })
            else:
                fail_count += 1
                self.failed_emails.append({
                    'email': recipient['email'],
                    'error': 'Sending failed',
                    'timestamp': datetime.now().isoformat()
                })
                
            # Add delay (for spam protection)
            time.sleep(delay_seconds)
            
        print(f"{Fore.GREEN}[+] Bulk sending completed!{Style.RESET_ALL}")
        print(f"{Fore.GREEN}   Successful: {success_count}{Style.RESET_ALL}")
        print(f"{Fore.RED}   Failed: {fail_count}{Style.RESET_ALL}")
        
    def schedule_email(self, template_name: str, send_time: str, delay_seconds: int = 1):
        """Schedule email"""
        schedule.every().day.at(send_time).do(
            self.send_bulk_emails, template_name, delay_seconds
        )
        print(f"{Fore.GREEN}[+] Email scheduled: {send_time}{Style.RESET_ALL}")
        
    def run_scheduler(self):
        """Run scheduler"""
        print(f"{Fore.CYAN}[*] Scheduler running... (Press Ctrl+C to stop){Style.RESET_ALL}")
        while True:
            schedule.run_pending()
            time.sleep(1)
            
    def save_report(self, filename: str = None):
        """Save report"""
        if not filename:
            filename = f"email_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            
        report = {
            'sent_emails': self.sent_emails,
            'failed_emails': self.failed_emails,
            'total_sent': len(self.sent_emails),
            'total_failed': len(self.failed_emails),
            'timestamp': datetime.now().isoformat()
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
            
        print(f"{Fore.GREEN}[+] Report saved: {filename}{Style.RESET_ALL}")
        
    def create_sample_csv(self, filename: str = "sample_recipients.csv"):
        """Create sample CSV file"""
        sample_data = [
            {'name': 'John Smith', 'email': 'john@example.com', 'company': 'ABC Company'},
            {'name': 'Jane Doe', 'email': 'jane@example.com', 'company': 'XYZ Ltd.'},
            {'name': 'Mike Johnson', 'email': 'mike@example.com', 'company': 'DEF Corp.'}
        ]
        
        df = pd.DataFrame(sample_data)
        df.to_csv(filename, index=False, encoding='utf-8')
        print(f"{Fore.GREEN}[+] Sample CSV file created: {filename}{Style.RESET_ALL}")

def main():
    """Main program"""
    print(f"{Fore.CYAN}")
    print("=" * 60)
    print("           EMAIL AUTOMATION SYSTEM")
    print("           Developed by: Eroniyom")
    print("=" * 60)
    print(f"{Style.RESET_ALL}")
    
    automation = EmailAutomation()
    
    while True:
        print(f"\n{Fore.YELLOW}MENU:{Style.RESET_ALL}")
        print("1. SMTP Settings")
        print("2. Load Recipient List")
        print("3. Add Email Template")
        print("4. Send Single Email")
        print("5. Send Bulk Emails")
        print("6. Schedule Email")
        print("7. Save Report")
        print("8. Create Sample CSV")
        print("9. Exit")
        
        choice = input(f"\n{Fore.GREEN}Your choice (1-9): {Style.RESET_ALL}")
        
        if choice == "1":
            smtp_server = input("SMTP Server (e.g.: smtp.gmail.com): ")
            smtp_port = int(input("SMTP Port (e.g.: 587): "))
            email = input("Your email address: ")
            password = input("Your email password: ")
            automation.setup_smtp(smtp_server, smtp_port, email, password)
            
        elif choice == "2":
            file_type = input("File type (csv/excel): ").lower()
            filename = input("File name: ")
            if file_type == "csv":
                automation.load_recipients_from_csv(filename)
            elif file_type == "excel":
                automation.load_recipients_from_excel(filename)
                
        elif choice == "3":
            name = input("Template name: ")
            subject = input("Subject: ")
            print("Email content (press Enter to finish):")
            body = ""
            while True:
                line = input()
                if line == "":
                    break
                body += line + "\n"
            automation.add_template(name, subject, body)
            
        elif choice == "4":
            to_email = input("Recipient email: ")
            subject = input("Subject: ")
            print("Email content (press Enter to finish):")
            body = ""
            while True:
                line = input()
                if line == "":
                    break
                body += line + "\n"
            automation.send_single_email(to_email, subject, body)
            
        elif choice == "5":
            if not automation.templates:
                print(f"{Fore.RED}[ERROR] Please add email template first!{Style.RESET_ALL}")
                continue
            print("Available templates:")
            for i, name in enumerate(automation.templates.keys(), 1):
                print(f"{i}. {name}")
            template_name = input("Template name: ")
            delay = int(input("Delay (seconds, recommended: 1-5): "))
            automation.send_bulk_emails(template_name, delay)
            
        elif choice == "6":
            if not automation.templates:
                print(f"{Fore.RED}[ERROR] Please add email template first!{Style.RESET_ALL}")
                continue
            print("Available templates:")
            for i, name in enumerate(automation.templates.keys(), 1):
                print(f"{i}. {name}")
            template_name = input("Template name: ")
            send_time = input("Send time (HH:MM format): ")
            automation.schedule_email(template_name, send_time)
            automation.run_scheduler()
            
        elif choice == "7":
            automation.save_report()
            
        elif choice == "8":
            automation.create_sample_csv()
            
        elif choice == "9":
            print(f"{Fore.GREEN}Program terminating...{Style.RESET_ALL}")
            break
            
        else:
            print(f"{Fore.RED}Invalid choice!{Style.RESET_ALL}")

if __name__ == "__main__":
    main()