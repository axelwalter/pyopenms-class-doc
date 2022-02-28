OpenPepXLLFAlgorithm
====================

.. py:class:: OpenPepXLLFAlgorithm


   Bases: :py:class:`object`


Cython implementation of _OpenPepXLLFAlgorithm


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1OpenPepXLLFAlgorithm.html
 -- Inherits from ['DefaultParamHandler']




.. py:attribute:: OpenPepXLLFAlgorithm.OpenPepXLLFAlgorithm_ExitCodes


alias of :py:class:`pyopenms.pyopenms_3.__OpenPepXLLFAlgorithm_ExitCodes`


.. py:method:: OpenPepXLLFAlgorithm.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: OpenPepXLLFAlgorithm.getName


Cython signature: String getName()
Returns the name




.. py:method:: OpenPepXLLFAlgorithm.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: OpenPepXLLFAlgorithm.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: OpenPepXLLFAlgorithm.run


Cython signature: OpenPepXLLFAlgorithm_ExitCodes run(MSExperiment & unprocessed_spectra, libcpp_vector[FASTAEntry] & fasta_db, libcpp_vector[ProteinIdentification] & protein_ids, libcpp_vector[PeptideIdentification] & peptide_ids, libcpp_vector[libcpp_vector[CrossLinkSpectrumMatch]] & all_top_csms, MSExperiment & spectra)


Performs the main function of this class, the search for cross-linked peptides
-----
:param unprocessed_spectra: The input PeakMap of experimental spectra
:param fasta_db: The protein database containing targets and decoys
:param protein_ids: A result vector containing search settings. Should contain one PeptideIdentification
:param peptide_ids: A result vector containing cross-link spectrum matches as PeptideIdentifications and PeptideHits. Should be empty
:param all_top_csms: A result vector containing cross-link spectrum matches as CrossLinkSpectrumMatches. Should be empty. This is only necessary for writing out xQuest type spectrum files
:param spectra: A result vector containing the input spectra after preprocessing and filtering. Should be empty. This is only necessary for writing out xQuest type spectrum files




.. py:method:: OpenPepXLLFAlgorithm.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: OpenPepXLLFAlgorithm.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




