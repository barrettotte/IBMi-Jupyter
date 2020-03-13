from distutils.core import setup

setup(
    name='ipython-db2i',
    version=0.1,
    packages=['ipython-db2i'],
    url='https://github.com/barrettotte.com/IBMi-JupyterNotebook',
    license='MIT',
    author='Barrett Otte',
    author_email='barrettotte@gmail.com',
    description='IPython extension for IBMi DB2',
    install_requires=["pyodbc", "pandas"]
)
