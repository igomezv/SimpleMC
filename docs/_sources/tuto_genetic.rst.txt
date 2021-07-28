MLE with genetic algorithms
============================

In the `maxlike tutorial <tuto_maxlike.html>`_ it is shown how ``SimpleMC`` uses an optimization algorithm to maximize the Likelihood function. This task can also be accomplished using genetic algorithms: 

  * :ref:`simplegenetic`

  * :ref:`deap`

In both cases, we can run ``SimpleMC`` as in the `example Python script <quickstart.html#python-script>`_ using the ``ini file`` with the genetic algorithm information.


..  _simplegenetic:

Simple Genetic
---------------

An example of ``ini file`` to use the ``SimpleGenetic class`` is as follows:

.. code-block:: bash

	[custom]
	...

	model = LCDM

	datasets = SN+HD
	
	analyzer = genetic
	...

	[genetic]
	
	n_individuals = 10
	n_generations = 500
	;selection_method = {tournament, roulette, rank}
	selection_method = tournament
	;mutation probability
	mut_prob = 0.4
	;distribution = {"uniform", "gaussian", "random"}
	distribution = "uniform"
	;media_distribution : media value for gaussian distributions
	media_distribution = 1.0
	;sd_distribution : Standard deviation for gaussian distributions
	sd_distribution = 1.0
	;min_distribution : Minimum value for uniform distributions
	min_distribution = -1.0
	;max_distribution : Maximum value for uniform distributions
	max_distribution = 1.0
	;stopping_early : It needs a value for "rounds_stopping" and "tolerance_stopping".
	stopping_early = True
	;rounds_stopping : Rounds to consider to stopping early with the tolerance_stopping value.
	rounds_stopping = 100
	;tolerance_stopping : Value to stopping early criteria.
	;This value is the difference between the best fit for the
	;latest rounds_stopping generations.
	tolerance_stopping = 0.01


..  _deap:


DEAP library
--------------

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

*TO DO: add in the ini file the keywords to set the simple genetic algorithm from DEAP library.*

