Set a prior probability density function
==========================================

The goal of Bayesian inference is to sample an unknown posterior probability distribution and thus to get an idea of how probable a theoretical model is given a set of data. To do this, it is worthwhile to establish two probabilities at hand: the likelihood and the prior.

Given a dataset *D* and a model with :math:`\theta` free parameters, it is worth reminding the Bayes' theorem:

.. math::

   P(\theta| D)= \frac{P(D|\theta)P(\theta)}{P(D)},
   
where the likelihood function :math:`P(D|\theta)` is defined according to the data involved and the priori probability :math:`P(\theta)` contains the prior knowledge about the model parameters. It is common that this a priori likelihood function can be a uniform distribution in which the bounds of the parameter values are set. Another common approach is that the prior probability is assumed to be a Gaussian distribution. In ``SimpleMC`` both types of priors can be used for nested sampling, but for MCMC we can only use (for the moment) uniform priors. To define the priors we need to use the ``Parameter class`` and set the bounds of each parameter; for example, if we know that the matter density parameter :math:`\Omega_m` is between 0.25 and 0.35, we can write it as follows:

.. code-block:: python

    from simplemc.cosmo.Parameter import Parameter	
    
    Om = Parameter("Om", 0.28, 0.05, (0.25, 0.35), "\Omega_m")

Then, if we use nested sampling, in the `ini file <inifile.html>`_ we can choose between uniform or Gaussian prior:

.. code-block::
        
    [custom]
    ...
    ...

    [nested]
    ...
    ...
    ;u for flat(uniform) or g for gaussian prior
    priortype = u
    ;when using gaussian prior
    sigma = 2

In the ``simplemc.cosmo.paramDefs`` module there is a collection of cosmological parameters already defined and you can edit their bounds at your convenience. If you want to create a new parameter, you can write it in this module, or define it externally as in the `Simple Model <tuto_simple_model.html>`_ and `Simple Likelihood <tuto_simple_likelihood.html>`_ examples.

