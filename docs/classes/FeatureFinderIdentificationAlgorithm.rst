FeatureFinderIdentificationAlgorithm
====================================

.. py:class:: FeatureFinderIdentificationAlgorithm


   Bases: :py:class:`object`


Cython implementation of _FeatureFinderIdentificationAlgorithm


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1FeatureFinderIdentificationAlgorithm.html
 -- Inherits from ['DefaultParamHandler']


 Algorithm class for FeatureFinderIdentification
 -----
 External IDs (peptides_ext, proteins_ext) may be empty,
 in which case no machine learning or FDR estimation will be performed.
 Optional seeds from e.g. untargeted FeatureFinders can be added with
 seeds.
 Results will be written to features .
 Caution: peptide IDs will be shrunk to best hit, FFid metavalues added
 and potential seed IDs added.
 -----
 Usage:
   from pyopenms import *
   from urllib.request import urlretrieve
   urlretrieve("https://raw.githubusercontent.com/OpenMS/OpenMS/develop/src/tests/topp/FeatureFinderIdentification_1_input.mzML", "FeatureFinderIdentification_1_input.mzML")
   urlretrieve("https://raw.githubusercontent.com/OpenMS/OpenMS/develop/src/tests/topp/FeatureFinderIdentification_1_input.idXML", "FeatureFinderIdentification_1_input.idXML")
   #
   ffid_algo = FeatureFinderIdentificationAlgorithm()
   # load ms data from mzML
   mzml = MzMLFile()
   mzml_options = mzml.getOptions()
   mzml_options.addMSLevel(1) # only MS1
   mzml.setOptions(mzml_options)
   #
   exp = MSExperiment()
   mzml.load("FeatureFinderIdentification_1_input.mzML", exp)
   ffid_algo.setMSData(exp)
   # annotate mzML file
   features = FeatureMap()
   features.setPrimaryMSRunPath([b"FeatureFinderIdentification_1_input.idXML"], ffid_algo.getMSData())
   #
   peptides = []
   proteins = []
   peptides_ext = []
   proteins_ext = []
   IdXMLFile().load("FeatureFinderIdentification_1_input.idXML", proteins, peptides)
   #
   #"internal" IDs:
   ffid_algo.run(peptides, proteins, peptides_ext, proteins_ext, features)
   #
   # Terminal output:
   # Summary statistics (counting distinct peptides including PTMs):
   # 22 peptides identified (22 internal, 0 additional external)
   # 16 peptides with features (16 internal, 0 external)
   # 6 peptides without features (6 internal, 0 external)
 -----




.. py:method:: FeatureFinderIdentificationAlgorithm.getChromatograms


Cython signature: MSExperiment getChromatograms()
Returns chromatogram data as MSExperiment




.. py:method:: FeatureFinderIdentificationAlgorithm.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: FeatureFinderIdentificationAlgorithm.getLibrary


Cython signature: TargetedExperiment getLibrary()
Returns constructed assay library




.. py:method:: FeatureFinderIdentificationAlgorithm.getMSData


Cython signature: MSExperiment getMSData()
Returns ms data as MSExperiment




.. py:method:: FeatureFinderIdentificationAlgorithm.getName


Cython signature: String getName()
Returns the name




.. py:method:: FeatureFinderIdentificationAlgorithm.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: FeatureFinderIdentificationAlgorithm.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: FeatureFinderIdentificationAlgorithm.run


         - Cython signature: void run(libcpp_vector[PeptideIdentification] peptides, libcpp_vector[ProteinIdentification] & proteins, libcpp_vector[PeptideIdentification] peptides_ext, libcpp_vector[ProteinIdentification] proteins_ext, FeatureMap & features)


Run feature detection
:param peptides: Vector of identified peptides
:param proteins: Vector of identified proteins
:param peptides_ext: Vector of external identified peptides, can be used to transfer ids from other runs
:param proteins_ext: Vector of external identified proteins, can be used to transfer ids from other runs
:param features: Feature detection results will be added here
         - Cython signature: void run(libcpp_vector[PeptideIdentification] peptides, libcpp_vector[ProteinIdentification] & proteins, libcpp_vector[PeptideIdentification] peptides_ext, libcpp_vector[ProteinIdentification] proteins_ext, FeatureMap & features, FeatureMap & seeds)


Run feature detection
:param peptides: Vector of identified peptides
:param proteins: Vector of identified proteins
:param peptides_ext: Vector of external identified peptides, can be used to transfer ids from other runs
:param proteins_ext: Vector of external identified proteins, can be used to transfer ids from other runs
:param features: Feature detection results will be added here
:param seeds: Optional seeds for feature detection from e.g. untargeted FeatureFinders
         - Cython signature: void run(libcpp_vector[PeptideIdentification] peptides, libcpp_vector[ProteinIdentification] & proteins, libcpp_vector[PeptideIdentification] peptides_ext, libcpp_vector[ProteinIdentification] proteins_ext, FeatureMap & features, FeatureMap & seeds, String & spectra_file)


Run feature detection
:param peptides: Vector of identified peptides
:param proteins: Vector of identified proteins
:param peptides_ext: Vector of external identified peptides, can be used to transfer ids from other runs
:param proteins_ext: Vector of external identified proteins, can be used to transfer ids from other runs
:param features: Feature detection results will be added here
:param seeds: Optional seeds for feature detection from e.g. untargeted FeatureFinders
:param spectra_file: Path will be stored in features in case the MSExperiment has no proper primaryMSRunPath




.. py:method:: FeatureFinderIdentificationAlgorithm.runOnCandidates


Cython signature: void runOnCandidates(FeatureMap & features)
Run feature detection on identified features (e.g. loaded from an IdXML file)




.. py:method:: FeatureFinderIdentificationAlgorithm.setMSData


Cython signature: void setMSData(const MSExperiment &)
Sets ms data




.. py:method:: FeatureFinderIdentificationAlgorithm.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: FeatureFinderIdentificationAlgorithm.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




