PSLPFormulation
===============

.. py:class:: PSLPFormulation


   Bases: :py:class:`object`


Cython implementation of _PSLPFormulation


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1PSLPFormulation.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: PSLPFormulation.createAndSolveILPForInclusionListCreation


Cython signature: void createAndSolveILPForInclusionListCreation(PrecursorIonSelectionPreprocessing & preprocessing, unsigned int ms2_spectra_per_rt_bin, unsigned int max_list_size, FeatureMap & precursors, bool solve_ILP)
Find a set of precursors, so that the protein coverage is maximal and that the number of precursors per bin is not exceeded




.. py:method:: PSLPFormulation.createAndSolveILPForKnownLCMSMapFeatureBased


Cython signature: void createAndSolveILPForKnownLCMSMapFeatureBased(FeatureMap & features, MSExperiment & experiment, libcpp_vector[IndexTriple] & variable_indices, libcpp_vector[libcpp_vector[libcpp_pair[size_t,size_t]]] & mass_ranges, libcpp_set[int] & charges_set, unsigned int ms2_spectra_per_rt_bin, libcpp_vector[int] & solution_indices)


Encode ILP formulation for a given LC-MS map, but unknown protein sample
-----
:param features: FeatureMap with all possible precursors
:param experiment: Input raw data
:param variable_indices: Assignment of feature indices and ILP variables
:param mass_ranges: Feature borders as indices in the raw data
:param charges_set: Allowed charge states
:param ms2_spectra_per_rt_bin: Allowed number of precursors per rt bin
:param solution_indices: Indices of ILP variables that are in the optimal solution




.. py:method:: PSLPFormulation.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: PSLPFormulation.getLPSolver


Cython signature: SOLVER getLPSolver()




.. py:method:: PSLPFormulation.getName


Cython signature: String getName()
Returns the name




.. py:method:: PSLPFormulation.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: PSLPFormulation.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: PSLPFormulation.setLPSolver


Cython signature: void setLPSolver(SOLVER solver)




.. py:method:: PSLPFormulation.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: PSLPFormulation.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: PSLPFormulation.solveILP


Cython signature: void solveILP(libcpp_vector[int] & solution_indices)
Solve the ILP




.. py:method:: PSLPFormulation.updateRTConstraintsForSequentialILP


Cython signature: void updateRTConstraintsForSequentialILP(size_t & rt_index, unsigned int ms2_spectra_per_rt_bin, size_t max_rt_index)




.. py:method:: PSLPFormulation.updateStepSizeConstraint


Cython signature: void updateStepSizeConstraint(size_t iteration, unsigned int step_size)




