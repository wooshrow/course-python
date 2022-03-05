# A Course Python

This is a course to learn the Python programming language.

### Hardware and software requirement

You need to bring your own laptop with either of this OS: Windows (at least Windows 10), or MacOS, or Linux.

Install the following on your laptop:

1. Download this course-repository to your laptop. For example you [can download its zip](https://github.com/wooshrow/course-python/archive/refs/heads/main.zip).

1. Install [Python 3.x](https://www.python.org/), at least version 3.7. The latest now is 3.10.

    To check if you have the right version, open a Command Line shell, and do:

    `python3 --version`

    Check if you also get `pip3`, which is Python's official package manager; you need this for installing packages which are not in the standard Python distributions (for example data-science related packages). To check if you have pip3, do this in your Command Line shell:

    `pip3 --version`

1. Install [Visual Studio Code (VSC)](https://code.visualstudio.com/); we will use this later as a text editor to write programs.

    From VSC, install the Python extensions. This shoukd also intsall Jupyter extension. If Jupyter extension is installed, you can just do `Open Folder` from VSC to open the directory `Lecturenotes`. After this you can browse the lecture notes from VSC.

1. Install Jupyter. This gives you an easy to use working environment to do our exercises at the beginning.

    After you installed Python 3.x (above), you can install `Jupyter Notebook` from Python 3.x. Open a Command Line shell. From there do these:

      `pip3 install --upgrade pip`

      `pip3 install jupyter`

    After installing Jupyter, to try that it works, from the Command Line shell, go to the directory where you unziped this course, and do:

      `jupyter notebook`

    This should open Jupyter in your web-browser. From there, browse the course materials, load one of the `*.ipynb` file in the folder `Lecturenotes`.  

    You can use either this web-browser-based Jupyter, or VSC Jupyter. 

### [Course Plan, click here](./courseplan.md)

### Other stuffs

* Lecture notes and exercises (previously in PDF format, now as interactive Jupyter notebooks)
* Project assignments (for four two-week projects, done in groups of 3-4 students)

### License
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

### Acknowledgement

This course is based on the materials from the course _Computational Thinking, Programming with Python and Programming with Data at Utrecht University (CoTaPP)_, developed by [Anna-Lena Lamprecht](https://github.com/annalenalamprecht) and [Amy van der Ham](https://github.com/amyvdham). Thank you!
