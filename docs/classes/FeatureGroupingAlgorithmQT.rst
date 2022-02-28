FeatureGroupingAlgorithmQT
==========================

.. py:class:: FeatureGroupingAlgorithmQT


   Bases: :py:class:`object`


Cython implementation of _FeatureGroupingAlgorithmQT


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1FeatureGroupingAlgorithmQT.html
 -- Inherits from ['FeatureGroupingAlgorithm']




.. py:method:: FeatureGroupingAlgorithmQT.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: FeatureGroupingAlgorithmQT.getName


Cython signature: String getName()
Returns the name




.. py:method:: FeatureGroupingAlgorithmQT.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: FeatureGroupingAlgorithmQT.getProductName


Cython signature: String getProductName()




.. py:method:: FeatureGroupingAlgorithmQT.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: FeatureGroupingAlgorithmQT.group


- Cython signature: void group(libcpp_vector[FeatureMap] & maps, ConsensusMap & out)
- Cython signature: void group(libcpp_vector[ConsensusMap] & maps, ConsensusMap & out)




.. py:method:: FeatureGroupingAlgorithmQT.registerChildren


Cython signature: void registerChildren()
Register all derived classes in this method




.. py:method:: FeatureGroupingAlgorithmQT.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: FeatureGroupingAlgorithmQT.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: FeatureGroupingAlgorithmQT.transferSubelements


Cython signature: void transferSubelements(libcpp_vector[ConsensusMap] maps, ConsensusMap & out)
Transfers subelements (grouped features) from input consensus maps to the result consensus map




