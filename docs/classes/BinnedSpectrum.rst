BinnedSpectrum
==============

.. py:class:: BinnedSpectrum


   Bases: :py:class:`object`


Cython implementation of _BinnedSpectrum


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1BinnedSpectrum.html




.. py:method:: BinnedSpectrum.getBinIndex


Cython signature: unsigned int getBinIndex(float mz)
Returns the bin index of a given m/z position




.. py:method:: BinnedSpectrum.getBinIntensity


Cython signature: float getBinIntensity(double mz)
Returns the bin intensity at a given m/z position




.. py:method:: BinnedSpectrum.getBinLowerMZ


Cython signature: float getBinLowerMZ(size_t i)
Returns the lower m/z of a bin given its index




.. py:method:: BinnedSpectrum.getBinSize


Cython signature: float getBinSize()
Returns the bin size




.. py:method:: BinnedSpectrum.getBinSpread


Cython signature: unsigned int getBinSpread()
Returns the bin spread




.. py:method:: BinnedSpectrum.getOffset


Cython signature: float getOffset()
Returns offset




.. py:method:: BinnedSpectrum.getPrecursors


Cython signature: libcpp_vector[Precursor] getPrecursors()




.. py:method:: BinnedSpectrum.isCompatible


Cython signature: bool isCompatible(BinnedSpectrum & a, BinnedSpectrum & b)




