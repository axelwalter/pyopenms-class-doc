IdentificationDataConverter
===========================

.. py:class:: IdentificationDataConverter


   Bases: :py:class:`object`


Cython implementation of _IdentificationDataConverter


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1IdentificationDataConverter.html




.. py:method:: IdentificationDataConverter.exportIDs


Cython signature: void exportIDs(const IdentificationData & id_data, libcpp_vector[ProteinIdentification] & proteins, libcpp_vector[PeptideIdentification] & peptides, bool export_oligonucleotides)
Export to legacy peptide/protein identifications




.. py:method:: IdentificationDataConverter.exportMzTab


Cython signature: MzTab exportMzTab(const IdentificationData & id_data)
Export to mzTab format




.. py:method:: IdentificationDataConverter.importIDs


Cython signature: void importIDs(IdentificationData & id_data, const libcpp_vector[ProteinIdentification] & proteins, const libcpp_vector[PeptideIdentification] & peptides)
Import from legacy peptide/protein identifications




