import requests
import allure_behave
from behave import *
from utilities.configurations import *
from utilities.resources import *
from utilities import payload


@given('the Weather API (URL), API KEY and {city}')
def step_impl(context, city):
    context.url = getConfig()['API']['endpoint'] + ApiResources.getWeatherData
    context.cityName = payload.callByCityName(city=city)  # payload


@when('a user queries the URL by the city name')
def step_impl(context):
    context.response = requests.get(url=context.url, params=context.cityName)
    context.json_response = context.response.json()


@then('the name attribute in the response body should correspond to the entered {city}')
def step_impl(context, city):
    assert context.json_response.get('name') == city


# REUSED STEP DEFINITION FOR STATUS CODE VALIDATION OF EACH CALL IN THIS STEP IMPLEMENTATION FILE
@then('the status code should be {statusCode:d}')
def step_impl(context, statusCode):
    assert context.response.status_code == statusCode


@given('the Weather API (URL), API KEY, {longitude} and {latitude}')
def step_impl(context, longitude, latitude):
    context.url = getConfig()['API']['endpoint'] + ApiResources.getWeatherData
    context.lonLat = payload.callByLongitudeLatitude(lon=longitude, lat=latitude)  # payload


@when('a user queries the URL by the longitude & latitude')
def step_impl(context):
    context.response = requests.get(url=context.url, params=context.lonLat)
    context.json_response = context.response.json()


@then('the {longitude:d} and {latitude:d} in the response body should correspond to the values entered')
def step_impl(context, longitude, latitude):
    assert longitude == context.json_response.get('coord').get('lon')
    assert latitude == context.json_response.get('coord').get('lat')


@given('the Weather API (URL), API KEY, {zipcode}')
def step_impl(context, zipcode):
    context.url = getConfig()['API']['endpoint'] + ApiResources.getWeatherData
    context.zipcode = payload.callByZipcode(zipcode)  # payload


@when('a user queries the URL by the zipcode')
def step_impl(context):
    context.response = requests.get(url=context.url, params=context.zipcode)
    context.json_response = context.response.json()


@then('the (city) {name} in the response body should be associated with the zipcode')
def step_impl(context, name):
    assert context.json_response.get('name') == name
