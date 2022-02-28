OSWFile
=======

.. py:class:: OSWFile


   Bases: :py:class:`object`


Cython implementation of _OSWFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1OSWFile.html


 This class serves for reading in and writing OpenSWATH OSW files
 -----
 See OpenSwathOSWWriter for more functionality
 -----
 The reader and writer returns data in a format suitable for PercolatorAdapter.
 OSW files have a flexible data structure. They contain all peptide query
 parameters of TraML/PQP files with the detected and quantified features of
 OpenSwathWorkflow (feature, feature_ms1, feature_ms2 & feature_transition)
 -----
 The OSWFile reader extracts the feature information from the OSW file for
 each level (MS1, MS2 & transition) separately and generates Percolator input
 files. For each of the three Percolator reports, OSWFile writer adds a table
 (score_ms1, score_ms2, score_transition) with the respective confidence metrics.
 These tables can be mapped to the corresponding feature tables, are very similar
 to PyProphet results and can thus be used interchangeably




