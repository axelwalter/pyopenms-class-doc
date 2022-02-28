PepXMLFile
==========

.. py:class:: PepXMLFile


   Bases: :py:class:`object`


Cython implementation of _PepXMLFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1PepXMLFile.html




.. py:method:: PepXMLFile.keepNativeSpectrumName


Cython signature: void keepNativeSpectrumName(bool keep)




.. py:method:: PepXMLFile.load


- Cython signature: void load(String filename, libcpp_vector[ProteinIdentification] & protein_ids, libcpp_vector[PeptideIdentification] & peptide_ids)
- Cython signature: void load(String filename, libcpp_vector[ProteinIdentification] & protein_ids, libcpp_vector[PeptideIdentification] & peptide_ids, String experiment_name)
- Cython signature: void load(String filename, libcpp_vector[ProteinIdentification] & protein_ids, libcpp_vector[PeptideIdentification] & peptide_ids, String experiment_name, SpectrumMetaDataLookup lookup)




.. py:method:: PepXMLFile.setParseUnknownScores


Cython signature: void setParseUnknownScores(bool parse_unknown_scores)




.. py:method:: PepXMLFile.store


- Cython signature: void store(String filename, libcpp_vector[ProteinIdentification] & protein_ids, libcpp_vector[PeptideIdentification] & peptide_ids)
- Cython signature: void store(String filename, libcpp_vector[ProteinIdentification] & protein_ids, libcpp_vector[PeptideIdentification] & peptide_ids, String mz_file, String mz_name, bool peptideprophet_analyzed, double rt_tolerance)




