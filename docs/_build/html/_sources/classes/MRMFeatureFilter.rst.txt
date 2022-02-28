MRMFeatureFilter
================

.. py:class:: MRMFeatureFilter


   Bases: :py:class:`object`


Cython implementation of _MRMFeatureFilter


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MRMFeatureFilter.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: MRMFeatureFilter.FilterFeatureMap


Cython signature: void FilterFeatureMap(FeatureMap features, MRMFeatureQC filter_criteria, TargetedExperiment transitions)


Flags or filters features and subordinates in a FeatureMap
-----
:param features: FeatureMap to flag or filter
:param filter_criteria: MRMFeatureQC class defining QC parameters
:param transitions: Transitions from a TargetedExperiment




.. py:method:: MRMFeatureFilter.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: MRMFeatureFilter.getName


Cython signature: String getName()
Returns the name




.. py:method:: MRMFeatureFilter.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: MRMFeatureFilter.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: MRMFeatureFilter.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: MRMFeatureFilter.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




