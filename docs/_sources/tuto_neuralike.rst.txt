Speed-up Bayesian inference with neural networks
===================================================

[Section in process...], [Beta release]

``SimpleMC`` can use Artificial Neural Networks (ANNs) to speed-up a Bayesian inference process. Currently, the two available methods only work with one processor and are under continuous development and improvement. 

  * :ref:`pybambi`

  * :ref:`neuralike`

In both cases, we can run ``SimpleMC`` as in the `example Python script <quickstart.html#python-script>`_ using the ``ini file`` with the genetic algorithm information.


..  _pybambi:

Modified pybambi
-----------------

``SimpleMC`` contains a modified version of ``pybambi`` that only works with nested sampling. It trains a real-time ANN and, if the accuracy of the predictions is good, the sampling process uses the ANN instead of the analytical expression of the Likelihood function. 

.. code-block:: bash

	[custom]
	...
	...
	analyzername = nested
	...

	useNeuralLike = False


	[nested]
	nlivepoints = 350
	accuracy = 0.02
	...
	neuralNetwork = True

	[neural]
	;modified bambi
	split = 0.8
	; keras or nearestneighbour
	learner = keras
	;all the following options are only for keras learner
	; number of neurons of the three hidden layers
	numNeurons = 50
	; epochs for training
	epochs = 100
	; number of training points
	;ntrain = nlivepoints by default
	;dlogz to start to train the neural net (we recommend dlogz_start <=10)
	dlogz_start = 5
	;number of nested (dynesty) iterations to start to train the neural net
	it_to_start_net = 10000
	;number of iterations to re-train the neural net. By default updInt = nlivepoints,
	;choose updInt <= nlivepoints
	;updInt = 500
	;proxy_tolerance uncertainity of the net allowed.
	proxy_tolerance = 0.3



..  _neuralike:

Neuralike
-----------

``Neuralike`` generate a grid over the parameter space and train an ANN with it and the corresponding likelihood values. Then, if the accuracy of the ANN predictions are consistent, perform Bayesian inference with the ANN instead of the analytical expression of the Likelihood function. 

.. code-block:: bash

	[custom]
	...
	...
	analyzername = nested 
	;analyzername can be mcmc
	...

	useNeuralLike = True

	[neuralike]
	;neuralike contains options to use a neural network in likelihood evaluations over the parameter space
	ndivsgrid = 4
	epochs = 500
	learning_rate = 1e-5
	batch_size = 16
	psplit = 0.8
	;hidden_layers_neurons: number of nodes per layer separated by commas
	hidden_layers_neurons = 100, 100, 100
	;number of procesors to make the grid
	nproc = 5

