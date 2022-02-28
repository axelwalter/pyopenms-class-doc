FeatureGroupingAlgorithmUnlabeled
=================================

.. py:class:: FeatureGroupingAlgorithmUnlabeled


   Bases: :py:class:`object`


Cython implementation of _FeatureGroupingAlgorithmUnlabeled


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1FeatureGroupingAlgorithmUnlabeled.html
 -- Inherits from ['FeatureGroupingAlgorithm']




.. py:method:: FeatureGroupingAlgorithmUnlabeled.addToGroup


Cython signature: void addToGroup(int map_id, FeatureMap feature_map)




.. py:method:: FeatureGroupingAlgorithmUnlabeled.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: FeatureGroupingAlgorithmUnlabeled.getName


Cython signature: String getName()
Returns the name




.. py:method:: FeatureGroupingAlgorithmUnlabeled.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: FeatureGroupingAlgorithmUnlabeled.getProductName


Cython signature: String getProductName()




.. py:method:: FeatureGroupingAlgorithmUnlabeled.getResultMap


Cython signature: ConsensusMap getResultMap()




.. py:method:: FeatureGroupingAlgorithmUnlabeled.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: FeatureGroupingAlgorithmUnlabeled.group


Cython signature: void group(libcpp_vector[FeatureMap] & maps, ConsensusMap & out)




.. py:method:: FeatureGroupingAlgorithmUnlabeled.registerChildren


Cython signature: void registerChildren()
Register all derived classes in this method




.. py:method:: FeatureGroupingAlgorithmUnlabeled.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: FeatureGroupingAlgorithmUnlabeled.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: FeatureGroupingAlgorithmUnlabeled.setReference


Cython signature: void setReference(int map_id, FeatureMap map)




.. py:method:: FeatureGroupingAlgorithmUnlabeled.transferSubelements


Cython signature: void transferSubelements(libcpp_vector[ConsensusMap] maps, ConsensusMap & out)
Transfers subelements (grouped features) from input consensus maps to the result consensus map




