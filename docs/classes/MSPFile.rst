MSPFile
=======

.. py:class:: MSPFile


   Bases: :py:class:`object`


Cython implementation of _MSPFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MSPFile.html




.. py:method:: MSPFile.load


Cython signature: void load(String filename, libcpp_vector[PeptideIdentification] & ids, MSExperiment & exp)


Loads a map from a MSPFile file
-----
:param exp: PeakMap which contains the spectra after reading
:param filename: The filename of the experiment
:param ids: Output parameter which contains the peptide identifications from the spectra annotations




.. py:method:: MSPFile.store


Cython signature: void store(String filename, MSExperiment & exp)
Stores a map in a MSPFile file




