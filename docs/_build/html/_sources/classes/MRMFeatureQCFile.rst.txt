MRMFeatureQCFile
================

.. py:class:: MRMFeatureQCFile


   Bases: :py:class:`object`


Cython implementation of _MRMFeatureQCFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MRMFeatureQCFile.html


 File adapter for MRMFeatureQC files
 -----
 Loads and stores .csv or .tsv files describing an MRMFeatureQC




.. py:method:: MRMFeatureQCFile.load


Cython signature: void load(const String & filename, MRMFeatureQC & mrmfqc, const bool is_component_group)


Loads an MRMFeatureQC file
-----
:param filename: The path to the input file
:param mrmfqc: The output class which will contain the criteria
:param is_component_group: True if the user intends to load ComponentGroupQCs data, false otherwise
-----
:raises:
  Exception: FileNotFound is thrown if the file could not be opened
:raises:
  Exception: ParseError is thrown if an error occurs during parsing




