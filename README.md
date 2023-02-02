# Scraped data from Le Service public fédéral Intérieur

![Open Issues](https://img.shields.io/github/issues-raw/joseparreiras/resultatselection)
![Last Commit](https://img.shields.io/github/last-commit/joseparreiras/resultatselection)
![Language](https://img.shields.io/github/languages/top/joseparreiras/resultatselection)
![Git Forks](https://img.shields.io/github/forks/joseparreiras/resultatselection?label=Fork)
## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Running](#usage)

## 📌 About <a name = "about"></a>

This program downloads the election data available on the [Service public fédéral Intérieur](https://resultatselection.belgium.be/fr/information). Fore more information go to their [ℹ️ Info Page](https://resultatselection.belgium.be/fr/information)

## 🚦 Getting Started <a name = "getting_started"></a>

This code uses Selenium webdriver to download the data. You can find the installation instructions [here](https://selenium-python.readthedocs.io/installation.html). The required packages are listed in the requirements.txt file and you can install them from pip using the following command:

```
    pip install -r requirements.txt     # install the required packages
```

### 🦎 Geckodriver
Geckodriver is used to control the Firefox browser. You can download it from [here](https://github.com/mozilla/geckodriver/releases) or using homebrew on macOS:

```
    brew install geckodriver            # install geckodriver
```

End with an example of getting some data out of the system or using it for a little demo.

### 📦 Package
The file [resultat.py](/resultat.py) contains the functions that are used to download the data. The main function is `download_election` and you can find the documentation for it in the file. The second function `get_download_url` is used to get the download link for a specific election queue.

## 🏃🏻‍♂️ Running <a name = "usage"></a>

There are two programs to download the data. The first one is on [get_results](/get_results.py) and downloads the data for a specific election queue. It should be better for people interested in donwnloading a single file. For this program I recommend running on terminal as it uses `inquirer` package which I have found some issues within Jupyter interactive terminals. You can do it with:
```
    python get_results.py               # run the program
```
After this, you will be asked to select the election type, date and description you want to download.

The second program is on [get_all_results](/get_all_results.py) and downloads all the data available on the website. This takes longer than the previous one since it scrapes the entire website for data. It can be run in a similar way:
```
    python get_all_results.py           # run the program
```
or you can use it on an interactive terminal.