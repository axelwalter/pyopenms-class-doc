KroenikFile
===========

.. py:class:: KroenikFile


   Bases: :py:class:`object`


Cython implementation of _KroenikFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1KroenikFile.html


 File adapter for Kroenik (HardKloer sibling) files
 -----
 The first line is the header and contains the column names:
 File,  First Scan,  Last Scan,  Num of Scans,  Charge,  Monoisotopic Mass,  Base Isotope Peak,  Best Intensity,  Summed Intensity,  First RTime,  Last RTime,  Best RTime,  Best Correlation,  Modifications
 -----
 Every subsequent line is a feature
 -----
 All properties in the file are converted to Feature properties, whereas "First Scan", "Last Scan", "Num of Scans" and "Modifications" are stored as
 metavalues with the following names "FirstScan", "LastScan", "NumOfScans" and "AveragineModifications"
 -----
 The width in m/z of the overall convex hull of each feature is set to 3 Th in lack of a value provided by the Kroenik file




.. py:method:: KroenikFile.load


Cython signature: void load(String filename, FeatureMap & feature_map)


Loads a Kroenik file into a featureXML
-----
The content of the file is stored in `features`
-----
:raises:
  Exception: FileNotFound is thrown if the file could not be opened
:raises:
  Exception: ParseError is thrown if an error occurs during parsing




.. py:method:: KroenikFile.store


Cython signature: void store(String filename, MSSpectrum & spectrum)
Stores a MSExperiment into a Kroenik file




