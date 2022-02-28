OfflinePrecursorIonSelection
============================

.. py:class:: OfflinePrecursorIonSelection


   Bases: :py:class:`object`


Cython implementation of _OfflinePrecursorIonSelection


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1OfflinePrecursorIonSelection.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: OfflinePrecursorIonSelection.createProteinSequenceBasedLPInclusionList


Cython signature: void createProteinSequenceBasedLPInclusionList(String include_, String rt_model_file, String pt_model_file, FeatureMap & precursors)




.. py:method:: OfflinePrecursorIonSelection.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: OfflinePrecursorIonSelection.getLPSolver


Cython signature: SOLVER getLPSolver()




.. py:method:: OfflinePrecursorIonSelection.getName


Cython signature: String getName()
Returns the name




.. py:method:: OfflinePrecursorIonSelection.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: OfflinePrecursorIonSelection.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: OfflinePrecursorIonSelection.makePrecursorSelectionForKnownLCMSMap


Cython signature: void makePrecursorSelectionForKnownLCMSMap(FeatureMap & features, MSExperiment & experiment, MSExperiment & ms2, libcpp_set[int] & charges_set, bool feature_based)


Makes the precursor selection for a given feature map, either feature or scan based
-----
:param features: Input feature map
:param experiment: Input raw data
:param ms2: Precursors are added as empty MS2 spectra to this MSExperiment
:param charges_set: Allowed charge states
:param feature_based: If true the selection is feature based, if false it is scan based and the highest signals in each spectrum are chosen




.. py:method:: OfflinePrecursorIonSelection.setLPSolver


Cython signature: void setLPSolver(SOLVER solver)




.. py:method:: OfflinePrecursorIonSelection.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: OfflinePrecursorIonSelection.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




