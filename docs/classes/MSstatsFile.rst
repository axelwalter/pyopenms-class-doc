MSstatsFile
===========

.. py:class:: MSstatsFile


   Bases: :py:class:`object`


Cython implementation of _MSstatsFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MSstatsFile.html




.. py:method:: MSstatsFile.storeISO


Cython signature: void storeISO(String & filename, ConsensusMap & consensus_map, ExperimentalDesign & design, StringList & reannotate_filenames, String & bioreplicate, String & condition, String & mixture, String & retention_time_summarization_method)
Store isobaric experiment (MSstatsTMT)




.. py:method:: MSstatsFile.storeLFQ


Cython signature: void storeLFQ(String & filename, ConsensusMap & consensus_map, ExperimentalDesign & design, StringList & reannotate_filenames, bool is_isotope_label_type, String & bioreplicate, String & condition, String & retention_time_summarization_method)
Store label free experiment (MSstats)




