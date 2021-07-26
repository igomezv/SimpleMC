**Run modules**
===================


driver
-------


This little code allows running SuperMC on command line given a *ini file*. It is the module that runs all the machinery.

Usage: 

.. code-block:: bash

   python driver.py file.ini


RunBase
---------
 .. note::

   * This module joins models with likelihood modules. 
   
   * Instance and set the priors values given the free parameters of the model.


 
* **SetPriors(T):** 
   Since a given theory **T** returns all the attributes of the parameters objects.

   Returns: [names, values, errorlist, boundlist, latexnames]

* **instantiatePars(T,values):** 
   This method returns a list of instances of Parameter objects with the sampler **values**.

* **ParseModel(model):** 
   Instance the model object corresponding to the chosen **model**.

* **ParseDataset(datasets):** Recives the **datasets** used and generates the likelihood objects. 


initializer
------------
 .. note::

   This module, from RunBase, prepares and instantiates what is necessary to run the driver.

* **TLinit(model,datasets):**
   
   Returns T (model object) evaluated at the model, and L (likelihood object) in at the datasets.

* **priorsTransform(theta, bounds, priortype):**
    
    Prior Transform for gaussian and flat priors.

* **getDims(T):**
   
   Returns the numbers of dimensions and the parameters list.


wqdriver
--------------

.. automodule:: Run.wqdriver
    :members:
    :undoc-members:
    :show-inheritance:

NestleConection
-----------------

See `NestleConection <nested_samplers.html#module-Run.NestleConection>`_ .

