SequestOutfile
==============

.. py:class:: SequestOutfile


   Bases: :py:class:`object`


Cython implementation of _SequestOutfile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1SequestOutfile.html


 Representation of a Sequest output file




.. py:method:: SequestOutfile.getACAndACType


Cython signature: void getACAndACType(String line, String & accession, String & accession_type)
Retrieves the accession type and accession number from a protein description line




.. py:method:: SequestOutfile.getColumns


Cython signature: bool getColumns(const String & line, libcpp_vector[String] & substrings, size_t number_of_columns, size_t reference_column)
Retrieves columns from a Sequest outfile line




.. py:method:: SequestOutfile.getSequences




.. py:method:: SequestOutfile.load


Cython signature: void load(const String & result_filename, libcpp_vector[PeptideIdentification] & peptide_identifications, ProteinIdentification & protein_identification, double p_value_threshold, libcpp_vector[double] & pvalues, const String & database, bool ignore_proteins_per_peptide)


Loads data from a Sequest outfile
-----
:param result_filename: The file to be loaded
:param peptide_identifications: The identifications
:param protein_identification: The protein identifications
:param p_value_threshold: The significance level (for the peptide hit scores)
:param pvalues: A list with the pvalues of the peptides (pvalues computed with peptide prophet)
:param database: The database used for the search
:param ignore_proteins_per_peptide: This is a hack to deal with files that use a suffix like "+1" in column "Reference", but do not actually list extra protein references in subsequent lines




