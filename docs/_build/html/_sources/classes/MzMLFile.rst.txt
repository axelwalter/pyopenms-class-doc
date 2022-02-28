MzMLFile
========

.. py:class:: MzMLFile


   Bases: :py:class:`object`


Cython implementation of _MzMLFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MzMLFile.html
 -- Inherits from ['ProgressLogger']


 File adapter for MzML files
 -----
 Provides methods to load and store MzML files.
 PeakFileOptions allow to load a reduced subset of the data into an MSExperiment.
 -----
 See help(MSExperiment) how data is stored after loading.
 See help(PeakFileOptions) for available options.
 -----
 Usage:
   exp = MSExperiment()
   MzMLFile().load("test.mzML", exp)
   spec = []
   for s in exp.getSpectra():
     if s.getMSLevel() != 1:
       spec.append(s)
   exp.setSpectra(spec)
   MzMLFile().store("filtered.mzML", exp)
 -----




.. py:method:: MzMLFile.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: MzMLFile.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: MzMLFile.getOptions


Cython signature: PeakFileOptions getOptions()




.. py:method:: MzMLFile.isSemanticallyValid


Cython signature: bool isSemanticallyValid(const String & filename, StringList & errors, StringList & warnings)




.. py:method:: MzMLFile.load


Cython signature: void load(const String & filename, MSExperiment &)
Loads from an MzML file. Spectra and chromatograms are sorted by default (this can be disabled using PeakFileOptions)




.. py:method:: MzMLFile.loadBuffer


Cython signature: void loadBuffer(const String & input, MSExperiment & exp)


Loads a map from a MzML file stored in a buffer (in memory)
-----
:param buffer: The buffer with the data (i.e. string with content of an mzML file)
:param exp: Is an MSExperiment
-----
:raises:
  Exception: ParseError is thrown if an error occurs during parsing




.. py:method:: MzMLFile.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: MzMLFile.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: MzMLFile.setOptions


Cython signature: void setOptions(PeakFileOptions)
Set PeakFileOptions to perform filtering during loading. E.g., to load only MS1 spectra or meta data only




.. py:method:: MzMLFile.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: MzMLFile.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




.. py:method:: MzMLFile.store


Cython signature: void store(const String & filename, MSExperiment &)
Stores a MSExperiment in an MzML file




.. py:method:: MzMLFile.storeBuffer


Cython signature: void storeBuffer(String & output, MSExperiment exp)


Stores a map in an output string
-----
:param output: An empty string to store the result
:param exp: Has to be an MSExperiment




.. py:method:: MzMLFile.transform




