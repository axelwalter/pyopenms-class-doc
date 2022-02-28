OMSSAXMLFile
============

.. py:class:: OMSSAXMLFile


   Bases: :py:class:`object`


Cython implementation of _OMSSAXMLFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1OMSSAXMLFile.html
 -- Inherits from ['XMLFile']




.. py:method:: OMSSAXMLFile.getVersion


Cython signature: String getVersion()
Return the version of the schema




.. py:method:: OMSSAXMLFile.load


Cython signature: void load(const String & filename, ProteinIdentification & protein_identification, libcpp_vector[PeptideIdentification] & id_data, bool load_proteins, bool load_empty_hits)


Loads data from a OMSSAXML file
-----
:param filename: The file to be loaded
:param protein_identification: Protein identifications belonging to the whole experiment
:param id_data: The identifications with m/z and RT
:param load_proteins: If this flag is set to false, the protein identifications are not loaded
:param load_empty_hits: Many spectra will not return a hit. Report empty peptide identifications?




.. py:method:: OMSSAXMLFile.setModificationDefinitionsSet


Cython signature: void setModificationDefinitionsSet(ModificationDefinitionsSet rhs)
Sets the valid modifications




