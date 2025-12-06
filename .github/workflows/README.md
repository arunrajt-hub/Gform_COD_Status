# GitHub Actions Workflows

This directory contains GitHub Actions workflows for automating the G-Form COD Status email reports.

## Workflow: `gform-cod-status.yml`

### Schedule
- **9:30 AM IST** (04:00 UTC) - Daily
- **8:00 PM IST** (14:30 UTC) - Daily

### Manual Trigger
You can manually trigger the workflow from the GitHub Actions tab by clicking "Run workflow".

### Required Secrets
Before the workflow can run, make sure you've added these secrets to your repository:

1. `GMAIL_SENDER_EMAIL` - Gmail address for sending emails
2. `GMAIL_APP_PASSWORD` - Gmail App Password
3. `GOOGLE_SERVICE_ACCOUNT_JSON` - Complete JSON content from service account key file

See the main [GITHUB_SECRETS.md](../GITHUB_SECRETS.md) file for detailed instructions.

### How It Works

1. **Checkout** - Downloads the repository code
2. **Set up Python** - Installs Python 3.11
3. **Install dependencies** - Installs packages from `requirements.txt`
4. **Create service account key** - Creates the JSON file from secret
5. **Run script** - Executes `G-Form_COD_Status.py`
6. **Upload logs** - Saves any log files as artifacts (optional)

### Viewing Workflow Runs

1. Go to: https://github.com/arunrajt-hub/Gform_COD_Status/actions
2. Click on a workflow run to see logs and status
3. Download artifacts (logs) if needed

### Troubleshooting

- **Workflow not running?** - Check that secrets are added correctly
- **Permission errors?** - Verify Google Sheet is shared with service account email
- **Email not sending?** - Check Gmail App Password is correct
- **Schedule not working?** - GitHub Actions schedules may have delays, verify cron syntax

### Timezone Notes

- IST = UTC + 5:30
- Cron schedules are in UTC time
- 9:30 AM IST = 04:00 UTC
- 8:00 PM IST = 14:30 UTC

