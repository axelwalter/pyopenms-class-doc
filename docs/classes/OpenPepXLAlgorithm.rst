OpenPepXLAlgorithm
==================

.. py:class:: OpenPepXLAlgorithm


   Bases: :py:class:`object`


Cython implementation of _OpenPepXLAlgorithm


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1OpenPepXLAlgorithm.html
 -- Inherits from ['DefaultParamHandler']




.. py:attribute:: OpenPepXLAlgorithm.OpenPepXLAlgorithm_ExitCodes


alias of :py:class:`pyopenms.pyopenms_1.__OpenPepXLAlgorithm_ExitCodes`


.. py:method:: OpenPepXLAlgorithm.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: OpenPepXLAlgorithm.getName


Cython signature: String getName()
Returns the name




.. py:method:: OpenPepXLAlgorithm.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: OpenPepXLAlgorithm.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: OpenPepXLAlgorithm.run


Cython signature: OpenPepXLAlgorithm_ExitCodes run(MSExperiment & unprocessed_spectra, ConsensusMap & cfeatures, libcpp_vector[FASTAEntry] & fasta_db, libcpp_vector[ProteinIdentification] & protein_ids, libcpp_vector[PeptideIdentification] & peptide_ids, OPXL_PreprocessedPairSpectra & preprocessed_pair_spectra, libcpp_vector[libcpp_pair[size_t,size_t]] & spectrum_pairs, libcpp_vector[libcpp_vector[CrossLinkSpectrumMatch]] & all_top_csms, MSExperiment & spectra)


Performs the main function of this class, the search for cross-linked peptides
-----
:param unprocessed_spectra: The input PeakMap of experimental spectra
:param cfeatures: The input cfeatures
:param fasta_db: The protein database containing targets and decoys
:param protein_ids: A result vector containing search settings. Should contain one PeptideIdentification
:param peptide_ids: A result vector containing cross-link spectrum matches as PeptideIdentifications and PeptideHits. Should be empty
:param preprocessed_pair_spectra: A result structure containing linear and cross-linked ion spectra. Will be overwritten. This is only necessary for writing out xQuest type spectrum files
:param spectrum_pairs: A result vector containing paired spectra indices. Should be empty. This is only necessary for writing out xQuest type spectrum files
:param all_top_csms: A result vector containing cross-link spectrum matches as CrossLinkSpectrumMatches. Should be empty. This is only necessary for writing out xQuest type spectrum files
:param spectra: A result vector containing the input spectra after preprocessing and filtering. Should be empty. This is only necessary for writing out xQuest type spectrum files




.. py:method:: OpenPepXLAlgorithm.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: OpenPepXLAlgorithm.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




