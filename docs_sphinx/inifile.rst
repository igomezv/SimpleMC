==================
Customize ini file
==================

The ``ini file`` to ``SimpleMC`` configuration must have a module ``[custom]`` and according to the selected analyzer can have several modules: ``[mcmc]``, ``[nested]``, ``[neural]``, ``[neuralike]``, ``[MaxLikeAnalyzer]``, ``[emcee]``, ``[genetic]``, ``[ga_deap]``. In this section, we explain each of them. To more details about analyzers, pleas visit the `Analyzer sections <analyzers.html>`_.

- ``[custom]``
    - Requiered keys: 
        
        - ``model`` : visit `Models section <models.html>`_ to see the options.
        
        - ``datasets`` : visit `Data section <data.html>`_ to see all the datasets options.
        

    - Other keys: 

        -  ``analyzer``: mcmc, nested, genetic, MaxLikeAnalyzer, ga_deap. By default: mcmc.

        - ``chainsdir``: directory to save the outputs. By default ``simplemc/chain``.

    **Example:**

    .. code-block:: bash

            [custom]

            chainsdir = chains
            
            model = LCDM
            
            datasets = BBAO+HD+SN

            analyzer = mcmc


- ``[mcmc]``
    - Keys:
        - nsamp: number of steps.
        - skip: burn-in samples.
        - temp: temperature. 
        - chainno: number of chains.
        - addderived: If you want to add derived parameters such as the age of the Universe.

    **Example:**
    
    .. code-block:: bash

          [mcmc]
          nsamp   = 4000
          skip    = 100
          temp    = 2
          chainno = 1
          addderived = False


- ``[nested]``
    - Keys:
        - dynamic: If you want dynamic nested sampling. 
        - neuralNetwork: if you can to use neural network to speed-up the process. Currently only works for one processor. 
        - nestedType: nested sampling algorithm, can be {'single','multi', 'balls', 'cubes'}.
        - nlivepoints: number of live points.
        - accuracy: difference of Bayesian evidence between two iterations that indicates the stopping criterion. 
        - priortype: u->uniform, g->gaussian.
        - nproc: number of processors.

    **Example**

    .. code-block:: bash
    
            dynamic = no
            neuralNetwork = no
            nestedType = multi
            nlivepoints = 500
            accuracy = 0.01

            priortype = u

            nproc = 0


- ``[neural]``
    At the current time, this block only have sense if analyzer is nested and if nproc=1. 

    - Keys:
        - numNeurons: number of neurons of the three hidden layers.
        - epochs: number of epochs. 
        - dlogz_start: value of dlogz to start to train the neural net. 
        - it_to_start_net: iterations to start the trainning. 
        - updInt: number of iterations to re-train the neural net. 

    **Example:**
    
    .. code-block:: bash
            
            [neural]
            numNeurons = 50
            epochs = 100
            dlogz_start = 5
            it_to_start_net = 10000
            updInt = 500



..  _baseConfig:

baseConfig.ini
---------------

.. code-block:: bash
         
    [custom]
    ;directory for chains/output
    ;it is better if you set an absolute path
    chainsdir = simplemc/chains

    ;set model
    ;model options: LCDM, LCDMasslessnu, nuLCDM, NeffLCDM, noradLCDM, nuoLCDM,
    ;nuwLCDM, oLCDM, wCDM, waCDM, owCDM, owaCDM, JordiCDM, WeirdCDM, TLight, StepCDM,
    ;Spline, PolyCDM, fPolyCDM, Decay, Decay01, Decay05, EarlyDE, EarlyDE_rd_DE, SlowRDE, sline
    ;more options located in the RunBase.py
    model = LCDM

    ;prefact options : [pre, phy]
    prefact = phy

    ;varys8 True otherwise s8=0.8
    varys8  = False

    ;set datasets used. Ex: UnionSN+BBAO+Planck
    ;data options: HD, BBAO, GBAO, GBAO_no6dF, CMASS, LBAO, LaBAO,
    ;LxBAO, MGS, Planck, WMAP, PlRd, WRd, PlDa, PlRdx10, CMBW, SN, SNx10, UnionSN,
    ;RiessH0, 6dFGS, dline, generic
    datasets = HD

    ;following four lines is to use external datasets
    ;fn can be distance_mod, h, fs8
    ;datasets = generic
    ;path_to_data = /home/cosmocicatais/panth15.txt
    ;path_to_cov = /home/cosmocicatais/panth15cov.txt
    ;fn = distance_mod


    ;sampler can be {mcmc, nested, emcee}
    ;or analyzers {maxlike, genetic, ga_deap}
    ;
    ;mcmc -> metropolis-hastings
    ;nested -> nested sampling
    ;emcee
    ;maxlike -> Maximum Likelihood Analyzer
    ;genetic -> ga_deap (genetic using deap library)
    analyzername = mcmc


    ;add derived parameters (True/False) ,
    ;i.e. Omega_Lambda, H0, Age of the Universe
    addDerived = False

    ;mcevidence = True to calculate Bayesian evidence wiht mcevidence
    ;Only valid to samplers (mcmc, emcee, nested).
    ;Nested sampling does not need it.
    mcevidence = True

    ;overwrite = True -> overwrite output files with the same name
    ;overwrite = False -> if the outputname already exist
    ;it sends an error and ends the simplemc execution
    overwrite = True

    ;options to triangle plots for mcmc, nested and emcee;
    ;if True any of the following options
    ;.png files will be saved in chainsdir
    getdist = False
    corner = True
    simpleplot = True
    ;True to display figures; we recommended false
    showfig = True

    ;use neural network to predict likelihoods (True/False),
    ;edit block neuralike to set options
    useNeuralLike = False


    [mcmc]
    ;Nsamples
    nsamp   = 500

    ;Burn-in
    skip    = 0

    ;temperature at which to sample
    temp    = 2

    ; Gelman-Rubin for convergence
    GRstop  = 0.01

    ;every number of steps check the GR-criteria
    checkGR = 50

    ;1 if single cpu , otherwise is giving by the nproc-> mpi -np #
    chainno = 0


    [nested]
    ;type for dynesty -> {'single','multi', 'balls', 'cubes'}
    nestedType = multi 

    ;it is recommended around nlivepoints=50*ndim, recommended 1024
    nlivepoints = 50


    ;recommended 0.01
    accuracy =5

    ;u for flat(uniform) or g for gaussian prior
    priortype = u

    ;when using gaussian prior
    sigma = 2


    ;if nproc = 0 uses mp.cpu_count()//2 by default, 
    ;you can set with another positive integer
    nproc = 2

    ;Produce output on the fly
    showfiles = True

    ;dynamic option is only for dynesty engine
    ;dynamic and neuralNetwork can be False/True
    dynamic = False

    neuralNetwork = False

    ;if neuralNetwork = True, then you can set:

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

    [emcee]
    ;walkers >= 2*dim
    walkers = 10
    nsamp = 200
    burnin = 0
    nproc = 4


    [maxlike]
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

    ;[DerivedParameters]
    compute_derived = True


    ;genetic parameters

    [ga_deap]
    ;Population size
    population = 20
    ;Crossover probability
    crossover = 0.7
    ;Mutation probability
    mutation = 0.3
    ;Max generation number
    max_generation = 50
    ;Size of the Hall of Fame
    hof_size = 1
    ;Crowding factor
    crowding_factor = 1

    ;Plot Generation vs Fitness
    plot_fitness = True

    ;compute errror from Hessian matrix
    ;False/True
    compute_errors = True

    ;If compute_errors is True
    ;plot Fisher matrix
    show_contours = True

    ;If show_contours is True, then
    ;2D plot for the parameters:
    plot_param1 = h
    plot_param2 = Om


.. note::

   Considerations:
  
   * *prefact* and *nsamp* are only for Metropolis-Hastings.

   * *nlivepoints* and *accuracy* are only for nested sampling.

   * *sampler* options are:
   
      * mcmc : Metropolis-Hastings.
      * nested : Nested Sampling

   * *sampler* can be one *optimizer* of the following:
      
      * MaxLikeAnalyzer : from scipy.optimize.minimize
      * genetic : a Simple Genetic Algorithm
      

   * *skip* is burnin. 
  
   * For *priortype* u is uniform prior and g gaussian prior. At this time, only nested sampling accept both of them.
   
   * *chainsdir* is the directory where the chains in a text file and the plots will be saved.

