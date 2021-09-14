MLE with genetic algorithms
============================

In the `maxlike tutorial <tuto_maxlike.html>`_ it is shown how ``SimpleMC`` uses an optimization algorithm to maximize the Likelihood function. This task can also be accomplished using genetic algorithms from DEAP library.


We can run ``SimpleMC`` as in the `example Python script <quickstart.html#python-script>`_ using the ``ini file`` with the genetic algorithm information.


An example of ``ini file`` to use the simple genetic algorithm from ``DEAP library`` is as follows:

.. code-block:: bash

	[custom]
	...

	model = LCDM

	datasets = SN+HD
	
	analyzer = ga_deap
	...

	[ga_deap]
	;Plot Generation vs Fitness
	plot_fitness = True

	;compute errror from Hessian matrix
	;False/True
	compute_errors = False

	;If withErrors is True
	;plot Fisher matrix
	show_contours = False

	;If showplot is True, then
	;2D plot for the parameters:
	plot_par1 = h
	plot_par2 = Om


..  _notebook:

Notebook example
-----------------

In the following notebook there is an example of the use of ``ga_deap`` and ``maxlike``.

.. raw:: html
   :file: notebook_optimizers.html

