# query parameters (payload)
appid = 'fe059ce4c2a38cb3be061fb0ddb4625f'


def callByLongitudeLatitude(lon, lat):
    return {'lat': lat, 'lon': lon, 'appid': appid}


def callByCityName(city):
    return {'q': city, 'appid': appid}


def callByZipcode(zipcode):
    return {'zip': zipcode, 'appid': appid}
