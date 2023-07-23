# Company Review Web App

<p align="center">
  <!-- Insert a relevant image here to represent the project visually -->
</p>

This is a Python-based web application that allows users to search for a company and retrieve reviews from Trustpilot. The application also performs sentiment analysis on the reviews and extracts keywords to provide valuable insights into the company's reputation. I developed this project to practice web scraping, sentiment analysis, and using machine learning models to extract relevant information from textual data.

## Technologies Used

![Python](https://img.shields.io/badge/Python-100%25-blue?style=flat-square&logo=python&logoColor=white)
![Beautiful Soup](https://img.shields.io/badge/Beautiful%20Soup-Web%20Scraping-yellow?style=flat-square&logo=beautifulsoup&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI%20Framework-orange?style=flat-square&logo=tkinter&logoColor=white)
![KeyBERT](https://img.shields.io/badge/KeyBERT-Keyword%20Extraction-blueviolet?style=flat-square&logo=python&logoColor=white)
![VADER Sentiment](https://img.shields.io/badge/VADER%20Sentiment-Sentiment%20Analysis-blue?style=flat-square&logo=nltk&logoColor=white)

# Features
- Search for a company on Trustpilot and retrieve reviews
- Perform sentiment analysis on the reviews to determine their overall sentiment (positive, negative, or neutral)
- Extract the top keywords from the reviews using KeyBERT
- Display the reviews, sentiment analysis result, and extracted keywords on a user-friendly GUI

# Installation
1. Clone the repository:
```
git clone https://github.com/your-username/company-review-web-app.git
```
2. Install the required dependencies:
```
pip install beautifulsoup4 requests tkinter keybert vaderSentiment
```

# Usage
1. Run the application by executing the following command in your terminal or command prompt:
```
python your_project_file.py
```

2. The application window will open, providing an interface to interact with the app.

3. Enter the name of the company you want to search for in the "Company Name" entry field.

4. Click the "Search" button to retrieve the list of websites associated with the searched company from Trustpilot.

5. Choose a website from the list and click the "Get Data" button to scrape reviews, perform sentiment analysis, and extract keywords.

6. The application will display the scraped reviews on the left side, the sentiment analysis result on the top right, and the extracted keywords on the bottom right.

# Customization
If you want to modify the GUI's appearance or layout, you can make changes to the Tkinter code in your_project_file.py. You can also adjust the number of top keywords to be extracted by modifying the "top_n" parameter in the model.extract_keywords() function call.

# Contributing
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.

# License
This project is licensed under the MIT License.
