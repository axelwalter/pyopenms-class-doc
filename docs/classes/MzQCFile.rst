MzQCFile
========

.. py:class:: MzQCFile


   Bases: :py:class:`object`


Cython implementation of _MzQCFile


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MzQCFile.html


 File adapter for mzQC files used to load and store mzQC files
 -----
 This class collects the data for the mzQC File




.. py:method:: MzQCFile.store


Cython signature: void store(String input_file, String output_file, MSExperiment & exp, String contact_name, String contact_address, String description, String label, FeatureMap & feature_map, libcpp_vector[ProteinIdentification] & prot_ids, libcpp_vector[PeptideIdentification] & pep_ids)


Stores QC data in mzQC file with JSON format
:param input_file: MzML input file name
:param output_file: MzQC output file name
:param exp: MSExperiment to extract QC data from, prior sortSpectra() and updateRanges() required
:param contact_name: Name of the person creating the mzQC file
:param contact_address: Contact address (mail/e-mail or phone) of the person creating the mzQC file
:param description: Description and comments about the mzQC file contents
:param label: Qnique and informative label for the run
:param feature_map: FeatureMap from feature file (featureXML)
:param prot_ids: Protein identifications from ID file (idXML)
:param pep_ids: Protein identifications from ID file (idXML)




