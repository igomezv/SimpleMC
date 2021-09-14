Maximum Likelihood Estimation (MLE) with optimizer
===================================================

``SimpleMC`` through the ``MaxLikeAnalyzer class`` uses the L-BFGS-B algorithm from ``scipy.optimize.minimize`` and tries to maximize the Likelihood function based on a cosmological model and selected datasets. It then obtains the errors of the Hessian.

An example of ``ini file`` to use the ``MaxLikeAnalyzer class`` is as follows:

.. code-block:: bash

	[custom]
	...

	model = LCDM

	datasets = SN+HD
	
	analyzer = maxlike
	...

	[maxlike]
	;compute errror from Hessian matrix
	;False/True
	compute_errors = True

	;If withErrors is True
	;plot Fisher matrix
	show_contours = True

	;If showplot is True, then
	;2D plot for the parameters:
	plot_par1 = h
	plot_par2 = Om

	;[DerivedParameters]
	compute_derived = True


Lastly, we can run ``SimpleMC`` as in the `example Python script <quickstart.html#python-script>`_ using the ``ini file`` with the ``maxlike`` information.


..  _notebook:

Notebook example
-----------------

In the following notebook there is an example of the use of ``ga_deap`` and ``maxlike``.

.. raw:: html
   :file: notebook_optimizers.html

