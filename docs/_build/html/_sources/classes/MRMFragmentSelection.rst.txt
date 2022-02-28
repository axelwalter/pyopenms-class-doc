MRMFragmentSelection
====================

.. py:class:: MRMFragmentSelection


   Bases: :py:class:`object`


Cython implementation of _MRMFragmentSelection


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MRMFragmentSelection.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: MRMFragmentSelection.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: MRMFragmentSelection.getName


Cython signature: String getName()
Returns the name




.. py:method:: MRMFragmentSelection.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: MRMFragmentSelection.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: MRMFragmentSelection.selectFragments


Cython signature: void selectFragments(libcpp_vector[Peak1D] & selected_peaks, MSSpectrum & spec)
Selects accordingly to the parameters the best peaks of spec and writes them into `selected_peaks`




.. py:method:: MRMFragmentSelection.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: MRMFragmentSelection.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




