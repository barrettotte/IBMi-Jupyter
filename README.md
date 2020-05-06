# IBMi-Jupyter

Utility notebook for using Jupyter notebooks with IBMi basic reports and visualizations.


## Example

[Cell 1]
```python
# Loads IBMi notebook
%%run IBMi.ipynb
```

[Cell 2]
```sql
-- Do a simple DB2 query
%%ibmi

select *
from QSYS2.SYSTABLES
limit 10;
```


See more in [tests/Test.ipynb](tests/Test.ipynb)


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
