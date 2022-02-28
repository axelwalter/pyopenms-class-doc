OPXLHelper
==========

.. py:class:: OPXLHelper


   Bases: :py:class:`object`


Cython implementation of _OPXLHelper


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1OPXLHelper.html




.. py:method:: OPXLHelper.addBetaAccessions


Cython signature: void addBetaAccessions(libcpp_vector[PeptideIdentification] & peptide_ids)




.. py:method:: OPXLHelper.addPercolatorFeatureList


Cython signature: void addPercolatorFeatureList(ProteinIdentification & prot_id)




.. py:method:: OPXLHelper.addProteinPositionMetaValues


Cython signature: void addProteinPositionMetaValues(libcpp_vector[PeptideIdentification] & peptide_ids)




.. py:method:: OPXLHelper.addXLTargetDecoyMV


Cython signature: void addXLTargetDecoyMV(libcpp_vector[PeptideIdentification] & peptide_ids)




.. py:method:: OPXLHelper.buildCandidates


Cython signature: libcpp_vector[ProteinProteinCrossLink] buildCandidates(libcpp_vector[XLPrecursor] & candidates, libcpp_vector[int] & precursor_corrections, libcpp_vector[int] & precursor_correction_positions, libcpp_vector[AASeqWithMass] & peptide_masses, const StringList & cross_link_residue1, const StringList & cross_link_residue2, double cross_link_mass, DoubleList cross_link_mass_mono_link, libcpp_vector[double] & spectrum_precursor_vector, libcpp_vector[double] & allowed_error_vector, String cross_link_name)




.. py:method:: OPXLHelper.buildFragmentAnnotations


Cython signature: void buildFragmentAnnotations(libcpp_vector[PeptideHit_PeakAnnotation] & frag_annotations, libcpp_vector[libcpp_pair[size_t,size_t]] matching, MSSpectrum theoretical_spectrum, MSSpectrum experiment_spectrum)




.. py:method:: OPXLHelper.buildPeptideIDs


Cython signature: void buildPeptideIDs(libcpp_vector[PeptideIdentification] & peptide_ids, libcpp_vector[CrossLinkSpectrumMatch] top_csms_spectrum, libcpp_vector[libcpp_vector[CrossLinkSpectrumMatch]] & all_top_csms, size_t all_top_csms_current_index, MSExperiment spectra, size_t scan_index, size_t scan_index_heavy)




.. py:method:: OPXLHelper.collectPrecursorCandidates


Cython signature: libcpp_vector[ProteinProteinCrossLink] collectPrecursorCandidates(IntList precursor_correction_steps, double precursor_mass, double precursor_mass_tolerance, bool precursor_mass_tolerance_unit_ppm, libcpp_vector[AASeqWithMass] filtered_peptide_masses, double cross_link_mass, DoubleList cross_link_mass_mono_link, StringList cross_link_residue1, StringList cross_link_residue2, String cross_link_name, bool use_sequence_tags, const libcpp_vector[libcpp_utf8_string] & tags)




.. py:method:: OPXLHelper.combineTopRanksFromPairs


Cython signature: libcpp_vector[PeptideIdentification] combineTopRanksFromPairs(libcpp_vector[PeptideIdentification] & peptide_ids, size_t number_top_hits)




.. py:method:: OPXLHelper.computeDeltaScores


Cython signature: void computeDeltaScores(libcpp_vector[PeptideIdentification] & peptide_ids)




.. py:method:: OPXLHelper.computePrecursorError


Cython signature: double computePrecursorError(CrossLinkSpectrumMatch csm, double precursor_mz, int precursor_charge)




.. py:method:: OPXLHelper.digestDatabase


Cython signature: libcpp_vector[AASeqWithMass] digestDatabase(libcpp_vector[FASTAEntry] fasta_db, EnzymaticDigestion digestor, size_t min_peptide_length, StringList cross_link_residue1, StringList cross_link_residue2, ModifiedPeptideGenerator_MapToResidueType & fixed_modifications, ModifiedPeptideGenerator_MapToResidueType & variable_modifications, size_t max_variable_mods_per_peptide)




.. py:method:: OPXLHelper.enumerateCrossLinksAndMasses


Cython signature: libcpp_vector[XLPrecursor] enumerateCrossLinksAndMasses(libcpp_vector[AASeqWithMass] peptides, double cross_link_mass_light, DoubleList cross_link_mass_mono_link, StringList cross_link_residue1, StringList cross_link_residue2, libcpp_vector[double] & spectrum_precursors, libcpp_vector[int] & precursor_correction_positions, double precursor_mass_tolerance, bool precursor_mass_tolerance_unit_ppm)




.. py:method:: OPXLHelper.isoPeakMeans


Cython signature: void isoPeakMeans(CrossLinkSpectrumMatch & csm, IntegerDataArray & num_iso_peaks_array, libcpp_vector[libcpp_pair[size_t,size_t]] & matched_spec_linear_alpha, libcpp_vector[libcpp_pair[size_t,size_t]] & matched_spec_linear_beta, libcpp_vector[libcpp_pair[size_t,size_t]] & matched_spec_xlinks_alpha, libcpp_vector[libcpp_pair[size_t,size_t]] & matched_spec_xlinks_beta)




.. py:method:: OPXLHelper.removeBetaPeptideHits


Cython signature: void removeBetaPeptideHits(libcpp_vector[PeptideIdentification] & peptide_ids)




