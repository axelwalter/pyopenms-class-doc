IndexedMzMLHandler
==================

.. py:class:: IndexedMzMLHandler


   Bases: :py:class:`object`


Cython implementation of _IndexedMzMLHandler


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1IndexedMzMLHandler.html




.. py:method:: IndexedMzMLHandler.getChromatogramById


Cython signature: shared_ptr[_Interfaces_Chromatogram] getChromatogramById(int id_)




.. py:method:: IndexedMzMLHandler.getMSChromatogramById


Cython signature: MSChromatogram getMSChromatogramById(int id_)




.. py:method:: IndexedMzMLHandler.getMSChromatogramByNativeId


Cython signature: void getMSChromatogramByNativeId(libcpp_string id_, MSChromatogram & chrom)




.. py:method:: IndexedMzMLHandler.getMSSpectrumById


Cython signature: MSSpectrum getMSSpectrumById(int id_)




.. py:method:: IndexedMzMLHandler.getMSSpectrumByNativeId


Cython signature: void getMSSpectrumByNativeId(libcpp_string id_, MSSpectrum & spec)




.. py:method:: IndexedMzMLHandler.getNrChromatograms


Cython signature: size_t getNrChromatograms()




.. py:method:: IndexedMzMLHandler.getNrSpectra


Cython signature: size_t getNrSpectra()




.. py:method:: IndexedMzMLHandler.getParsingSuccess


Cython signature: bool getParsingSuccess()




.. py:method:: IndexedMzMLHandler.getSpectrumById


Cython signature: shared_ptr[_Interfaces_Spectrum] getSpectrumById(int id_)




.. py:method:: IndexedMzMLHandler.openFile


Cython signature: void openFile(String filename)




.. py:method:: IndexedMzMLHandler.setSkipXMLChecks


Cython signature: void setSkipXMLChecks(bool skip)




