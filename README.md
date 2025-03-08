# Stock-Web-Scrapping
Initial Upload: 2/27/2025
Last Updated: 3/8/2025

Data 580D -- Analytics for Enterprise Apps

Project Objective: Write a python script to scrape stock price movement in the US stock market.

Project Tools: Utilizes a basic python script, initially coded through Jupyter Notebook. Additionally, the following libraries are required:
• json
• csv
• sys
• typing
• requests
• BeautifulSoup
• pandas

# Motivation
Scraping finance data from the Web offers valuable insights that come in handy in various scenarios, including:
• Automated Trading: By gathering real-time or historical market data, such as stock prices and volume, developers can build automated trading strategies.
• Technical Analysis: Historical market data and indicators are extremely important for technical analysts. These allow them to identify patterns and trends, assisting their investment decision-making.
• Financial Modeling: Researchers and analysts can gather relevant data like financial statements and economic indicators to build complex models for evaluating company performance, forecasting earnings, and assessing investment opportunities.
• Market Research: Financial data provide a great deal of information about stocks, market indices, and commodities. Analyzing this data helps researchers understand market trends, sentiment, and industry health to make informed investment decisions.

When it comes to monitoring the market, Yahoo Finance is one of the most popular finance websites. It provides a wide range of information and tools to investors and traders, such as real-time and historical data on stocks, bonds, mutual funds, commodities, currencies, and market indices. Plus, it offers news articles, financial statements, analyst estimates, charts, and other valuable resources.

By scraping Yahoo Finance, you can access a wealth of information to support your financial analysis, research,
and decision-making processes.

## Usage
Running the code requires no alterations, as all system/user-specific actions will be initiated upon implementation. The program will ask the user for their user-agent, which you can find by entering "my user agent" into your search engine.

The program will then ask for a series of stock tickets, which can be provided in one string, separated by spaces.

After being provided with your user-agent and the string of stock tickets, the program will individually pull the current stock information from each company, including a variety of informtion. Following program completion, it will print ("Done!" and export the stock information to a JSON, CSV, and an SLXS (excel) file.

# Example
## Deriving User Agent
User-agent obtained through entering "my the user agent" into the search engine (in this example, google chrome)

![image](https://github.com/user-attachments/assets/05a0e203-c3b3-42da-aa62-d2ee7794dcd9)

## Python
Upon running the code, it will ask for the user agent, which you can respond by typing into the box and pressing enter

![image](https://github.com/user-attachments/assets/0042ade8-eab8-4560-8499-274a55f27e78)

Then it will request a series of stock tickers, separated by a space. In the below example, Tesla (TSLA), Amazon (AMZN), Apple (AAPL), META (META), Netflix (NFLX), and Google (GOOG) are provided.

![image](https://github.com/user-attachments/assets/2be156c9-cd12-4a9a-a125-4c9cee4f8601)

## Output
The program will provided real-time updates about the derivation of each companies stocks, then informing you of the program's completion through printing "Done!" as seen below.

![image](https://github.com/user-attachments/assets/39afcc64-2900-4445-9634-c640503ac2ac)

Items will be output in csv, xlsx, and JSON format in the folder the python code is run in.

![image](https://github.com/user-attachments/assets/98831219-bf8a-4b16-998a-31b866abf74c)

# Attributions
Template for README.md derived from David Freitag (https://github.com/dkfreitag/chicago_crime_project)

Additional assistance provided by Dr. Sumantra Sarkar and GA Vidyascagar Reddy
