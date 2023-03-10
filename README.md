# Scraped data from Le Service public fédéral Intérieur

![Open Issues](https://img.shields.io/github/issues-raw/joseparreiras/resultatselection)
![Last Commit](https://img.shields.io/github/last-commit/joseparreiras/resultatselection)
![Language](https://img.shields.io/github/languages/top/joseparreiras/resultatselection)
![Git Forks](https://img.shields.io/github/forks/joseparreiras/resultatselection?label=Fork)
## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Running](#usage)
- [Citation](#citation)

## 📌 About <a name = "about"></a>

This program downloads the election data available on the [Service public fédéral Intérieur](https://resultatselection.belgium.be/fr/information). This data contains the votes for each party in many Belgium elections since the 18s century at the municipality level. For more information go to their [ℹ️ Info Page](https://resultatselection.belgium.be/fr/information).

### 💾 Data

Data is stored in the [data/](/data/) directory in the following pattern `data/election_type/election_date/district_type.csv`. The data is stored in a CSV file with the following columns:


Header | Type | Description
---------|----------|---------
 *Parti* | str | Name of the party
 *Nombre de sièges* | int | Number of seats won by the party
 *Nombre de voix* | int | Number of votes won by the party
 type of district (e.g. "canton")| str | The district of the data
 *date* | int | The year of the election
 *election* | str | The election type
## 🚦 Getting Started <a name = "getting_started"></a>

This code uses Selenium webdriver to download the data. You can find the installation instructions [here](https://selenium-python.readthedocs.io/installation.html). The required packages are listed in the requirements.txt file and you can install them from pip using the following command:

```
    pip install -r requirements.txt
```

### 🦎 Geckodriver
Geckodriver is used to control the Firefox browser. You can download it from [here](https://github.com/mozilla/geckodriver/releases) or using homebrew on macOS:

```
    brew install geckodriver          
```

End with an example of getting some data out of the system or using it for a little demo.

### 📦 Package
The file [resultat.py](/resultat.py) contains the functions that are used to download the data. The main function is `download_election` and you can find the documentation for it in the file. The second function `get_download_url` is used to get the download link for a specific election queue. It can be imported with:

```python
    from resultat import *
```

## 🏃🏻‍♂️ Running <a name = "usage"></a>

There are two programs to download the data. The first one is on [get_results.py](/get_results.py) and downloads the data for a specific election queue. It should be better for people interested in donwnloading a single file. For this program I recommend running on terminal as it uses `inquirer` package which I have found some issues within Jupyter interactive terminals. You can do it with:
```
    python get_results.py
```
After this, you will be asked to select the election type, date and district type you want to download.

The second program is on [get_all.py](/get_all.py) and downloads all the data available on the website. This takes longer than the previous one since it scrapes the entire website for data. It can be run in a similar way:
```
    python get_all_results.py
```
or you can use it on an interactive terminal.

## ☕️ Citation <a name = "citation"></a>
If this code is useful for your research, please consider citing it as:

```bibtex

@software{resultatselection,
  author = {Antunes-Neto, Jose},
  title = {{Scraped data from Le Service public fédéral Intérieur}},
  url = {https://github.com/github/joseparreiras/resultatselection},
  version = {1.0.0},
  date = {2023-02-02}
}
```

or refer to GitHub's *"Cite this repository"* button.