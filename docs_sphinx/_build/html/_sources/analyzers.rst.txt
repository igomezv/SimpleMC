**Analyzers**
=============

SimpleMC contains the following analyzers:

.. list-table:: Analyzers
   :widths: 15 20 25 40
   :header-rows: 1

   * - Analyzer key
     - Type
     - Description
     - Tasks

   * - mcmc
     - Bayesian inference
     - Metropolis-Hastings algorithm
     - Parameter estimation

   * - nested
     - Bayesian inference
     - Nested sampling algorithms from Dynesty library 

       [arXiv:1904.02180]
     - Parameter estimation and model comparison

   * - emcee
     - Bayesian inference
     - EMCEE algorithm

       [arXiv:1202.3665]
     - Parameter estimation 

   * - MaxLikeAnalyzer
     - Optimization
     - L-BFGS-B algorithm
       
       https://docs.scipy.org/doc/scipy/reference/optimize.minimize-lbfgsb.html
     - Likelihood maximization

   * - ga_deap
     - Optimization
     - Collection of genetic algorithms from DEAP library

       Fortin, F. A., et al (2012). 

       DEAP: Evolutionary algorithms made easy. 

       The Journal of Machine Learning Research, 13(1), 2171-2175.

     - Likelihood maximization


We recommend for a previous quickly test, to use an optimizer before an Bayesian inference algorithm.


Sampler comparison
-------------------

.. note:: 

   To verify the consistency of the parameter estimation among the different samplers available, we have made the following graph.

.. figure:: /img/samplersTriangle.png

     We estimates the posteriors of the parameters of the owaCDM model (dark energy with timedependent equation-of-state in a model of unknown curvature) using Supernovae type Ia, Cosmic Chronometers (Hubble Distance) and BAO .








