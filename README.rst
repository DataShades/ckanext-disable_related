=====================
Disable Related Items
=====================

An extensions for CKAN that disables the Related Items feature.

* Returns HTTP 404s for related items URLs
* Returns authorisation denied responses for API methods
* Removes Related Items tab from Dataset page

------------
Requirements
------------

Developed and tested with CKAN 2.3.1.

------------------------
Development Installation
------------------------

To install ckanext-disable_related for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/DataShades/ckanext-disable_related.git
    cd ckanext-disable_related
    python setup.py develop

Add ``disable_related`` to the ``ckan.plugins`` setting in your CKAN config file.

-----------------
Running the Tests
-----------------

To run the tests, do::

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have
coverage installed in your virtualenv (``pip install coverage``) then run::

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.disable_related --cover-inclusive --cover-erase --cover-tests

-------------------
Copying and License
-------------------

This material is copyright © 2015 Link Web Services Pty Ltd

It is open and licensed under the GNU Affero General Public License (AGPL) v3.0 whose full text may be found at:

http://www.fsf.org/licensing/licenses/agpl-3.0.html
