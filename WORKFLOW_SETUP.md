# GitHub Actions Workflow Setup Guide

## ✅ Workflow Created Successfully!

The GitHub Actions workflow has been created and pushed to your repository. Here's what you need to know:

## 📍 Where to Find Your Workflows

1. **Go to Actions Tab**: https://github.com/arunrajt-hub/Gform_COD_Status/actions
2. You should now see: **"G-Form COD Status Email Automation"** workflow

## 🔍 Why Workflows Might Not Show Up

If you don't see workflows yet, check:

1. **Refresh the page** - GitHub may take a few seconds to index new workflows
2. **Check the branch** - Workflows must be in the `main` branch (or default branch)
3. **File location** - Workflow files must be in `.github/workflows/` directory
4. **File extension** - Must be `.yml` or `.yaml`
5. **Syntax errors** - Invalid YAML will prevent workflows from showing

## 🚀 Current Status

✅ **Workflow file created**: `.github/workflows/gform-cod-status.yml`  
✅ **Pushed to GitHub**: Yes  
✅ **Should be visible**: Immediately after push (may take a few seconds)

## 📅 Workflow Schedule

The workflow is configured to run:
- **Daily at 9:30 AM IST** (04:00 UTC)
- **Daily at 8:00 PM IST** (14:30 UTC)

**Note**: GitHub Actions schedules may have slight delays (up to 15 minutes).

## 🧪 Testing the Workflow

You can manually trigger the workflow:

1. Go to: https://github.com/arunrajt-hub/Gform_COD_Status/actions
2. Click on **"G-Form COD Status Email Automation"**
3. Click **"Run workflow"** button (top right)
4. Select branch: `main`
5. Click **"Run workflow"**

## ⚠️ Before First Run

Make sure you've added all required secrets:

- [ ] `GMAIL_SENDER_EMAIL`
- [ ] `GMAIL_APP_PASSWORD`
- [ ] `GOOGLE_SERVICE_ACCOUNT_JSON`

See [GITHUB_SECRETS.md](GITHUB_SECRETS.md) for detailed instructions.

## 🔧 Workflow Triggers

The workflow will run automatically on:

1. **Schedule**: Twice daily (9:30 AM & 8:00 PM IST)
2. **Manual**: Click "Run workflow" button
3. **Push**: When `G-Form_COD_Status.py` or workflow file is updated

## 📊 Viewing Workflow Runs

1. Go to Actions tab
2. Click on a workflow run to see:
   - Execution status
   - Logs for each step
   - Artifacts (log files)
   - Duration and timing

## ❌ Common Issues

### Workflow not appearing?
- Wait a few seconds and refresh
- Check you're on the correct repository
- Verify the workflow file is in `.github/workflows/`

### Workflow failing?
- Check that all secrets are configured
- Review the logs in the Actions tab
- Verify Google Sheet permissions
- Check Gmail App Password is correct

### Schedule not running?
- GitHub Actions schedules can be delayed
- First run after creating schedule may take up to 24 hours
- Verify cron syntax is correct (UTC time)

## 📝 Workflow File Location

```
.github/
└── workflows/
    ├── gform-cod-status.yml  ← Main workflow file
    └── README.md              ← Workflow documentation
```

## 🎯 Next Steps

1. ✅ Verify workflow is visible in Actions tab
2. ✅ Add all required secrets (see GITHUB_SECRETS.md)
3. ✅ Test workflow manually using "Run workflow" button
4. ✅ Monitor scheduled runs at 9:30 AM and 8:00 PM IST

---

**Workflow is ready!** Go to the Actions tab to see it:  
https://github.com/arunrajt-hub/Gform_COD_Status/actions

