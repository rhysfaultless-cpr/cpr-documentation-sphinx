# CPR documentation

[Access the site here](https://rhysfaultless-cpr.github.io/cpr-documentation/)

This documentation can be build as either webpages or latex/PDF, but is optimized for webpages

## Setup

1.  [Install Sphinx](https://www.sphinx-doc.org/en/master/usage/installation.html#windows-other-method) on your computer. 

2.  Check if you have Node.js installed on your computer, by opening a terminal and running:

        node -v

    [Install _Node.js_](https://nodejs.org/en/download/package-manager/) if it is not on your computer.

3.  Add _Live Server_ as an extension in _VS Code_.


4.  Clone this repository. This repository has two Git Submodules, so the easiest way to grab those files is to clone this using the recursive flag:

        git clone --recurse-submodules https://github.com/rhysfaultless-cpr/cpr-documentation.git

    Alternatively, you can clone the repository, and then add the Git Submodules:

        git clone https://github.com/rhysfaultless-cpr/cpr-documentation.git
        git submodule init
        git submodule update

5.  To build the HTML webpages:

    1.  Open a new terminal in _VS Code_
    2.  Navigate to the root of the project directory on your computer
    3.  Run the command:

            sphinx-build -b html source html

6.  To view the HTML webpages:

    1.  In _VS Code's_ file explorer, navigate to _cpr-documentation/html/index.html_. 
    2.  Right click on _index.html_ and select _Open with Live Server_.
        This should open a web browser with the latest files stored on your computer in _cpr-documentation/build/html_.
    3.  You can stop running the server by clicking the _Port: 5500_ button in the bottom right of _VS Code_.

7.  To build PDF files using LaTex:
    1.  Open a new teminal
    2.  Navigate to the project root directory, and run:
    
            sphinx-build -b latex doc build-latex
            cd build-latex
            make
        
    3.  If you get errors about missing fonts, go to latex/clearpath-latex/fonts and install all the fonts there.