# SSENSE-Price-Tracker
Price tracker for the eCommerce website [SSENSE](https://www.ssense.com/en-kr).

## Motivation
This project was created to practice web scrapping using python and the web scrapping module beautifulsoup4. Tkinter was used to further practice using GUI libraries.

## Installation
There are certain packages you need to install before running this project.

1. Beautifulsoup4 (this package is used for web scrapping)
```python
pip install beautifulsoup4 
```
Documentation can be found [here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

2. lxml (html5 parser)
```python
pip install lxml
```
There are many different HTML5 parsers you can use, lxml is just one of those. This package will be used to parse the HTML5
markup collected from the web using beautifulsoup4. Documentation can be found [here](https://lxml.de/3.1/index.html)

3. requests
```python
pip install requests
```
Used to send HTML5 requests. Documentation can be found here [here](https://requests.readthedocs.io/en/master/)

There are other packages used such as the tkinter package, but these packages come pre-installed with python3.

## Run
To run the program, make sure you are in the directory with both python files and type in this command in your terminal (or cmd if on windows):
```python
python3 main.py
```
