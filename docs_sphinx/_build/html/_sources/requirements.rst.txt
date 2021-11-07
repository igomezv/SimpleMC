==================
Requirements
==================


This code runs both in Python 2x and 3x. However, we highly recommend Python 3x. In the github repository, the requirements.txt file contains the basic libraries to run simplemc, but some functions such as graphics or neural networks may not be available. To get the full requirements use ``requirements_full.txt``. You can manually install these dependencies with pip3 install -r requirements_full.txt. The dependencies are listed below.

Imperative libraries are:

.. code-block:: bash
   
   sudo pip install numpy matplotlib scipy numdifftools sklearn mpi4py


To use genetic algorithms in order to maximize the Likelihood function:

.. code-block:: bash
   
   pip install deap


To use Artificial Neural Networks with nested sampling or to learn likelihood functions, you need to install:

.. code-block:: bash
   
   pip install tensorflow



If you want the full options to plot:

.. code-block:: bash
   
   pip install corner getdist


To run MCMC analyzer (Metropolis-Hastings) in parallel you need to have `MPI <https://www.open-mpi.org/>`_  in your computer and then install the Python library:

.. code-block:: bash
   
   pip install mpi4py

this requirement is not necessary if you want to use nested sampling, emcee or optimization algorithms.


.. note:: All in one copy-paste line: 

   .. code-block:: bash
   
      pip install numpy matplotlib scipy tensorflow corner getdist deap numdifftools sklearn mpi4py



