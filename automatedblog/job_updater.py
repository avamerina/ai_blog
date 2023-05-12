from apscheduler.schedulers.background import BackgroundScheduler
from django.http import HttpResponse
from django.shortcuts import redirect

from automatedblog import main_job


def start(request, *args, **kwargs) -> HttpResponse:
    """Runs daily checkup for a beginning of new month"""
    scheduler = BackgroundScheduler()
    scheduler.add_job(main_job.main_script, 'interval', minutes=5, max_instances=1)
    scheduler.start()
    return redirect('home')
