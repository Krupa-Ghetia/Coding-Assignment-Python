<h3>Assignment 1</h3>

Write a python program to scrape the list of links available in this Github repository (https://github.com/vinta/awesome-python) and search them by exact name from the console. Search result should return the github url of the result repository. 

Expected output:
```
$ python search_repos.py
> Query? graphene 
> Output: https://github.com/graphql-python/graphene/
```
The list should be scraped and kept in a runtime variable as soon as the program is initialized.. Handle the error with a suitable error message in case the exact name is not matched from the list.


<h3>System Requirements</h3>

* python v3.8 or greater
* geckodriver v0.29.0 or greater
  
  (You can download geckodriver from [here](https://github.com/mozilla/geckodriver/releases). Unzip the file and add it to your system path)


<h3>Execution</h3>

To run, in the terminal run ```python3.8 search_repos.py```

You will be prompted to enter the name of the repository you want to search

**Input**
```buildoutcfg
$ python3.8 search_repos.py
> Query? Caching
```
**Output:**
```buildoutcfg
> Output: https://github.com/vinta/awesome-python#caching
```




