Scripty
============

.. image:: https://badge.fury.io/py/scripty.svg
    :target: https://badge.fury.io/py/scripty
    :alt: PyPI Version

.. image:: https://readthedocs.org/projects/scripty/badge/?version=latest
    :target: https://scripty.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://api.codacy.com/project/badge/Grade/b567417a57594f59bb715fc8a72108bf
    :target: https://www.codacy.com/gh/equinoxfitness/scripty?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=equinoxfitness/scripty&amp;utm_campaign=Badge_Grade
    :alt: Code Quality Grade

.. image:: https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg
    :target: https://github.com/equinoxfitness/datacoco-email_tools/blob/master/CODE_OF_CONDUCT.rst
    :alt: Code of Conduct

Scripty is a simple script runner to execute ELT and load tasks.

Installation
------------

Scripty requires Python 3.6+

::

    python3 -m venv <virtual env name>
    source <virtual env name>/bin/activate
    pip install scripty

Quickstart
----------

Redshift does not have stored procedures so we will use Scripty to execute our ELT and load tasks.

Both script runner and SQLWorkbenchJ will use the same notation for variable expansion: `$[?variable]`.  This string will be replaced at runtime by the appropriate variable:

There are three types of substitution parameters that can be used through script runner.  The first is a set of standard etl params for ease of use:

*  -f, from_date, default 1776-07-24
*  -t,to_date, default 9999-12-31
*  -b, batch_no, default is -1

The second option is for arbitrary variable expansion.  This is passed in the following format because rundeck commands don't like json quotes:

*  -p, example: -p "param1-val1, param2-val2"

The final option is to use the batchy integration

*  -wf, batchy_job, this will substitue parameters from a batchy workflow, this should be a fully qualified batchy job name of the format wf.job, if no job is specified it will assume global

Here is a sample SQL Script.  If run in SQL workbench you will be prompted for values for var1 and var2.

::

    drop table if exists  zzztemp;

    create table zzztemp (
    dt timestamp,
    var varchar,
    from_date timestamp,
    batch_no integer
    );

    insert into zzztemp
    values (getdate(), '$[?var1]', '$[?from_date]', '$[?batch_no]');

    insert into zzztemp
    values (getdate(), '$[?var2]', '$[?from_date]', '$[?batch_no]');

    select * from zzztemp;


In the script runner you would use the following params to substitute that value.  It is assumed these params would be dynamically substituted by the calling script or informatica process:

``python -m scripty.module -s "sample/scripty_test.sql" -p "var1-cat, var2-dog" -f '1980-12-31 07:00' -b '9999'``

Assuming you had workflow config in batchy under wf3, you could also use this script:

``python -m scripty.module -s sample/scripty_test.sql -wf wf3``


Development
-----------

Getting Started
~~~~~~~~~~~~~~~

It is recommended to use the steps below to set up a virtual environment for development:

::

    python3 -m venv <virtual env name>
    source <virtual env name>/bin/activate
    pip install -r requirements.txt

Testing
~~~~~~~

::

    pip install -r requirements-dev.txt

To run the testing suite, simply run the command: ``tox`` or ``python -m unittest discover tests``

Contributing
------------

Contributions to scripty are welcome!

Please reference guidelines to help with setting up your development
environment
`here <https://github.com/equinoxfitness/scripty/blob/master/CONTRIBUTING.rst>`__.