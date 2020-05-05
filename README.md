# IBMi-JupyterNotebook

Examples of using Jupyter notebooks with IBMi DB2 to make basic reports and visualizations.


## Introduction
Start a DB2 for i code cell with ```%%db2i```

Example
```sql
%%db2i

select *
from QSYS2.SYSTABLES
limit 10;
```


## Setup
* Install dependencies - ```pip3 install jupyter pandas matplotlib numpy pyodbc```
* Open Jupyter - ```jupyter notebook``` (current directory)
* Hosted locally at - **http://localhost:8888/notebooks**


## Additional Jupyter Commands
* ```%%javascript``` - javascript code cell
* ```%load_ext sql``` - load iPython SQL extension
* ```%quickref``` - quick reference of IPython
* ```%%run <file>``` - run another notebook
* ```%%sql``` - SQL code cell

## References
* Jupyter refresher - https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook
* Jupyter widgets - https://ipywidgets.readthedocs.io/en/latest/
* Interactive dashboards in jupyter - https://blog.dominodatalab.com/interactive-dashboards-in-jupyter/
* SQL + Jupyter
  * https://towardsdatascience.com/heres-how-to-run-sql-in-jupyter-notebooks-f26eb90f3259
  * https://www.mssqltips.com/sqlservertip/6120/data-exploration-with-python-and-sql-server-using-jupyter-notebooks/
* Notebook extensions - https://github.com/ipython-contrib/jupyter_contrib_nbextensions
* ipython-sql - https://github.com/catherinedevlin/ipython-sql
