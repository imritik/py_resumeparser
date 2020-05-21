
    A simple resume parser used for extracting information from resumes

Features
========

-  Extract name
-  Extract email
-  Extract mobile numbers
-  Extract skills
-  Extract total experience
-  Extract college name
-  Extract degree
-  Extract designation
-  Extract company names

Installation
============

-  You can install this package using



    pip install pyresparser

-  For NLP operations we use spacy and nltk. Install them using below
   commands:

.. code:: bash

    # spaCy
    python -m spacy download en_core_web_sm

    # nltk
    python -m nltk.downloader words


Supported File Formats
======================

-  PDF and DOCx files are supported on all Operating Systems
-  If you want to extract DOC files you can install
   `textract <https://textract.readthedocs.io/en/stable/installation.html>`__
   for your OS (Linux, MacOS)
-  Note: You just have to install textract (and nothing else) and doc
   files will get parsed easily

Usage
=====

-  Import it in your Python project

.. code:: python

    from pyresparser import ResumeParser
    data = ResumeParser('/path/to/resume/file').get_extracted_data()

