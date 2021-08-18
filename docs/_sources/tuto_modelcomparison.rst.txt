Model comparison with Bayesian evidence
========================================

Model comparison between two models can be performed with Bayesian inference using Bayesian evidence obtained by nested sampling (or ``MCEvidence`` for other samplers). To do this, it is neccesary to `run a Bayesian inference process <tuto_lcdm_bayesian.html>`_ for each of the two models and be fair using the same datasets. 

Bayesian evidence is:

.. math::

	Z = P(D)=\int_{\mathbb{R}^N} P(D|\theta)P(\theta)d\theta,
	
and is an output value of a nested sampling process. To perform model comparison we can use the Bayes factor. 

The Bayes factor :math:`B_{0,1}` of the *Model 0* with respect to *Model 1* is the ratio of their respective Bayesian evidences:

.. math::

	B_{0,1} = \frac{Z_0}{Z_1}

or in logarithm:

.. math::

	\ln B_{0,1} = \ln Z_0 - \ln Z_1
    
The following table has the Jeffrey's scale, where the strength of the Bayesian evidence Z is in favours of the *Model 0* over the *Model 1*.

.. list-table:: 
   :widths: 50 50
   :header-rows: 1

   * - :math:`\ln B_{0,1}`
     - Strength of Z

   * - :math:`<1`
     - Inconclusive

   * - :math:`1-2.5`
     - Significant

   * - :math:`2.5-5`
     - Strong
     
   * - :math:`>5`
     - Decisive


If you want to estimate Bayesian evidence without nested sampling, i.e., using ``mcmc`` or ``emcee``, you can use ``MCEvidence`` as follows:

.. code-block:: bash

  [custom]
  ...
  ...
  analyzer = mcmc
  mcevidence = True
  ...
  