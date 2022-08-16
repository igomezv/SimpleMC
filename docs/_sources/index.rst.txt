===========
SimpleMC
===========

**[Site under construction]**
**[Last update 15/08/2022]**


This is the ``SimpleMC`` documentation, a Python package for cosmological parameter estimation and model comparison using Bayesian inference, optimization and machine learning algorithms. ``SimpleMC`` also contains a collection of tools for cosmological data analysis, such as a `cosmological calculator <tuto_cosmocalc.html>`_, `plotting utilities <tuto_plotters.html>`_ and other statistical issues. The cosmological models included in ``SimpleMC`` are Dark Energy models where only expansion history matters.

There are 3 options to install, or use, ``SimpleMC``: 

1) You can use ``SimpleMC`` in Google Colab, please see the Section `Using Google Colab in Requirements <requirements.html#using-google-colab>`_.

2) On the other hand, you can visit the `GitHub code repository <https://github.com/ja-vazquez/SimpleMC.git>`_, download the `source code here <https://github.com/ja-vazquez/SimpleMC/archive/refs/heads/master.zip>`_ or clone it as follows:

   .. code-block:: bash

      git clone https://github.com/ja-vazquez/SimpleMC.git

Then, you can install it:

   .. code-block:: bash

      cd SimpleMC
      
      pip3 install -e .


3) Also, you can install ``SimpleMC`` without clonning: 

   .. code-block:: bash
   	
   	  pip3 install -e git+https://github.com/ja-vazquez/SimpleMC#egg=simplemc
   	  

In a few days, the pip install option will be available ``pip3 install simplemc``.


Please read the `introduction <intro.html>`_ section where you can see the `requirements <intro.html#requirements>`_  and a simple `quick start <intro.html#quick-start>`_. In the `tutorials section <tutorials.html>`_ you can find several examples of ``SimpleMC`` functions.


``SimpleMC`` employs amazing external codes and algorithms, please go to the `citation  section <Citation.html#cite-external-codes>`_ for details if you feel it is pertinent to cite them.


Extended index
---------------

.. toctree::
   :maxdepth: 3

   intro
   
   structure

   tutorials

   Citation

   API


Changelog
----------

- **0.9.8.6 (24/05/2022)** Fix MCMCAnalyzer and update requirements.
- **0.9.8.6 (27/04/2022)** Fix mpi4py import in MCMCAnalyzer and allow to work it with only 1 processor. 
- **0.9.8.5 (23/02/2022)** Improving postprocessing. 
- **0.9.8.4 (12/01/2022)** Unifying binned and full Pantheon likelihoods. Added covariance matrix in postprocessing. Added AIC information criterion. Saving output of individuals from GADeap. 
- **0.9.8.3 (17/12/2021)** Fix binned Pantheon data and likelihood. Save maxloglikes in postprocessing. Reordering optimizers. 
- **0.9.8.2 (04/11/2021)** Update paths of datasets, setup and requirements.
- **0.9.8.1 (06/09/2021)** Setup file and pypy install ready. Data in likelihood modules use relative paths. 
- **0.9.8 (06/09/2021)** Improvements in postprocessing. Return dictionaries in DriverMC.executer. Correction in the reading of the columns by mcevidence.
- **0.9.7 (02/09/2021)** Add emcee and mcevidence source codes (modified). Fix output texfile of ga_deap. Delete old genetic algorithm.
- **0.9.6.8 (12/08/2021)** Summary output to all analyzers. Remove nestle engine. 
- **0.9.6.5 (09/08/2021)** Add ga_deap options in ini file. 
- **0.9.6 (7/06/2021)** Unify simple and generic models, test generic likelihood.
- **0.9.5.8 (26/04/2021)** Quintom with coupling and curvature. Beta version of neuralike. Warnings for non-essential libraries.
- **0.9.5.4 (21/03/2021)** Fixed parameter estimation problem in Summary of nested chains.
- **0.9.5.2 (07/02/2021)** GA from deap working with fisher matrix for errors.
- **0.9.5 (19/09/2020)** Test and fix bambi with modified dynesty.
- **0.9.4 (25/06/2020)** Working on neutrinos. New models: logt, IBEG, anisotropic, brans-dickie. Maxanalizer and fisher working. 
- **0.9.3.5 (05/06/2020)** SimpleMC Workshop via Zoom for ICF-UNAM
- **0.9.3 (02/06/2020)** Fix typos and little errrors. DriverMC. Testing models and cosmology. Running and cleanning genetic functions.
- **0.9.2 (23/04/2020)** adding modified dynesty. Postprocessing. Compressed data. GR for a single chain.
- **0.9.1 (06/04/2020)** paralelise MCMC and added GR. Simple plots. Nested samplers. Updating hubble diagram to 31 points. 
- **0.9.0 (28/11/2019)** Gelman-Rubin diagnostics for MCMCAnalyzer. Ini files. Generic models and likelihoods.
- **0.8.9 (25/11/2019)** Moving likelihoods into a likelihoods folder and models on to models folder.
- **0.8.7 (20/11/2019)** Adding HD and full JLA. Ordering directories.
- **0.8.6 (20/08/2019)** Bug in the MCMC sampler.
- **0.8.5 (29/04/2019)** Updated Lya likelihood to DR14.
- **0.8.4 (23/03/2019)** python 3, towards eBOSS.
- **0.8.3 (10/10/2017)** Added binned cosmology.
- **0.8.2 (25/07/2017)** DR12 and DR14 data.
- **0.8.1 (06/01/2016)** Added sampling test for demonstration of MCMC.
- **0.8.0 (01/09/2014)** Initial version.


TO DO
------
- Add nerualike. 

