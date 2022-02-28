MorphologicalFilter
===================

.. py:class:: MorphologicalFilter


   Bases: :py:class:`object`


Cython implementation of _MorphologicalFilter


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MorphologicalFilter.html
 -- Inherits from ['DefaultParamHandler', 'ProgressLogger']




.. py:method:: MorphologicalFilter.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: MorphologicalFilter.filter


Cython signature: void filter(MSSpectrum & spectrum)


Applies the morphological filtering operation to an MSSpectrum
-----
If the size of the structuring element is given in 'Thomson', the number of data points for
the structuring element is computed as follows:




.. py:method:: MorphologicalFilter.filterExperiment


Cython signature: void filterExperiment(MSExperiment & exp)


Applies the morphological filtering operation to an MSExperiment
-----
The size of the structuring element is computed for each spectrum individually, if it is given in 'Thomson'
See the filtering method for MSSpectrum for details




.. py:method:: MorphologicalFilter.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: MorphologicalFilter.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: MorphologicalFilter.getName


Cython signature: String getName()
Returns the name




.. py:method:: MorphologicalFilter.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: MorphologicalFilter.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: MorphologicalFilter.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: MorphologicalFilter.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: MorphologicalFilter.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: MorphologicalFilter.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: MorphologicalFilter.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: MorphologicalFilter.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




