# A Course on Python

This is a course to learn the Python programming language.

### Hardware and software requirement

You need to bring your own laptop with either Windows (at least Windows 10), or MacOS, or Linux.

To prepapre for the course, install the following on your laptop:

1. Download this course-repository to your laptop. For example you [can download its zip here](https://github.com/wooshrow/course-python/archive/refs/heads/main.zip).

1. Install **Python 3.x** from https://www.python.org/ , at least version 3.9. The latest now is 3.10.

    To check if you have the right version, open a **Command Line Interface (CLI)** (also called 'Command Prompt' in Windows). In Mac a CLI looks like this:

    ![Command Line Interface (CLI) in Mac](./Lecturenotes/img/CLI.png) 
    
    
    In the CLI, type one of these commands:

    `python3 --version`

    `python --version`

    Check if you also get `pip3`, which is Python's official package manager; you need this for installing packages which are not in the standard Python distributions (for example data-science related packages). To check if you have pip3, do this in your CLI:

    `pip3 --version`

1. Install the package `pandas` for Python. From CLI do one of these:

     `pip3 install pandas`

     `python3 -m pip install pandas`

1. Test your Python installation. At CLI, go to root directory of this course materials. Then run the program `testme.py` from the CLI:

     `python3 testme.py`

    The program should not crash.     


1. Install **Visual Studio Code (VSC)** from https://code.visualstudio.com/ ; we will use this later as a text editor to write programs.

    From VSC, install the _Python Extensions_. This shoukd also intsall Jupyter extension. If Jupyter extension is installed, you can just do `Open Folder` from VSC to open the directory `Lecturenotes` of this course. After this you can browse the lecture notes from VSC.

1. Install Jupyter. This gives you an easy to use working environment to do our exercises at the beginning.

    After you installed Python 3.x (above), you can install `Jupyter Notebook` from Python 3.x. From CLI, do these:

      `pip3 install --upgrade pip`

      `pip3 install jupyter`

    After installing Jupyter, to try that it works, from CLI, go to the directory where you unziped this course, and do:

      `jupyter notebook`

    This should open Jupyter in your web-browser. From there, browse the course materials, load one of the `*.ipynb` files in the folder `Lecturenotes`.  

    You can use either this web-browser-based Jupyter. Alternatively, use VSC to open and browse the folder `Lecturenotes`. From there just open one of the `*.ipynb` files in the folder, this will open the file in the Jupyter-mode in VSC. 

### [Course Plan, click here](./courseplan.md)

### Other stuffs

* Lecture notes and exercises (previously in PDF format, now as interactive Jupyter notebooks)
* Project assignments (for four two-week projects, done in groups of 3-4 students)

### License
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

### Acknowledgement

This course is based on the materials from the course _Computational Thinking, Programming with Python and Programming with Data at Utrecht University (CoTaPP)_, developed by [Anna-Lena Lamprecht](https://github.com/annalenalamprecht) and [Amy van der Ham](https://github.com/amyvdham). Thank you!
