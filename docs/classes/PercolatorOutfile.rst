PercolatorOutfile
=================

.. py:class:: PercolatorOutfile


   Bases: :py:class:`object`


Cython implementation of _PercolatorOutfile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1PercolatorOutfile.html


 Class for reading Percolator tab-delimited output files
 -----
 For PSM-level output, the file extension should be ".psms"




.. py:attribute:: PercolatorOutfile.PercolatorOutfile_ScoreType


alias of :py:class:`pyopenms.pyopenms_7.__PercolatorOutfile_ScoreType`


.. py:method:: PercolatorOutfile.getScoreType


Cython signature: PercolatorOutfile_ScoreType getScoreType(String score_type_name)
Returns a score type given its name




.. py:method:: PercolatorOutfile.load


Cython signature: void load(const String & filename, ProteinIdentification & proteins, libcpp_vector[PeptideIdentification] & peptides, SpectrumMetaDataLookup & lookup, PercolatorOutfile_ScoreType output_score)
Loads a Percolator output file




