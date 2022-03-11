# Issues

## Multiple pythons

There may be multiple versions of python installed. Check:

    `python --version`

    `python3 --version`

    `which python`

    `which python3`

## Pandas is not recognized.

In my case this is because `pip install package` puts packages to

   ` /usr/local/lib/python3.9/site-packages`

but this path is not in the search path of Python when I run it :|  Instead, my Python looked in:

   `/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages`

What I did is to do:

    `python3 -m pip install package`

This will install the packages in the second path above.

Another solution could be by adding the first path to the env-var PYTHONPATH. See https://stackoverflow.com/questions/15252040/how-does-python-find-a-module-file-if-the-import-statement-only-contains-the-fil   
