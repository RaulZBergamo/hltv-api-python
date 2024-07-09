[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
![Build Status](https://github.com/RaulZBergamo/hltv-api-python/actions/workflows/python-app.yml/badge.svg)
![Lint Status](https://github.com/RaulZBergamo/hltv-api-python/actions/workflows/python-linting.yml/badge.svg)

# hltv-api-python

A simple unofficial API to return data from matches, players, news...

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)
- [Acknowledgements](#acknowledgements)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/RaulZBergamo/hltv-api-python.git
   ```
2. Navigate to the project directory:
   ```sh
   cd hltv-api-python
   ```
3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

To start the application, run:

```sh
python app/main.py
```

## Endpoints

### Matches

- **All**
  - Endpoint to retrieve data from all today's matches.
  - Example usage:
    ```sh
    curl -X GET "http://localhost:8080/api/matches/all"
    ```

## Contributing

1. Fork the repository.
2. Create a branch for your feature (`git checkout -b feature/fooBar`).
3. Commit your changes (`git commit -am 'Add some fooBar'`).
4. Push to the branch (`git push origin feature/fooBar`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors

- **Raul Z. Bergamo** - *Initial work* - [RaulZBergamo](https://github.com/RaulZBergamo)

## Acknowledgements

- Thanks to anyone or any project that helped.
