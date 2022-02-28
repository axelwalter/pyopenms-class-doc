FileHandler
===========

.. py:class:: FileHandler


   Bases: :py:class:`object`


Cython implementation of _FileHandler


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1FileHandler.html




.. py:method:: FileHandler.computeFileHash


Cython signature: String computeFileHash(const String & filename)




.. py:method:: FileHandler.getOptions


Cython signature: PeakFileOptions getOptions()
Access to the options for loading/storing




.. py:method:: FileHandler.getType


Cython signature: int getType(const String & filename)




.. py:method:: FileHandler.getTypeByContent


Cython signature: FileType getTypeByContent(const String & filename)




.. py:method:: FileHandler.getTypeByFileName


Cython signature: FileType getTypeByFileName(const String & filename)




.. py:method:: FileHandler.hasValidExtension


Cython signature: bool hasValidExtension(const String & filename, FileType type_)




.. py:method:: FileHandler.isSupported


Cython signature: bool isSupported(FileType type_)




.. py:method:: FileHandler.loadExperiment


Cython signature: bool loadExperiment(String, MSExperiment &)


Loads a file into an MSExperiment
-----
:param filename: The file name of the file to load
:param exp: The experiment to load the data into
:param force_type: Forces to load the file with that file type. If no type is forced, it is determined from the extension (or from the content if that fails)
:param log: Progress logging mode
:param rewrite_source_file: Set's the SourceFile name and path to the current file. Note that this looses the link to the primary MS run the file originated from
:param compute_hash: If source files are rewritten, this flag triggers a recomputation of hash values. A SHA1 string gets stored in the checksum member of SourceFile
:returns: true if the file could be loaded, false otherwise
:raises:
  Exception: FileNotFound is thrown if the file could not be opened
:raises:
  Exception: ParseError is thrown if an error occurs during parsing
Stores an MSExperiment to a file
-----
The file type to store the data in is determined by the file name. Supported formats for storing are mzML, mzXML, mzData and DTA2D. If the file format cannot be determined from the file name, the mzML format is used
-----
:param filename: The name of the file to store the data in
:param exp: The experiment to store
:param log: Progress logging mode
:raises:
  Exception: UnableToCreateFile is thrown if the file could not be written
Loads a file into a FeatureMap
-----
:param filename: The file name of the file to load
:param map: The FeatureMap to load the data into
:param force_type: Forces to load the file with that file type. If no type is forced, it is determined from the extension (or from the content if that fails)
:returns: true if the file could be loaded, false otherwise
:raises:
  Exception: FileNotFound is thrown if the file could not be opened
:raises:
  Exception: ParseError is thrown if an error occurs during parsing




.. py:method:: FileHandler.loadFeatures


Cython signature: bool loadFeatures(String, FeatureMap &)


Loads a file into a FeatureMap
-----
:param filename: The file name of the file to load
:param map: The FeatureMap to load the data into
:param force_type: Forces to load the file with that file type. If no type is forced, it is determined from the extension (or from the content if that fails)
:returns: true if the file could be loaded, false otherwise
:raises:
  Exception: FileNotFound is thrown if the file could not be opened
:raises:
  Exception: ParseError is thrown if an error occurs during parsing




.. py:method:: FileHandler.setOptions


Cython signature: void setOptions(PeakFileOptions)
Sets options for loading/storing




.. py:method:: FileHandler.storeExperiment


Cython signature: void storeExperiment(String, MSExperiment)


Stores an MSExperiment to a file
-----
The file type to store the data in is determined by the file name. Supported formats for storing are mzML, mzXML, mzData and DTA2D. If the file format cannot be determined from the file name, the mzML format is used
-----
:param filename: The name of the file to store the data in
:param exp: The experiment to store
:param log: Progress logging mode
:raises:
  Exception: UnableToCreateFile is thrown if the file could not be written
Loads a file into a FeatureMap
-----
:param filename: The file name of the file to load
:param map: The FeatureMap to load the data into
:param force_type: Forces to load the file with that file type. If no type is forced, it is determined from the extension (or from the content if that fails)
:returns: true if the file could be loaded, false otherwise
:raises:
  Exception: FileNotFound is thrown if the file could not be opened
:raises:
  Exception: ParseError is thrown if an error occurs during parsing




.. py:method:: FileHandler.stripExtension


Cython signature: String stripExtension(String file)




.. py:method:: FileHandler.swapExtension


Cython signature: String swapExtension(String filename, FileType new_type)




