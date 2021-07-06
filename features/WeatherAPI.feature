# Created by muhammed at 7/6/21
Feature: Verify the Weather API GET Request Response corresponds to the query variables

  # please note a more robust test data set can be generated using Chance Library in JS, stored in CSV and imported into the following test cases

  @smoke @regression @weather   # multiple tags can be used in order to group test cases and run specific groups
  Scenario Outline:
    Given the Weather API (URL), API KEY and <city>
    When a user queries the URL by the city name
    Then the name attribute in the response body should correspond to the entered <city>
    And the status code should be 200
    Examples:
      | city |
      |London|
      |Moscow|
      |New York|

  @smoke @sprint2.6 @weather
  Scenario Outline:
    Given the Weather API (URL), API KEY, <longitude> and <latitude>
    When a user queries the URL by the longitude & latitude
    Then the <longitude> and <latitude> in the response body should correspond to the values entered
    And the status code should be 200
    Examples:
      | longitude | latitude |
      |   37      |   55     |
      |   55      |    55    |
      |   39      |    39    |

  @smoke @weather
  Scenario Outline:
    Given the Weather API (URL), API KEY, <zipcode>
    When a user queries the URL by the zipcode
    Then the (city) <name> in the response body should be associated with the zipcode
    And the status code should be 200
    Examples:
      | zipcode |     name      |
      | 10009   | New York      |
      | 11385   | Ridgewood     |
      | 35010   | Alexander City |







