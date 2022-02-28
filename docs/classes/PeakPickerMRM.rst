PeakPickerMRM
=============

.. py:class:: PeakPickerMRM


   Bases: :py:class:`object`


Cython implementation of _PeakPickerMRM


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1PeakPickerMRM.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: PeakPickerMRM.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: PeakPickerMRM.getName


Cython signature: String getName()
Returns the name




.. py:method:: PeakPickerMRM.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: PeakPickerMRM.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: PeakPickerMRM.pickChromatogram


Cython signature: void pickChromatogram(MSChromatogram & chromatogram, MSChromatogram & picked_chrom)


Finds peaks in a single chromatogram and annotates left/right borders
-----
It uses a modified algorithm of the PeakPickerHiRes
-----
This function will return a picked chromatogram




.. py:method:: PeakPickerMRM.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: PeakPickerMRM.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




