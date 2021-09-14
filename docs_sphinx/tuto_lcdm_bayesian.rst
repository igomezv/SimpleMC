Bayesian inference
======================

To perform Bayesian inference for the :math:`\Lambda CDM` model using Type Ia Supernovae and cosmic chronometers, in the ``ini file`` we must set ``LCDM`` and ``SN+HD``:

.. code-block:: bash

	[custom]
	...

	model = LCDM

	datasets = SN+HD
	
	...


There are three options to make parameter estimation through Bayesian inference in ``SimpleMC``: 


  * :ref:`mcmc`

  * :ref:`emcee`

  * :ref:`nested`
  
  * :ref:`notebook`

Once setting the ini file according to the selected sampler, we can run ``SimpleMC`` as in the `python script example <quickstart.html#python-script>`_.

In both cases, the output is a summary with the parameter estimation and an output file with the Markov Chain (see the `section of outputs for details <quickstart.html#analyze-outputs>`_).


..  _mcmc:

With Metropolis-Hastings algorithm
------------------------------------

The model keyword for using the Metropolis-Hastings algorithm is ``mcmc`` as the analyzer. The basic keys in the ``[mcmc]`` section are the number of samples ``nsamp``, the burn-in steps ``skip`` and the Gelman-Rubin stopping criterion ``GRstop``.

.. code-block:: bash

	[custom]
	...
	...
	analyzer = mcmc
	...
	
	[mcmc]
	nsamp = 10000
	skip    = 100
	GRstop  = 0.01
	...


..  _emcee:

With EMCEE algorithm
------------------------------------

To use the EMCEE algorithm we use ``emcee`` library. The basic keys in the ``[emcee]`` section of the ``ini file`` are the number of walkers of the ensemble ``walkers``, the number of samples for each walker ``[nsamp]`` and the burn-in steps ``burnin``.

The number of walkers must be at least twice the number of free parameters. 

.. code-block:: bash

	[custom]
	...
	...
	analyzer = emcee
	...
	
	[emcee]
	walkers = 10
	nsamp = 200
	burnin = 0
	...


..  _nested:


With nested sampling 
----------------------

To perform nested sampling we use the ``dynesty`` library. In this case, in the ``ini file`` the most important keys in the ``[nested]`` section are the number of live points ``nlivepoints`` and the difference between the Bayesian evidence of two consecutive steps (``accuracy``).

.. code-block:: bash

	[custom]
	...
	...
	analyzer = nested
	...

	[nested]
	nlivepoints = 100
	accuracy = 0.02
	...


..  _notebook:

Notebook example
-----------------

In the following notebook there is an example of Bayesian inference to the LCDM model, using SNIa and cosmic chronometers, with the three samplers available in ``SimpleMC``.

.. raw:: html
   :file: notebook_samplers.html
