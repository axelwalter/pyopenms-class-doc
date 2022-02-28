FeatureGroupingAlgorithmKD
==========================

.. py:class:: FeatureGroupingAlgorithmKD


   Bases: :py:class:`object`


Cython implementation of _FeatureGroupingAlgorithmKD


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1FeatureGroupingAlgorithmKD.html
 -- Inherits from ['FeatureGroupingAlgorithm', 'ProgressLogger']




.. py:method:: FeatureGroupingAlgorithmKD.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: FeatureGroupingAlgorithmKD.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: FeatureGroupingAlgorithmKD.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: FeatureGroupingAlgorithmKD.getName


Cython signature: String getName()
Returns the name




.. py:method:: FeatureGroupingAlgorithmKD.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: FeatureGroupingAlgorithmKD.getProductName


Cython signature: String getProductName()
Returns the product name (for the Factory)




.. py:method:: FeatureGroupingAlgorithmKD.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: FeatureGroupingAlgorithmKD.group


- Cython signature: void group(libcpp_vector[FeatureMap] & maps, ConsensusMap & out)
- Cython signature: void group(libcpp_vector[ConsensusMap] & maps, ConsensusMap & out)




.. py:method:: FeatureGroupingAlgorithmKD.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: FeatureGroupingAlgorithmKD.registerChildren


Cython signature: void registerChildren()
Register all derived classes in this method




.. py:method:: FeatureGroupingAlgorithmKD.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: FeatureGroupingAlgorithmKD.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: FeatureGroupingAlgorithmKD.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: FeatureGroupingAlgorithmKD.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: FeatureGroupingAlgorithmKD.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




.. py:method:: FeatureGroupingAlgorithmKD.transferSubelements


Cython signature: void transferSubelements(libcpp_vector[ConsensusMap] maps, ConsensusMap & out)
Transfers subelements (grouped features) from input consensus maps to the result consensus map




