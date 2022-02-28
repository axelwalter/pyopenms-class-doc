MzIdentMLFile
=============

.. py:class:: MzIdentMLFile


   Bases: :py:class:`object`


Cython implementation of _MzIdentMLFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MzIdentMLFile.html
 -- Inherits from ['ProgressLogger']




.. py:method:: MzIdentMLFile.endProgress


Cython signature: void endProgress()
Ends the progress display




.. py:method:: MzIdentMLFile.getLogType


Cython signature: LogType getLogType()
Returns the type of progress log being used




.. py:method:: MzIdentMLFile.isSemanticallyValid


Cython signature: bool isSemanticallyValid(String filename, StringList errors, StringList warnings)


Checks if a file is valid with respect to the mapping file and the controlled vocabulary
-----
:param filename: File name of the file to be checked
:param errors: Errors during the validation are returned in this output parameter
:param warnings: Warnings during the validation are returned in this output parameter
-----
:raises:
  Exception: FileNotFound is thrown if the file could not be opened




.. py:method:: MzIdentMLFile.load


Cython signature: void load(String filename, libcpp_vector[ProteinIdentification] & poid, libcpp_vector[PeptideIdentification] & peid)


Loads the identifications from a MzIdentML file
-----
:param filename: File name of the file to be checked
-----
:raises:
  Exception: FileNotFound is thrown if the file could not be opened
:raises:
  Exception: ParseError is thrown if an error occurs during parsin




.. py:method:: MzIdentMLFile.nextProgress


Cython signature: void nextProgress()
Increment progress by 1 (according to range begin-end)




.. py:method:: MzIdentMLFile.setLogType


Cython signature: void setLogType(LogType)
Sets the progress log that should be used. The default type is NONE!




.. py:method:: MzIdentMLFile.setProgress


Cython signature: void setProgress(ptrdiff_t value)
Sets the current progress




.. py:method:: MzIdentMLFile.startProgress


Cython signature: void startProgress(ptrdiff_t begin, ptrdiff_t end, String label)




.. py:method:: MzIdentMLFile.store


Cython signature: void store(String filename, libcpp_vector[ProteinIdentification] & poid, libcpp_vector[PeptideIdentification] & peid)


Stores the identifications in a MzIdentML file
-----
:raises:
  Exception: UnableToCreateFile is thrown if the file could not be created




