from apscheduler.schedulers.background import BackgroundScheduler
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from datetime import datetime
from automatedblog import main_job


def start(request, *args, **kwargs) -> HttpResponseRedirect:
    """Runs daily checkup for a beginning of new month"""
    scheduler = BackgroundScheduler()
    scheduler.add_job(main_job.main_script, 'interval', start_date=datetime.today(), minutes=10, max_instances=1)
    scheduler.start()
    return redirect('home')
