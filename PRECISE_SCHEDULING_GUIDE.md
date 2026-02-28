# Precise Scheduling Guide – Fix GitHub Actions Delays

GitHub Actions scheduled workflows can be delayed by 15–60+ minutes. For **exact** 7 AM and 9 PM IST runs, use an external cron service to trigger the workflow.

---

## Option 1: cron-job.org (Free, recommended)

### Step 1: Create GitHub Personal Access Token

1. Go to **GitHub → Settings → Developer settings → Personal access tokens**
2. Click **Generate new token (classic)**
3. Name: `Gform COD Trigger`
4. Expiry: 90 days or No expiration
5. Scopes: check **`workflow`**
6. Generate and copy the token (you won’t see it again)

### Step 2: Set up cron-job.org

1. Go to [cron-job.org](https://cron-job.org) and create a free account
2. Create a new cron job

**Job 1 – 7 AM IST:**
- **Title:** Gform COD Status – 7 AM
- **URL:**  
  `https://api.github.com/repos/arunrajt-hub/Gform_COD_Status/actions/workflows/gform-cod-status.yml/dispatches`
- **Request method:** POST
- **Schedule:** Custom → `30 1 * * *` (01:30 UTC = 7:00 AM IST)
- **Request headers:**
  - `Authorization`: `Bearer YOUR_GITHUB_TOKEN`
  - `Accept`: `application/vnd.github.v3+json`
  - `Content-Type`: `application/json`
- **Request body (raw JSON):**  
  `{"ref":"main"}`

**Job 2 – 9 PM IST:**
- Same as above, but:
- **Title:** Gform COD Status – 9 PM
- **Schedule:** `30 15 * * *` (15:30 UTC = 9:00 PM IST)

3. Save both jobs

---

## Option 2: Windows Task Scheduler (local machine)

If your PC is on and online at 7 AM and 9 PM IST:

1. Create `trigger_workflow.ps1`:
```powershell
$token = "YOUR_GITHUB_TOKEN"
$headers = @{
    "Authorization" = "Bearer $token"
    "Accept" = "application/vnd.github.v3+json"
}
$body = '{"ref":"main"}'
Invoke-RestMethod -Uri "https://api.github.com/repos/arunrajt-hub/Gform_COD_Status/actions/workflows/gform-cod-status.yml/dispatches" -Method Post -Headers $headers -Body $body -ContentType "application/json"
```

2. In **Task Scheduler**, create two tasks:
   - One at **7:00 AM** daily
   - One at **9:00 PM** daily  
   - Action: Run `powershell.exe -File "C:\path\to\trigger_workflow.ps1"`

---

## Option 3: Keep GitHub schedule (accept delays)

You can leave the built-in `schedule` triggers as is. Runs will usually be within 15–60 minutes of 7 AM and 9 PM IST. No extra setup.

---

## Summary

| Method               | Precision | Cost  | Setup          |
|----------------------|-----------|-------|----------------|
| cron-job.org         | Exact     | Free  | ~5 minutes     |
| Windows Task Scheduler | Exact   | Free  | PC must be on  |
| GitHub schedule only | ±15–60 min | Free | Already in use |

For reliable 7 AM / 9 PM IST delivery, **Option 1 (cron-job.org)** is the best approach.
