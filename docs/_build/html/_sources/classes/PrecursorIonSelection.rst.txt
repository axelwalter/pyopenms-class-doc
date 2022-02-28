PrecursorIonSelection
=====================

.. py:class:: PrecursorIonSelection


   Bases: :py:class:`object`


Cython implementation of _PrecursorIonSelection


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1PrecursorIonSelection.html
 -- Inherits from ['DefaultParamHandler']




.. py:attribute:: PrecursorIonSelection.PrecursorIonSelection_Type


alias of :py:class:`pyopenms.pyopenms_8.__PrecursorIonSelection_Type`


.. py:method:: PrecursorIonSelection.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: PrecursorIonSelection.getLPSolver


Cython signature: SOLVER getLPSolver()




.. py:method:: PrecursorIonSelection.getMaxScore


Cython signature: double getMaxScore()




.. py:method:: PrecursorIonSelection.getName


Cython signature: String getName()
Returns the name




.. py:method:: PrecursorIonSelection.getNextPrecursors


         - Cython signature: void getNextPrecursors(FeatureMap & features, FeatureMap & next_features, unsigned int number)


Returns features with highest score for MS/MS
-----
:param features: FeatureMap with all possible precursors
:param next_features: FeatureMap with next precursors
:param number: Number of features to be reported
         - Cython signature: void getNextPrecursors(libcpp_vector[int] & solution_indices, libcpp_vector[IndexTriple] & variable_indices, libcpp_set[int] & measured_variables, FeatureMap & features, FeatureMap & new_features, unsigned int step_size, PSLPFormulation & ilp)




.. py:method:: PrecursorIonSelection.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: PrecursorIonSelection.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: PrecursorIonSelection.rescore


Cython signature: void rescore(FeatureMap & features, libcpp_vector[PeptideIdentification] & new_pep_ids, libcpp_vector[ProteinIdentification] & prot_ids, PrecursorIonSelectionPreprocessing & preprocessed_db, bool check_meta_values)


Change scoring of features using peptide identifications from all spectra
-----
:param features: FeatureMap with all possible precursors
:param new_pep_ids: Peptide identifications
:param prot_ids: Protein identifications
:param preprocessed_db: Information from preprocessed database
:param check_meta_values: True if the FeatureMap should be checked for the presence of required meta values




.. py:method:: PrecursorIonSelection.reset


Cython signature: void reset()




.. py:method:: PrecursorIonSelection.setLPSolver


Cython signature: void setLPSolver(SOLVER solver)




.. py:method:: PrecursorIonSelection.setMaxScore


Cython signature: void setMaxScore(double & max_score)




.. py:method:: PrecursorIonSelection.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: PrecursorIonSelection.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: PrecursorIonSelection.simulateRun


Cython signature: void simulateRun(FeatureMap & features, libcpp_vector[PeptideIdentification] & pep_ids, libcpp_vector[ProteinIdentification] & prot_ids, PrecursorIonSelectionPreprocessing & preprocessed_db, String path, MSExperiment & experiment, String precursor_path)


Simulate the iterative precursor ion selection
-----
:param features: FeatureMap with all possible precursors
:param new_pep_ids: Peptide identifications
:param prot_ids: Protein identifications
:param preprocessed_db: Information from preprocessed database
:param step_size: Number of MS/MS spectra considered per iteration
:param path: Path to output file




.. py:method:: PrecursorIonSelection.sortByTotalScore


Cython signature: void sortByTotalScore(FeatureMap & features)
Sort features by total score




