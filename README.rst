------------------------
Development Installation
------------------------

To install ckanext-disable_related for development, activate your CKAN virtualenv and
do::

    git clone https://git.links.com.au/smotornyuk/ckanext-disable_related.git
    cd ckanext-disable_related
    python setup.py develop

-----------------
Running the Tests
-----------------

To run the tests, do::

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have
coverage installed in your virtualenv (``pip install coverage``) then run::

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.disable_related --cover-inclusive --cover-erase --cover-tests

