from functools import wraps
import requests
import json

def CheckVPN(*args, **kwargs):
    raise Exception("Function Not Finished")


def RequireVPN(*Dargs, **Dkwargs):
    def decorator(function):
        @wraps(function)
        def wrapper(*Fargs, **Fkwargs):
            RequirementsPassed = []

            r = requests.get(IPAPI).json()

            if "IP" in Dkwargs:
                if r['query'] == Dkwargs['IP']:
                    RequirementsPassed.append(True)

            if "Mobile" in Dkwargs:
                if r['mobile'] == Dkwargs['Mobile']:
                    RequirementsPassed.append(True)

            if "Proxy" in Dkwargs:
                if r['proxy'] == Dkwargs['Proxy']:
                    RequirementsPassed.append(True)

            if "Hosting" in Dkwargs:
                if r['hosting'] == Dkwargs['Hosting']:
                    RequirementsPassed.append(True)

            if "Reverse" in Dkwargs:
                if r['reverse'] == Dkwargs['Reverse']:
                    RequirementsPassed.append(True)

            if "ASName" in Dkwargs:
                if r['asname'] == Dkwargs['ASName']:
                    RequirementsPassed.append(True)

            if "AS" in Dkwargs:
                if r['as'] == Dkwargs['AS']:
                    RequirementsPassed.append(True)

            if "ISP" in Dkwargs:
                if r['isp'] == Dkwargs['ISP']:
                    RequirementsPassed.append(True)

            if "UTCOffset" in Dkwargs:
                if r['offset'] == Dkwargs['UTCOffset']:
                    RequirementsPassed.append(True)

            if "Continent" in Dkwargs:
                if r['continent'] == Dkwargs['Continent']:
                    RequirementsPassed.append(True)

            if "Country" in Dkwargs:
                if r['country'] == Dkwargs['Country']:
                    RequirementsPassed.append(True)

            if "City" in Dkwargs:
                if r['city'] == Dkwargs['City']:
                    RequirementsPassed.append(True)

            if "ZIP" in Dkwargs:
                if r['zip'] == Dkwargs['ZIP']:
                    RequirementsPassed.append(True)


            if len(RequirementsPassed) == len(Dkwargs):
                return function(*Fargs, **Fkwargs)
            else:
                raise Exception("Requirements Not Passed")
        return wrapper
    return decorator
