==================
Quickstart
==================

In this section we show a basic four steps to use ``SimpleMC``:

1. Set an :ref:`ini file`.
2. Read the configuration in a :ref:`Python script`.
3. Then :ref:`run in terminal`. 
4. Finally :ref:`analyze outputs`. 


..  _ini file:

ini file
***********


The ``ini file`` has all the necessary options to ``SimpleMC``, the mandatory options are in the ``[custom]`` section, the rest have default values corresponding to specific analyzers and you can modify them accordingly with your needs  (see `Customize inifile <inifile.html>`_ or  `baseConfig <inifile.html#baseconfig-ini>`_.ini file for more information).

The ``[custom]`` section has the following structure:

.. code-block::

        [custom]

        chainsdir = chains
        
        model = LCDM
        
        datasets = BBAO+HD+SN

        analyzer = mcmc


you must choose an existing directory to save the outputs (chains, summary, and .paramnames). The options for model, datasets and analyzer are as follows:

.. note::

	* model: visit `Models section <models.html>`_ to see the options.

	* analyzer options: 
		* mcmc, nested, emcee, MaxLikeAnalyzer, genetic, ga_deap

	* data options (you can combine any of them): visit `Data section <data.html>`_ to see the options.


..  _Python script:

Python script
*************

We can use ``test.py`` with the path of the ``ini file``:

.. code-block:: python
   
   from simplemc.DriverMC import DriverMC
   
   fileConfig = "path/baseConfig.ini"
   D = DriverMC(fileConfig)


..  _run in terminal:

run in terminal
****************

For last, run in the terminal:

.. code-block:: bash
   
   $ python test.py

To run multiple MCMC (Metropolis-Hastings) chains in parallel:

.. code-block:: bash
   
   mpirun -np 4 python test.py

where 4 is the number of chains and the number of processors.  

..  _analyze outputs:

analyze outputs
****************

You can see the outputs in the chains directory and then make plots. See the `plots <plotters.html>`_ section for details. The name of the outputs begins with the name of the model, prefact (pre / phy), datasets and analyzer, for the example of the above ``ini file``: ``LCDM_phy_BBAO+HD+SN_mcmc``.

In addition to the chain file, it is a summary where you can notice the parameter estimation, the execution time and in the case of nested sampling, the Bayesian evidence, useful for the comparison of models. 




