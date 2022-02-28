ConsensusXMLFile
================

.. py:class:: ConsensusXMLFile


   Bases: :py:class:`object`


Cython implementation of _ConsensusXMLFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ConsensusXMLFile.html




.. py:method:: ConsensusXMLFile.getOptions


Cython signature: PeakFileOptions getOptions()
Mutable access to the options for loading/storing




.. py:method:: ConsensusXMLFile.load


Cython signature: void load(String, ConsensusMap &)
Loads a consensus map from file and calls updateRanges




.. py:method:: ConsensusXMLFile.store


Cython signature: void store(String, ConsensusMap &)
Stores a consensus map to file




