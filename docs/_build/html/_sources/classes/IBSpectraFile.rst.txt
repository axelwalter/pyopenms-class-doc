IBSpectraFile
=============

.. py:class:: IBSpectraFile


   Bases: :py:class:`object`


Cython implementation of _IBSpectraFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1IBSpectraFile.html




.. py:method:: IBSpectraFile.store


Cython signature: void store(const String & filename, ConsensusMap & cm)


Writes the contents of the ConsensusMap cm into the file named by filename
-----
:param filename: The name of the file where the contents of cm should be stored
:param cm: The ConsensusMap that should be exported to filename
:raises:
  Exception: InvalidParameter if the ConsensusMap does not hold the result of an isobaric quantification experiment (e.g., itraq)




