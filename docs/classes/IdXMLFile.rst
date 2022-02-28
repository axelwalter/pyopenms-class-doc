IdXMLFile
=========

.. py:class:: IdXMLFile


   Bases: :py:class:`object`


Cython implementation of _IdXMLFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1IdXMLFile.html




.. py:method:: IdXMLFile.load


Cython signature: void load(String filename, libcpp_vector[ProteinIdentification] & protein_ids, libcpp_vector[PeptideIdentification] & peptide_ids)
Loads the identifications of an idXML file without identifier




.. py:method:: IdXMLFile.store


- Cython signature: void store(String filename, libcpp_vector[ProteinIdentification] & protein_ids, libcpp_vector[PeptideIdentification] & peptide_ids, String document_id)
  Stores the data in an idXML file


- Cython signature: void store(String filename, libcpp_vector[ProteinIdentification] & protein_ids, libcpp_vector[PeptideIdentification] & peptide_ids)




