MzDataFile
==========

.. py:class:: MzDataFile


   Bases: :py:class:`object`


Cython implementation of _MzDataFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MzDataFile.html
 -- Inherits from ['ProgressLogger']




.. py:method:: MzDataFile.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: MzDataFile.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: MzDataFile.getOptions


Cython signature: PeakFileOptions getOptions()
Returns the options for loading/storing




.. py:method:: MzDataFile.isSemanticallyValid


Cython signature: bool isSemanticallyValid(const String & filename, StringList & errors, StringList & warnings)


Checks if a file is valid with respect to the mapping file and the controlled vocabulary
-----
:param filename: File name of the file to be checked
:param errors: Errors during the validation are returned in this output parameter
:param warnings: Warnings during the validation are returned in this output parameter
-----
:raises:
  Exception: FileNotFound is thrown if the file could not be opened




.. py:method:: MzDataFile.load


Cython signature: void load(const String & filename, MSExperiment & map)


Loads a map from a MzData file
-----
:param filename: Directory of the file with the file name
:param map: It has to be a MSExperiment or have the same interface
-----
:raises:
  Exception: FileNotFound is thrown if the file could not be opened
:raises:
  Exception: ParseError is thrown if an error occurs during parsing




.. py:method:: MzDataFile.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: MzDataFile.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: MzDataFile.setOptions


Cython signature: void setOptions(PeakFileOptions)
Sets options for loading/storing




.. py:method:: MzDataFile.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: MzDataFile.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




.. py:method:: MzDataFile.store


Cython signature: void store(const String & filename, MSExperiment & map)


Stores a map in a MzData file
-----
:param filename: Directory of the file with the file name
:param map: It has to be a MSExperiment or have the same interface
-----
:raises:
  Exception: UnableToCreateFile is thrown if the file could not be created




