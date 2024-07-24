# Kanye Quote Twitter Bot

This Python script automates the process of fetching a random Kanye West quote and posting it on Twitter. It uses the Kanye REST API to get quotes and Selenium WebDriver to automate the Twitter posting process.

## Features

- Fetches random Kanye West quotes from the Kanye REST API
- Automates the Twitter login process
- Posts the Kanye quote as a tweet

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed
- Chrome browser installed
- ChromeDriver installed and in your system PATH

## Installation

1. Clone this repository: `https://github.com/F-odt/Custom-Twitter-Automation`
2. Install the required Python packages: `pip install selenium requests`

## Configuration

Before running the script, you need to configure your Twitter credentials:

1. Open the `kanye_quote_twitter_bot.py` file in a text editor.
2. Replace the following placeholders with your actual Twitter credentials:
- `"YOUR EMAIL"`: Your Twitter account email
- `"TWITTER PASSWORD"`: Your Twitter account password
- `"USERNAME"`: Your Twitter username
### NB: 
For this project a separate file was created called credentials, which contains email, username, and password which
was imported and into the main file to fill the login details. You could use
environment variables or config files.



## Usage

To run the Kanye Quote Twitter Bot: `python main.py`

The script will:
1. Fetch a random Kanye West quote
2. Print the quote to the console
3. Log in to your Twitter account
4. Post the quote as a tweet

## Caution

Please note that automated posting on X(Twitter) may violate their terms of service. Make sure you're complying with X(Twitter's) rules and regulations when using this script.

## Contributing

Contributions to the Kanye Quote Twitter Bot are welcome. Please feel free to submit a Pull Request.


## Acknowledgments

- [Kanye REST API](https://kanye.rest/) for providing the Kanye West quotes
- Selenium WebDriver for enabling web automation
