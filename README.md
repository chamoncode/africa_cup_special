# African Cup of Nations 2024 Results Scraper

This project is a Python script that scrapes the results of the African Cup of Nations 2024 from the Eurosprt website.

![Screenshot 2024-01-23 at 18 54 40](https://github.com/chamoncode/africa_cup_special/assets/84735736/27182468-1d15-4e76-88f9-f2ec8137ecb0)

It is automatically refreshed (uses polling).

```mermaid
graph LR
P(Polling2+requests) --> A[Website]
P --> B(BeautifulSoup)
B --> C{Data Extraction}
C --> E{Data Processing}
E --> F[Streamlit]
F --> G[Dynamic Webapp]
```

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python installed on your machine. You can download Python [here](https://www.python.org/downloads/).
Tested with Python 3.12

### Installing

1. Clone the repository:
    ```sh
    git clone <repository_url>
    ```
2. Navigate to the project directory:
    ```sh
    cd <project_directory>
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Script

To run the app, use the following command:

```sh
streamlit run app.py
