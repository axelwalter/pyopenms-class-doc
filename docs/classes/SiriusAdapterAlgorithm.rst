SiriusAdapterAlgorithm
======================

.. py:class:: SiriusAdapterAlgorithm


   Bases: :py:class:`object`


Cython implementation of _SiriusAdapterAlgorithm


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1SiriusAdapterAlgorithm.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: SiriusAdapterAlgorithm.callSiriusQProcess


Cython signature: libcpp_vector[String] callSiriusQProcess(const String & tmp_ms_file, const String & tmp_out_dir, String & executable, const String & out_csifingerid, bool decoy_generation)


Call SIRIUS with QProcess
-----
:param tmp_ms_file: Path to temporary .ms file
:param tmp_out_dir: Path to temporary output folder
:param executable: Path to executable
:param out_csifingerid: Path to CSI:FingerID output (can be empty)




.. py:method:: SiriusAdapterAlgorithm.determineSiriusExecutable


Cython signature: String determineSiriusExecutable(String & executable)


Checks if the provided String points to a valid SIRIUS executable, otherwise tries
to select the executable from the environment
-----
:param executable: Path to the potential executable
:returns: Path to SIRIUS executable




.. py:method:: SiriusAdapterAlgorithm.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: SiriusAdapterAlgorithm.getFilterByNumMassTraces


Cython signature: unsigned int getFilterByNumMassTraces()




.. py:method:: SiriusAdapterAlgorithm.getIsotopePatternIterations


Cython signature: int getIsotopePatternIterations()




.. py:method:: SiriusAdapterAlgorithm.getName


Cython signature: String getName()
Returns the name




.. py:method:: SiriusAdapterAlgorithm.getNumberOfCSIFingerIDCandidates


Cython signature: int getNumberOfCSIFingerIDCandidates()




.. py:method:: SiriusAdapterAlgorithm.getNumberOfSiriusCandidates


Cython signature: int getNumberOfSiriusCandidates()




.. py:method:: SiriusAdapterAlgorithm.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: SiriusAdapterAlgorithm.getPrecursorMzTolerance


Cython signature: double getPrecursorMzTolerance()




.. py:method:: SiriusAdapterAlgorithm.getPrecursorRtTolerance


Cython signature: double getPrecursorRtTolerance()




.. py:method:: SiriusAdapterAlgorithm.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: SiriusAdapterAlgorithm.isFeatureOnly


Cython signature: bool isFeatureOnly()




.. py:method:: SiriusAdapterAlgorithm.isNoMasstraceInfoIsotopePattern


Cython signature: bool isNoMasstraceInfoIsotopePattern()




.. py:method:: SiriusAdapterAlgorithm.logFeatureSpectraNumber


Cython signature: void logFeatureSpectraNumber(const String & featureinfo, FeatureMapping_FeatureToMs2Indices & feature_mapping, MSExperiment & spectra)


Logs number of features and spectra used
-----
Prints the number of features and spectra used (OPENMS_LOG_INFO)
-----
:param featureinfo: Path to featureXML
:param feature_mapping: FeatureToMs2Indices with feature mapping
:param spectra: Input of MSExperiment with spectra information




.. py:method:: SiriusAdapterAlgorithm.precursorMzToleranceUnitIsPPM


Cython signature: bool precursorMzToleranceUnitIsPPM()




.. py:method:: SiriusAdapterAlgorithm.preprocessingSirius


Cython signature: void preprocessingSirius(const String & featureinfo, MSExperiment & spectra, FeatureMapping_FeatureMappingInfo & fm_info, FeatureMapping_FeatureToMs2Indices & feature_mapping)


Preprocessing needed for SIRIUS
-----
Filter number of masstraces and perform feature mapping
-----
:param featureinfo: Path to featureXML
:param spectra: Input of MSExperiment with spectra information
:param fm_info: Emtpy - stores FeatureMaps and KDTreeMaps internally
:param feature_mapping: Empty FeatureToMs2Indices




.. py:method:: SiriusAdapterAlgorithm.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: SiriusAdapterAlgorithm.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: SiriusAdapterAlgorithm.sortSiriusWorkspacePathsByScanIndex


Cython signature: void sortSiriusWorkspacePathsByScanIndex(libcpp_vector[String] & subdirs)




