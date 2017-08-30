
Getting Started
===============

Installation
------------

Automatic Installation
~~~~~~~~~~~~~~~~~~~~~~

Clone this repository::

    git clone https://github.com/miclaraia/swap.git

Run the builtin setup script::
    
    ./swap/bin/install

This script will create a virtual environment in the cloned git repository
and install swap inside. It will also copy the default swap config file
to the local location in `swap/conf/swap.conf`. SWAP will look for this config
file in the following locations, and use the first one it finds:

    #. A location specified in the :code:`SWAP_CONFIG` environment variable
    #. :code:`~/.swaprc`
    #. :code:`/etc/swap/swap.conf`
    #. :code:`swap/conf/swap.conf` in the local SWAP installation directory

SWAP depends on an external MongoDB database. Make sure you have this installed
on the system. Find it in your distribution's repositories, or build it from
source. Find more information `here <https://www.mongodb.com/>`_

Manual Installation
~~~~~~~~~~~~~~~~~~~

It is recommended to set up a virtual environment and install SWAP
and its dependencies inside. Find more information about virtual environments
`here <http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/>`_,
and information about conda `conda <https://conda.io/docs/using/>`_.

First, clone the repository::

    git clone https://github.com/miclaraia/swap.git

Create a virtual environment::

    mkvirtualenv swap --python=/usr/bin/python3 swap

Install SWAP::

    pip install -e swap

*Extras:* 
SWAP has some additional functionalities that can be installed via pip. To
install these extras, run::

    pip install -e swap[{EXTRA1},{EXTRA2},...]

+---------------+--------------------------------------------------+
| dev           | Install additional dependencies required for     |
|               | development                                      |
+---------------+--------------------------------------------------+
| plot          | Install plotting libraries and activate SWAP's   |
|               | builtin plotting functionality.                  |
+---------------+--------------------------------------------------+


There are a number of additional dependencies that can be installed to enhance
SWAP. 
Run `pip install -e swap[dev]` to install dependencies require
Pip can also install SWAP in development mode. This means pip will install
the project in editable mode, so changes to the source affect the runtime version.
It will also install additional dependencies for testing and development.
To do this, clone the git repository, navigate to the projectd directory, and run::

    pip install -e hco-experiments/swap[dev,test]

.. include:: config.rst

