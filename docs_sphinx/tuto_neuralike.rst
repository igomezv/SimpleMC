Speed-up Bayesian inference with neural networks
===================================================

[Section in process...], [Beta release]


``SimpleMC`` can use Artificial Neural Networks (ANNs) to speed-up a Bayesian inference process. Currently, the two available methods only work with one processor and are under continuous development and improvement. At this moment we are finishing the paper and testing our method, it is available in the branch ``neuralike`` on `github.com/igomezv/simplemc_tests <https://github.com/igomezv/simplemc_tests/tree/neuralike>`_.

In both cases, we can run ``SimpleMC`` as in the `example Python script <quickstart.html#python-script>`_ using the ``ini file`` with the genetic algorithm information.



..  _neuralike:

Neuralike
-----------

``Neuralike`` generate a grid over the parameter space and train an ANN with it and the corresponding likelihood values. Then, if the accuracy of the ANN predictions are consistent, perform Bayesian inference with the ANN instead of the analytical expression of the Likelihood function. 

.. code-block:: bash

	[custom]
	...
	...
	analyzername = nested 
	
	[nested]
	;type for dynesty -> {'single','multi', 'balls', 'cubes'}
	nestedType = multi 

	;it is recommended around nlivepoints=50*ndim, recommended 1024
	nlivepoints = 1000

	;recommended 0.01
	accuracy = 0.01

	;u for flat(uniform) or g for gaussian prior
	priortype = u

	;when using gaussian prior
	sigma = 2


	;if nproc = 0 uses mp.cpu_count()//2 by default, 
	;you can set with another positive integer
	nproc = 4

	;Produce output on the fly
	showfiles = True

	;dynamic option is only for dynesty engine
	;dynamic and neuralNetwork can be False/True
	dynamic = False
	; use genetic algorithm to generate live points
	useGenetic = False
	;use neural network to predict likelihoods (True/False),
	;edit block neuralike to set options
	useNeuralike = False


	[neuralike]
	;neuralike contains options to use a neural network in likelihood evaluations over the parameter space
	epochs = 100
	learning_rate = 0.0001
	batch_size = 8 
	psplit = 0.7
	;hidden_layers_neurons: number of nodes per layer separated by commas
	hidden_layers_neurons = 200, 200, 200
	plot = True
	patience = 50
	# neuralike
	nrand = 1000
	valid_loss = 0.01
	nstart_samples = 2000
	nstart_stop_criterion = 100
	updInt = 500
	ncalls_excess = 1000

