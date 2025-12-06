"""
Scheduler script to run G-Form COD Status automation daily at 9:30 AM and 8:00 PM IST
This script runs continuously and executes the main script at scheduled intervals

Usage:
    python schedule_G-Form_COD_Status.py

Note: This script needs to run continuously. Consider using Windows Task Scheduler
to run this script as a service, or use the batch file + Task Scheduler method instead.
"""

import schedule
import time
import subprocess
import logging
import sys
import os
from datetime import datetime
import pytz

# Configure logging
log_file = os.path.join(os.path.dirname(__file__), 'G-Form_COD_Status_scheduler_log.txt')
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

# IST timezone
IST = pytz.timezone('Asia/Kolkata')

def get_ist_time():
    """Get current time in IST"""
    return datetime.now(IST)

def run_cod_status():
    """Run the G-Form COD Status script"""
    ist_time = get_ist_time()
    logging.info("="*80)
    logging.info(f"Starting scheduled G-Form COD Status automation at {ist_time.strftime('%Y-%m-%d %H:%M:%S IST')}...")
    logging.info("="*80)
    
    try:
        # Get the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))
        cod_status_script = os.path.join(script_dir, 'G-Form_COD_Status.py')
        
        # Run the script
        result = subprocess.run(
            [sys.executable, cod_status_script],
            cwd=script_dir,
            capture_output=True,
            text=True,
            timeout=1800  # 30 minutes timeout
        )
        
        if result.returncode == 0:
            logging.info("✅ G-Form COD Status automation completed successfully!")
            if result.stdout:
                # Log key output lines
                for line in result.stdout.split('\n'):
                    if any(keyword in line for keyword in ['✅', 'ERROR', '❌', 'INFO']):
                        logging.info(f"   {line}")
        else:
            logging.error(f"❌ G-Form COD Status automation failed with return code {result.returncode}")
            if result.stderr:
                logging.error(f"Error output: {result.stderr}")
            if result.stdout:
                logging.error(f"Standard output: {result.stdout}")
        
    except subprocess.TimeoutExpired:
        logging.error("❌ G-Form COD Status automation timed out after 30 minutes")
    except Exception as e:
        logging.error(f"❌ Error running G-Form COD Status automation: {e}")
        import traceback
        logging.error(traceback.format_exc())
    
    ist_time_end = get_ist_time()
    logging.info(f"Completed at {ist_time_end.strftime('%Y-%m-%d %H:%M:%S IST')}")
    logging.info("="*80)

def main():
    """Main scheduler function"""
    logging.info("="*80)
    logging.info("🚀 G-Form COD Status Scheduler Started")
    logging.info("="*80)
    ist_time = get_ist_time()
    logging.info(f"Current IST time: {ist_time.strftime('%Y-%m-%d %H:%M:%S IST')}")
    logging.info("Schedule:")
    logging.info("   • Daily at 09:30 IST (9:30 AM)")
    logging.info("   • Daily at 20:00 IST (8:00 PM)")
    logging.info("="*80)
    
    # Schedule the job to run at 9:30 AM IST daily
    schedule.every().day.at("09:30").do(run_cod_status)
    
    # Schedule the job to run at 8:00 PM IST daily
    schedule.every().day.at("20:00").do(run_cod_status)
    
    # Note: The schedule library uses local time by default
    # Since the user is in IST timezone, this should work correctly
    # If there are timezone issues, we may need to adjust
    
    logging.info("⏰ Scheduler running... Waiting for scheduled times...")
    logging.info("Press Ctrl+C to stop the scheduler")
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    except KeyboardInterrupt:
        logging.info("\n" + "="*80)
        logging.info("🛑 Scheduler stopped by user")
        logging.info("="*80)

if __name__ == "__main__":
    main()

