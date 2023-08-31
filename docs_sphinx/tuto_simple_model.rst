How to create a new model
==========================

Unfortunately, to use a model that is not included in ``SimpleMC`` we cannot use the ``ini file``, however it is still very easy. There are two options:

  * :ref:`simple_model`

  * :ref:`simple_cosmo_model`



..  _simple_model:

Simple model independent of any cosmology
------------------------------------------

You can propose any function that you want. Define your parameters with Parameter class and use the DriverMC class to an easy-use manager. 

.. code-block:: python
   
    from simplemc.cosmo.Parameter import Parameter
    from simplemc.DriverMC import DriverMC

The Parameter class have the structure:

Parameter(name string,  value intermediate, step size, (bound_inf, bound_sup), LaTeX name) 

The name of the variables must to be the same at the name of the Parameter. Then gather your parameter objects in a list:

.. code-block:: python

    m = Parameter("m", 0, 0.05, (0, 0.1), "m_0")
    b = Parameter("b", 3, 0.05, (0, 5), "b_0")

    # create a list with your parameters objects
    parameterlist = [m, b]


Define a method that reads a list of parameters,

.. code-block:: python

    def my_model(parameterlist, x):
        m, b = parameterlist
        return m*x+b

Use SimpleMC as usually, but with ``model = simple``

.. code-block:: python

    analyzer = DriverMC(model='simple', datasets='dline', analyzername='mcmc',
                        custom_parameters=parameterlist, custom_function=my_model)

    analyzer.executer(nsamp=1000)


..  _simple_cosmo_model:

Simple cosmological model based on LCDM
-----------------------------------------

Now we use ``model = simple_cosmo`` and we can use the LCDM parameters in the expresion of the model (Ocb, Omrad, Om, Ombh2, h and NuContrib) and add extra parameters. This expression must be in terms of a (scale factor) and definied in a string. For example:

.. code-block:: python

    from simplemc.cosmo.Parameter import Parameter
    from simplemc.DriverMC import DriverMC

    Oextra = Parameter('Oextra', 0.1, 0.001, (0, 0.2), '\Omega_{extra}')

    cosmo_model = 'Om/a**3+Omrad/a**4+(1.0-Om-Oextra)'

    analyzer = DriverMC(model='simple_cosmo', datasets='SN', analyzername='mcmc',
                        custom_parameters=parameterlist, custom_function=cosmo_model)
                   
It is important to note that the name of the Parameter instances must be the same as the string names of the Parameter class (first argument of the Parameter class).


