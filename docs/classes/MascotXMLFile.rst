MascotXMLFile
=============

.. py:class:: MascotXMLFile


   Bases: :py:class:`object`


Cython implementation of _MascotXMLFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MascotXMLFile.html
 -- Inherits from ['XMLFile']




.. py:method:: MascotXMLFile.getVersion


Cython signature: String getVersion()
Return the version of the schema




.. py:method:: MascotXMLFile.initializeLookup


Cython signature: void initializeLookup(SpectrumMetaDataLookup & lookup, MSExperiment & experiment, const String & scan_regex)


Initializes a helper object for looking up spectrum meta data (RT, m/z)
-----
:param lookup: Helper object to initialize
:param experiment: Experiment containing the spectra
:param scan_regex: Optional regular expression for extracting information from references to spectra




.. py:method:: MascotXMLFile.load


Cython signature: void load(const String & filename, ProteinIdentification & protein_identification, libcpp_vector[PeptideIdentification] & id_data, SpectrumMetaDataLookup & rt_mapping)


Loads data from a Mascot XML file
-----
:param filename: The file to be loaded
:param protein_identification: Protein identifications belonging to the whole experiment
:param id_data: The identifications with m/z and RT
:param lookup: Helper object for looking up spectrum meta data
:raises:
  Exception: FileNotFound is thrown if the file does not exists
:raises:
  Exception: ParseError is thrown if the file does not suit to the standard




