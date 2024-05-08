# Harvest Harmony

Harvest Harmony is a crop recommendation system designed to assist farmers in selecting the most suitable crops based on their soil data. This application utilizes machine learning techniques to analyze various soil parameters and provide recommendations for crops that are likely to thrive in the given conditions.

## Features

- **Soil Data Input**: Farmers can easily input their soil data, which includes nitrogen, phosphorus, potassium, temperature, humidity, pH, and rainfall, through a user-friendly form.
- **Crop Recommendation**: Based on the provided soil data, Harvest Harmony utilizes a machine learning model to recommend a list of crops that are most likely to thrive in the given conditions.

## Getting Started

To get started with Harvest Harmony, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/pkshetty15/harvest-harmony.git
   ```

2. Change working directory:

   ```bash
   cd harvest-harmony
   ```

3. [Setup Virtual Environment](https://pkshetty.hashnode.dev/setting-up-virtual-environments-in-python#heading-creating-a-virtual-environment):\*

   ```bash
   python -m venv .venv
   ```

4. [Activate the virtual environment](https://pkshetty.hashnode.dev/setting-up-virtual-environments-in-python#heading-activating-the-virtual-environment):\*

   - On Windows:

     ```bash
     .venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source .venv/bin/activate
     ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Configure the application settings in `config.py`
7. Run the application:

   ```bash
   python run.py
   ```

   or

   ```bash
   flask run
   ```

8. Access the application in your web browser at [http://localhost:5000](http://localhost:5000)

> \* Note: Steps 3 and 4 are optional but recommended to isolate the project dependencies from other Python projects on your system. To know more about virtual environments, refer to this [guide](https://pkshetty.hashnode.dev/setting-up-virtual-environments-in-python).

## Prerequisites

- Python 3.6 or higher
- Flask
- scikit-learn (or any other machine learning library used)
- Additional dependencies listed in `requirements.txt`

## Contributing

We welcome contributions from the community to further enhance Harvest Harmony. If you encounter any issues or have suggestions for improvements, please submit them to our [issue tracker](https://github.com/pkshetty15/harvest-harmony/issues).

To contribute to the project, follow these steps:

1. Fork the repository
2. Create a new branch: `git switch -c branch-name` or `git checkout -b branch-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin branch-name`
5. Submit a pull request

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - The web framework used
- [scikit-learn](https://scikit-learn.org/) - Machine learning library (or any other library used)
- [matplotlib](https://matplotlib.org/) - Data visualization library
- [pandas](https://pandas.pydata.org/) - Data manipulation library
