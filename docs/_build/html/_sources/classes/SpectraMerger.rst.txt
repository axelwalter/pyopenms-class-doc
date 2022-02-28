SpectraMerger
=============

.. py:class:: SpectraMerger


   Bases: :py:class:`object`


Cython implementation of _SpectraMerger


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1SpectraMerger.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: SpectraMerger.average


Cython signature: void average(MSExperiment & exp, String average_type)


Average over neighbouring spectra
-----
:param exp: Experimental data to be averaged
:param average_type: Averaging type to be used ("gaussian" or "tophat")




.. py:method:: SpectraMerger.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: SpectraMerger.getName


Cython signature: String getName()
Returns the name




.. py:method:: SpectraMerger.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: SpectraMerger.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: SpectraMerger.mergeSpectraBlockWise


Cython signature: void mergeSpectraBlockWise(MSExperiment & exp)




.. py:method:: SpectraMerger.mergeSpectraPrecursors


Cython signature: void mergeSpectraPrecursors(MSExperiment & exp)
Merges spectra with similar precursors (must have MS2 level)




.. py:method:: SpectraMerger.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: SpectraMerger.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




