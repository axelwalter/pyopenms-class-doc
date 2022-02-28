ExperimentalDesign_SampleSection
================================

.. py:class:: ExperimentalDesign_SampleSection


   Bases: :py:class:`object`


Cython implementation of _ExperimentalDesign_SampleSection


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ExperimentalDesign_SampleSection.html




.. py:method:: ExperimentalDesign_SampleSection.getFactorValue


Cython signature: String getFactorValue(unsigned int sample, String & factor)
Returns value of factor for given sample and factor name




.. py:method:: ExperimentalDesign_SampleSection.getFactors


Cython signature: libcpp_set[String] getFactors()
Returns a set of all factors (column names) that were defined for the sample section




.. py:method:: ExperimentalDesign_SampleSection.getSamples


Cython signature: libcpp_set[unsigned int] getSamples()
Returns a set of all samples that are present in the sample section




.. py:method:: ExperimentalDesign_SampleSection.hasFactor


Cython signature: bool hasFactor(String & factor)
Checks whether Sample Section has a specific factor (i.e. column name)




.. py:method:: ExperimentalDesign_SampleSection.hasSample


Cython signature: bool hasSample(unsigned int sample)
Checks whether sample section has row for a sample number




