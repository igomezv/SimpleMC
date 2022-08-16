==================
Requirements
==================


This code runs both in Python 2x and 3x. However, we highly recommend Python 3x. In the github repository, the requirements.txt file contains the basic libraries to run simplemc, but some functions such as graphics or neural networks may not be available. To get the full requirements use ``requirements_full.txt``. You can manually install these dependencies with pip3 install -r requirements_full.txt. The dependencies are listed below.


  * :ref:`installing_dependencies_in_python`

  * :ref:`using_google_colab`


..  _installing_dependencies_in_python:

Installing dependencies in python
----------------------------------

Imperative libraries are:

.. code-block:: bash
   
   sudo pip install numpy matplotlib scipy numdifftools sklearn mpi4py


To use genetic algorithms in order to maximize the Likelihood function:

.. code-block:: bash
   
   pip install deap


If you want the full options to plot:

.. code-block:: bash
   
   pip install corner getdist


To run MCMC analyzer (Metropolis-Hastings) in parallel you need to have `MPI <https://www.open-mpi.org/>`_  in your computer and then install the Python library:

.. code-block:: bash
   
   pip install mpi4py

this requirement is not necessary if you want to use nested sampling, emcee or optimization algorithms.


.. note:: All in one copy-paste line: 

   .. code-block:: bash
   
      pip install numpy matplotlib scipy corner getdist deap numdifftools sklearn mpi4py


..  _using_google_colab:

Using Google Colab
-------------------

For easy and immediate use, we recommend using Google Colab. Within it, it is necessary to install some libraries and simplemc in the first cells.


.. code-block:: bash
   
   %pip install getdist corner fgivenx deap numdifftools
   !pip install -e git+https://github.com/ja-vazquez/SimpleMC#egg=simplemc
   %cd /content/src/simplemc/

Once installed, you may get an error. So restart the kernel, rerun and that's it, the problem will be solved. Then, you can follow any example of the  `Tutorials section <tutorials.html>`_ .

