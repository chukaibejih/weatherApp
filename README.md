# weatherApp

## About

* This is a weather application that was built using django framework, django rest frame work and a weather api from http://api.openweathermap.org. This application receives an input (City name) and returns:
    * City and Country 
    * Current temperature
    * Feels like
    * Max and Min temprature
    * Weather description
* Project status: prototype


## Table of contents

> * [Title / weatherApp](#title--repository-name)
>   * [About](#about--synopsis)
>   * [Table of contents](#table-of-contents)
>   * [Installation](#installation)
>   * [Screenshots](#screenshots)
>   * [Requirements](#requirements)
>   * [Limitations](#limitations)
>   * [Deployment](#deploy-how-to-install-build-product)
>   * [Contributing / Reporting issues](#contributing--reporting-issues)
>   * [License](#license)


## Installation

1. Create a new virtual environment.

  ```bash
  python -m venv (virtual environment name)
  ```
  
2. Activate the virtual environment

  ```bash
  source (virtual environment name)/scripts/activate
  ```
  
3. Install dependencies by running the following command in your terminal:

  ```bash
  pip install -r requirements.txt
  ```
  
4. Visit https://openweathermap.org/api to choose a data collection and follow further instructions


### Screenshots

* First screenshot shows the initial launch of the application which displays the weather of the current location. 
  ![Screenshot (93)](https://user-images.githubusercontent.com/29266211/164565179-5c76086e-94b8-4204-8fd0-f0ff30adf44d.png)

* Second screenshot shows the searched city's weather (London)
  ![Screenshot (94)](https://user-images.githubusercontent.com/29266211/164565445-c24f256e-5247-4331-9b18-e8cb01555777.png)


### Requirements

* Install dependencies by running the following command in your terminal:

  ```bash
  pip install -r requirements.txt
  ```

### Limitations

* This application lacks a proper user interface
* All temprtures in this application is in °F. A temptrature converter is missing.


### Deploy (how to install build product)

* This Application has not been deployed. 

## Contributing / Reporting issues

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
