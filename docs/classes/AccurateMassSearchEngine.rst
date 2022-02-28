AccurateMassSearchEngine
========================

.. py:class:: AccurateMassSearchEngine


   Bases: :py:class:`object`


Cython implementation of _AccurateMassSearchEngine


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1AccurateMassSearchEngine.html
 -- Inherits from ['DefaultParamHandler', 'ProgressLogger']




.. py:method:: AccurateMassSearchEngine.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: AccurateMassSearchEngine.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: AccurateMassSearchEngine.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: AccurateMassSearchEngine.getName


Cython signature: String getName()
Returns the name




.. py:method:: AccurateMassSearchEngine.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: AccurateMassSearchEngine.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: AccurateMassSearchEngine.init


Cython signature: void init()




.. py:method:: AccurateMassSearchEngine.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: AccurateMassSearchEngine.queryByConsensusFeature


Cython signature: void queryByConsensusFeature(ConsensusFeature cfeat, size_t cf_index, size_t number_of_maps, String ion_mode, libcpp_vector[AccurateMassSearchResult] & results)




.. py:method:: AccurateMassSearchEngine.queryByFeature


Cython signature: void queryByFeature(Feature feature, size_t feature_index, String ion_mode, libcpp_vector[AccurateMassSearchResult] &)




.. py:method:: AccurateMassSearchEngine.queryByMZ


Cython signature: void queryByMZ(double observed_mz, int observed_charge, String ion_mode, libcpp_vector[AccurateMassSearchResult] &, EmpiricalFormula & observed_adduct)




.. py:method:: AccurateMassSearchEngine.run


- Cython signature: void run(FeatureMap &, MzTab &)
- Cython signature: void run(ConsensusMap &, MzTab &)




.. py:method:: AccurateMassSearchEngine.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: AccurateMassSearchEngine.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: AccurateMassSearchEngine.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: AccurateMassSearchEngine.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: AccurateMassSearchEngine.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




