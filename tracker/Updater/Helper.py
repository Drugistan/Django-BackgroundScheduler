import requests
from tracker.models import Covid


class CovidTracking:

    def ServerRequest(self):
        url_ = "https://api.covidtracking.com/v1/us/daily.json"
        request_ = None
        try:
            request_ = requests.get(url_)
        except Exception as e:
            print(e)

        response = request_.json()
        print(response)
        if response:
            for indices in response:
                self.create_db(indices)
            status = True
            message = "Covid Data is Fetch Successfully"
            return status, message
        else:
            status = False
            message = "Something Went Wrong"
            return status, message

    def create_db(self, response):
        Covid.objects.create(date=response['date'],
                             states=response['states'],
                             positive=response['positive'],
                             negative=response['negative'],
                             pending=response['pending'],
                             hospitalizedCurrently=response['hospitalizedCurrently'],
                             hospitalizedCumulative=response['hospitalizedCumulative'],
                             inIcuCurrently=response['inIcuCurrently'],
                             inIcuCumulative=response['inIcuCumulative'],
                             onVentilatorCurrently=response['onVentilatorCurrently'],
                             onVentilatorCumulative=response['onVentilatorCumulative'],
                             dateChecked=response['dateChecked'],
                             death=response['death'],
                             hospitalized=response['hospitalized'],
                             totalTestResults=response['totalTestResults'],
                             lastModified=response['lastModified'],
                             recovered=response['recovered'],
                             total=response['total'],
                             posNeg=response['posNeg'],
                             deathIncrease=response['deathIncrease'],
                             hospitalizedIncrease=response['hospitalizedIncrease'],
                             negativeIncrease=response['negativeIncrease'],
                             positiveIncrease=response['positiveIncrease'],
                             totalTestResultsIncrease=response['totalTestResultsIncrease']
                             )
