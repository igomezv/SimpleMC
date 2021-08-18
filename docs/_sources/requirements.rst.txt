==================
Requirements
==================


This code runs both in Python 2x and 3x. However, we highly recommend Python 3x. 

Imperative libraries are:

.. code-block:: bash
   
   sudo pip install numpy matplotlib scipy 


To use genetic algorithms in order to maximize the Likelihood function:

.. code-block:: bash
   
   pip install deap


To use Artificial Neural Networks with nested sampling or to learn likelihood functions, you need to install:

.. code-block:: bash
   
   pip install tensorflow



If you want the full options to plot:

.. code-block:: bash
   
   pip install corner getdist


.. note:: All in one copy-paste line: 

   .. code-block:: bash
   
      pip install numpy matplotlib scipy tensorflow corner getdist deap 

To run MCMC analyzer (Metropolis-Hastings) in parallel you need to have `MPI <https://www.open-mpi.org/>`_  in your computer and then install the Python library:

.. code-block:: bash
   
   pip install mpi4py

this requirement is not necessary if you want to use nested sampling, emcee or optimization algorithms.





