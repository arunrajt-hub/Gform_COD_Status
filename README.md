# G-Form COD Status Email Automation

Automated email reporting system for G-Form COD Status that extracts data from Google Sheets and sends formatted HTML emails with status information.

## Features

- 📊 Extracts data from Google Sheets (G-Form COD Status)
- 📧 Sends formatted HTML emails with status reports
- 🎨 Beautiful, responsive email template with color coding
- 📱 Mobile-friendly design
- ⏰ Automated scheduling (9:30 AM and 8:00 PM IST daily)
- 🔄 Status text abbreviations for compact display (Up-Accepted, Not-Up)

## Requirements

- Python 3.7+
- Google Sheets API access
- Gmail App Password for email sending

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/Gform_COD_Status.git
cd Gform_COD_Status
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Set up Google Sheets service account:
   - Create a service account in Google Cloud Console
   - Download the service account JSON key file
   - Share the Google Sheet with the service account email

4. Configure environment variables:
   - `GMAIL_SENDER_EMAIL`: Your Gmail address
   - `GMAIL_APP_PASSWORD`: Gmail App Password
   - `GOOGLE_SERVICE_ACCOUNT_FILE`: Path to service account JSON file

## Configuration

### Email Recipients

The script automatically sends emails to:
- **TO**: All hub emails, CLM emails, Lokesh, Bharath, and Maligai Rasmeen
- **CC**: Rakib

Recipients are configured in the script's `HUB_EMAIL`, `CLM_EMAIL`, and `get_email_recipients()` function.

### Google Sheet Setup

1. Share the Google Sheet with the service account email: `emo-reports-automation@single-frame-467107-i1.iam.gserviceaccount.com`
2. Ensure the sheet has a worksheet named "Status"
3. The sheet should have "Hub Name" column and date columns

## Usage

### Manual Run

```bash
python G-Form_COD_Status.py
```

### Scheduled Run

Run the scheduler script to automate daily runs at 9:30 AM and 8:00 PM IST:

```bash
python schedule_G-Form_COD_Status.py
```

The scheduler runs continuously. For production, consider using Windows Task Scheduler or a service manager.

## Email Format

- **Subject**: `South - COD (Gform) - Status - {Date} {Time}`
- **Content**: HTML table with:
  - Hub Name column
  - Latest 4 days status columns
  - Status color coding (Green: Up-Accepted, Red: Not-Up, Yellow: CMS Absent, Orange: Pending)
  - Compliance % row

## Status Text Abbreviations

- `Uploaded-Accepted` → `Up-Accepted`
- `Not Uploaded` → `Not-Up`

## Files

- `G-Form_COD_Status.py`: Main automation script
- `schedule_G-Form_COD_Status.py`: Scheduler script for automated runs
- `requirements.txt`: Python dependencies

## License

This project is for internal use at LoadShare Networks.

