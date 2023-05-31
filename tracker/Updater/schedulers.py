from apscheduler.schedulers.background import BackgroundScheduler
from ..Updater.Helper import CovidTracking


def start():
    print("reached")
    scheduler = BackgroundScheduler()
    mail = CovidTracking()
    scheduler.add_job(mail.ServerRequest(), "interval", seconds=10, id="test_mails_001", replace_existing=True)
    scheduler.start()
