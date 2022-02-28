OMSSACSVFile
============

.. py:class:: OMSSACSVFile


   Bases: :py:class:`object`


Cython implementation of _OMSSACSVFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1OMSSACSVFile.html


 File adapter for OMSSACSV files
 -----
 The files contain the results of the OMSSA algorithm in a comma separated manner. This file adapter is able to
 load the data from such a file into the structures of OpenMS




.. py:method:: OMSSACSVFile.load


Cython signature: void load(const String & filename, ProteinIdentification & protein_identification, libcpp_vector[PeptideIdentification] & id_data)


Loads a OMSSA file
-----
:param filename: The name of the file to read from
:param protein_identification: The protein ProteinIdentification data
:param id_data: The peptide ids of the file
-----
The content of the file is stored in `features`
-----
:raises:
  Exception: FileNotFound is thrown if the file could not be opened
:raises:
  Exception: ParseError is thrown if an error occurs during parsing




