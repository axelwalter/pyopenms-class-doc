ProtXMLFile
===========

.. py:class:: ProtXMLFile


   Bases: :py:class:`object`


Cython implementation of _ProtXMLFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ProtXMLFile.html


 Used to load (storing not supported, yet) ProtXML files
 -----
 This class is used to load (storing not supported, yet) documents that implement
 the schema of ProtXML files




.. py:method:: ProtXMLFile.load


Cython signature: void load(String filename, ProteinIdentification & protein_ids, PeptideIdentification & peptide_ids)


Loads the identifications of an ProtXML file without identifier
-----
The information is read in and the information is stored in the
corresponding variables
-----
:raises:
  Exception: FileNotFound is thrown if the file could not be found
:raises:
  Exception: ParseError is thrown if an error occurs during parsing




.. py:method:: ProtXMLFile.store


Cython signature: void store(String filename, ProteinIdentification & protein_ids, PeptideIdentification & peptide_ids, String document_id)




