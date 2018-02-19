A Text Analysis Using Project Gutenberg
=======================================

![alt text](https://prisonbookscollective.files.wordpress.com/2013/09/pile-of-books.jpg)


=======================================


#### Installation (OSX)
1. Install the homebrew package manager

  ```bash
  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  ```

2. Install Java from: https://java.com/en/download/

3. Brew install python3, spark, and scala
```bash
brew install python3 apache-spark scala
```

4. Set Environment variables for spark/java in your bash_profile. Java can be installed in many places...
Examples:
```bash
if which java > /dev/null; then export JAVA_HOME=$(/usr/libexec/java_home); fi

# setup spark for jupyter for prototyping
PYSPARK_DRIVER_PYTHON=jupyter
PYSPARK_DRIVER_PYTHON_OPTS='notebook'
```

4. Setup a Virtual environment

5. pip install requirements.txt

6. Protype anything locally and when ready, run on spark cluster!!