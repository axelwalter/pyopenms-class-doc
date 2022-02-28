SpectrumAlignmentScore
======================

.. py:class:: SpectrumAlignmentScore


   Bases: :py:class:`object`


Cython implementation of _SpectrumAlignmentScore


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1SpectrumAlignmentScore.html
 -- Inherits from ['DefaultParamHandler']


 Similarity score via spectra alignment
 -----
 This class implements a simple scoring based on the alignment of spectra. This alignment
 is implemented in the SpectrumAlignment class and performs a dynamic programming alignment
 of the peaks, minimizing the distances between the aligned peaks and maximizing the number
 of peak pairs
 -----
 The scoring is done via the simple formula score = sum / (sqrt(sum1 * sum2)). sum is the
 product of the intensities of the aligned peaks, with the given exponent (default is 2)
 sum1 and sum2 are the sum of the intensities squared for each peak of both spectra respectively




.. py:method:: SpectrumAlignmentScore.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: SpectrumAlignmentScore.getName


Cython signature: String getName()
Returns the name




.. py:method:: SpectrumAlignmentScore.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: SpectrumAlignmentScore.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: SpectrumAlignmentScore.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: SpectrumAlignmentScore.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




