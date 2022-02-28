CachedMzMLHandler
=================

.. py:class:: CachedMzMLHandler


   Bases: :py:class:`object`


Cython implementation of _CachedMzMLHandler


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS::Internal_1_1CachedMzMLHandler.html
 -- Inherits from ['ProgressLogger']




.. py:method:: CachedMzMLHandler.createMemdumpIndex


Cython signature: void createMemdumpIndex(String filename)
Create an index on the location of all the spectra and chromatograms




.. py:method:: CachedMzMLHandler.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: CachedMzMLHandler.getChromatogramIndex


Cython signature: libcpp_vector[streampos] getChromatogramIndex()




.. py:method:: CachedMzMLHandler.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: CachedMzMLHandler.getSpectraIndex


Cython signature: libcpp_vector[streampos] getSpectraIndex()




.. py:method:: CachedMzMLHandler.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: CachedMzMLHandler.readMemdump


Cython signature: void readMemdump(MSExperiment exp, String filename)
Read all spectra from a dump from the disk




.. py:method:: CachedMzMLHandler.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: CachedMzMLHandler.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: CachedMzMLHandler.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




.. py:method:: CachedMzMLHandler.writeMemdump


Cython signature: void writeMemdump(MSExperiment exp, String out)
Write complete spectra as a dump to the disk




.. py:method:: CachedMzMLHandler.writeMetadata


Cython signature: void writeMetadata(MSExperiment exp, String out_meta)
Write only the meta data of an MSExperiment




