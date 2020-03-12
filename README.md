# IBMi-jupyter

Jupyter notebooks for taking notes on IBMi production support


## Dependencies
* Install via pip - ```pip3 install jupyter ipython-sql urllib pandas matplotlib numpy```


## Installing IBMi SQL Alchemy adapter (for Python3)
* Clone ```git clone https://github.com/IBM/sqlalchemy-ibmi```
* Change instance of 'import urllib' to 'import urllib.parse'
* ```pip3 install -e sqlalchemy-ibmi```


## Commands
* ```jupyter notebook``` (open in directory)


## Jupyter Commands
* ```%quickref``` - quick reference of IPython
* ```%load_ext sql``` - load iPython SQL extension


## References
* Jupyter refresher - https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook
* Interactive dashboards in jupyter - https://blog.dominodatalab.com/interactive-dashboards-in-jupyter/
* SQL + Jupyter
  * https://towardsdatascience.com/heres-how-to-run-sql-in-jupyter-notebooks-f26eb90f3259
  * https://www.mssqltips.com/sqlservertip/6120/data-exploration-with-python-and-sql-server-using-jupyter-notebooks/
* SQL Alchemy + AS/400 - https://stackoverflow.com/questions/35461388/connecting-to-ibm-as400-server-for-database-operations-hangs
