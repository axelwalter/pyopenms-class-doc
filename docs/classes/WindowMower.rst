WindowMower
===========

.. py:class:: WindowMower


   Bases: :py:class:`object`


Cython implementation of _WindowMower


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1WindowMower.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: WindowMower.filterPeakMap


Cython signature: void filterPeakMap(MSExperiment & exp)




.. py:method:: WindowMower.filterPeakSpectrum


Cython signature: void filterPeakSpectrum(MSSpectrum & spec)




.. py:method:: WindowMower.filterPeakSpectrumForTopNInJumpingWindow


Cython signature: void filterPeakSpectrumForTopNInJumpingWindow(MSSpectrum & spectrum)
Jumping window version (faster)




.. py:method:: WindowMower.filterPeakSpectrumForTopNInSlidingWindow


Cython signature: void filterPeakSpectrumForTopNInSlidingWindow(MSSpectrum & spectrum)
Sliding window version (slower)




.. py:method:: WindowMower.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: WindowMower.getName


Cython signature: String getName()
Returns the name




.. py:method:: WindowMower.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: WindowMower.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: WindowMower.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: WindowMower.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




