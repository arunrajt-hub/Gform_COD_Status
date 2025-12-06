# GitHub Repository Secrets Configuration Guide

This document outlines all the secrets that need to be configured in your GitHub repository for the G-Form COD Status automation.

## 📋 Required Repository Secrets

To add secrets to your GitHub repository:
1. Go to your repository: https://github.com/arunrajt-hub/Gform_COD_Status
2. Navigate to **Settings** → **Secrets and variables** → **Actions**
3. Click **"New repository secret"**
4. Add each secret listed below

---

## 🔐 Secrets List

### 1. **GMAIL_SENDER_EMAIL**
- **Description**: Gmail address used to send emails
- **Current Value**: `arunraj@loadshare.net`
- **Required**: Yes
- **Example Value**: `your-email@gmail.com`

### 2. **GMAIL_APP_PASSWORD**
- **Description**: Gmail App Password (not regular password)
- **Current Value**: `ihczkvucdsayzrsu` *(Remove from code, use secret only)*
- **Required**: Yes
- **How to Generate**:
  1. Go to Google Account → Security
  2. Enable 2-Step Verification (if not enabled)
  3. Go to App Passwords → Select "Mail" and "Other (Custom name)"
  4. Enter name: "G-Form COD Status"
  5. Copy the 16-character password
- **Note**: This is different from your regular Gmail password

### 3. **GOOGLE_SERVICE_ACCOUNT_JSON**
- **Description**: Complete JSON content of the Google Service Account key file
- **Required**: Yes (for Google Sheets access)
- **Service Account Email**: `emo-reports-automation@single-frame-467107-i1.iam.gserviceaccount.com`
- **How to Add**:
  1. Get your `service_account_key.json` file
  2. Open it in a text editor
  3. Copy the entire JSON content
  4. Paste it as the secret value
- **Format**: Complete JSON object (single-line or multi-line, GitHub will handle it)
- **Example Structure**:
  ```json
  {
    "type": "service_account",
    "project_id": "...",
    "private_key_id": "...",
    "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
    "client_email": "emo-reports-automation@single-frame-467107-i1.iam.gserviceaccount.com",
    ...
  }
  ```

---

## 🔧 Optional Configuration (Environment Variables)

These can be set as secrets if you want to override default values:

### 4. **SPREADSHEET_ID** *(Optional)*
- **Description**: Google Sheets ID (currently hardcoded)
- **Default Value**: `1F5wmvARWLYwZHEwLpM3SxW9R_hbJdInnRDnOdRBp-L0`
- **Required**: No (hardcoded in script)

### 5. **WORKSHEET_NAME** *(Optional)*
- **Description**: Name of the worksheet to read
- **Default Value**: `Status`
- **Required**: No (hardcoded in script)

---

## ⚠️ Security Best Practices

1. **Never commit secrets to code**: The current script has a hardcoded password. Update it to only use environment variables.

2. **Remove hardcoded credentials**: The script currently has:
   - Line 130: Hardcoded `GMAIL_APP_PASSWORD` default value
   - Line 29: Hardcoded service account file path

3. **Use environment variables only**: For production, all secrets should come from environment variables or GitHub Secrets.

---

## 📝 Recommended Updates to Script

### Update Email Configuration Section (Line 128-133)

**Current** (has hardcoded password):
```python
EMAIL_CONFIG = {
    'sender_email': os.getenv('GMAIL_SENDER_EMAIL', 'arunraj@loadshare.net'),
    'sender_password': os.getenv('GMAIL_APP_PASSWORD', 'ihczkvucdsayzrsu'),  # ⚠️ Remove default
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587
}
```

**Recommended**:
```python
EMAIL_CONFIG = {
    'sender_email': os.getenv('GMAIL_SENDER_EMAIL', 'arunraj@loadshare.net'),
    'sender_password': os.getenv('GMAIL_APP_PASSWORD'),  # No default value
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587
}
```

### Update Service Account Configuration (Line 29)

**Current**:
```python
SERVICE_ACCOUNT_FILE = "service_account_key.json"
```

**Recommended** (for GitHub Actions):
```python
SERVICE_ACCOUNT_FILE = os.getenv('GOOGLE_SERVICE_ACCOUNT_FILE', 'service_account_key.json')
# Or create from JSON string:
SERVICE_ACCOUNT_JSON = os.getenv('GOOGLE_SERVICE_ACCOUNT_JSON')
```

---

## 🚀 For GitHub Actions Usage

If you want to run this script via GitHub Actions, you'll need:

1. **All secrets listed above**
2. **GitHub Actions workflow file** (`.github/workflows/gform-cod-status.yml`)
3. **Service account JSON** saved as a secret (not as a file)

The workflow will:
- Use the secrets as environment variables
- Create the service account JSON file from the secret
- Run the script on schedule (9:30 AM and 8:00 PM IST)

---

## ✅ Quick Checklist

- [ ] Add `GMAIL_SENDER_EMAIL` secret
- [ ] Add `GMAIL_APP_PASSWORD` secret
- [ ] Add `GOOGLE_SERVICE_ACCOUNT_JSON` secret (complete JSON content)
- [ ] Remove hardcoded password from script (optional but recommended)
- [ ] Verify Google Sheet is shared with service account email
- [ ] Test email sending functionality

---

## 📚 Additional Resources

- [GitHub Secrets Documentation](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
- [Gmail App Passwords Guide](https://support.google.com/accounts/answer/185833)
- [Google Service Accounts Guide](https://cloud.google.com/iam/docs/service-accounts)

---

**Last Updated**: December 6, 2025

