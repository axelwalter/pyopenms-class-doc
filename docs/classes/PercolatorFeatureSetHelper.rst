PercolatorFeatureSetHelper
==========================

.. py:class:: PercolatorFeatureSetHelper


   Bases: :py:class:`object`


Cython implementation of _PercolatorFeatureSetHelper


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1PercolatorFeatureSetHelper.html


 Percolator feature set and integration helper
 -----
 This class contains functions to handle (compute, aggregate, integrate)
 Percolator features. This includes the calculation or extraction of
 Percolator features depending on the search engine(s) for later use with
 PercolatorAdapter. It also includes handling the reintegration of the
 percolator result into the set of Identifications




.. py:method:: PercolatorFeatureSetHelper.addCOMETFeatures


Cython signature: void addCOMETFeatures(libcpp_vector[PeptideIdentification] & peptide_ids, StringList & feature_set)


Creates and adds Comet specific Percolator features and registers them in feature_set
-----
:param peptide_ids: PeptideIdentification vector to create Percolator features in
:param feature_set: Register of added features




.. py:method:: PercolatorFeatureSetHelper.addCONCATSEFeatures


Cython signature: void addCONCATSEFeatures(libcpp_vector[PeptideIdentification] & peptide_id_list, StringList & search_engines_used, StringList & feature_set)


Adds multiple search engine specific Percolator features and registers them in feature_set
-----
This struct can be used to store both peak or feature indices
:param peptide_ids: PeptideIdentification vector to create Percolator features in
:param search_engines_used: The list of search engines to be considered
:param feature_set: Register of added features




.. py:method:: PercolatorFeatureSetHelper.addMASCOTFeatures


Cython signature: void addMASCOTFeatures(libcpp_vector[PeptideIdentification] & peptide_ids, StringList & feature_set)


Creates and adds Mascot specific Percolator features and registers them in feature_set
-----
:param peptide_ids: PeptideIdentification vector to create Percolator features in
:param feature_set: Register of added features




.. py:method:: PercolatorFeatureSetHelper.addMSGFFeatures


Cython signature: void addMSGFFeatures(libcpp_vector[PeptideIdentification] & peptide_ids, StringList & feature_set)


Creates and adds MSGF+ specific Percolator features and registers them in feature_set. MSGF+ should be run with the addFeatures flag enabled
-----
:param peptide_ids: PeptideIdentification vector to create Percolator features in
:param feature_set: Register of added features




.. py:method:: PercolatorFeatureSetHelper.addMULTISEFeatures


Cython signature: void addMULTISEFeatures(libcpp_vector[PeptideIdentification] & peptide_ids, StringList & search_engines_used, StringList & feature_set, bool complete_only, bool limits_imputation)


Adds multiple search engine specific Percolator features and registers them in feature_set
-----
:param peptide_ids: PeptideIdentification vector to create Percolator features in
:param search_engines_used: The list of search engines to be considered
:param feature_set: Register of added features
:param complete_only: Will only add features for PeptideIdentifications where all given search engines identified something
:param limits_imputation




.. py:method:: PercolatorFeatureSetHelper.addXTANDEMFeatures


Cython signature: void addXTANDEMFeatures(libcpp_vector[PeptideIdentification] & peptide_ids, StringList & feature_set)


Creates and adds X!Tandem specific Percolator features and registers them in feature_set
-----
:param peptide_ids: PeptideIdentification vector to create Percolator features in
:param feature_set: Register of added features




.. py:method:: PercolatorFeatureSetHelper.checkExtraFeatures


Cython signature: void checkExtraFeatures(libcpp_vector[PeptideHit] & psms, StringList & extra_features)


Checks and removes requested extra Percolator features that are actually unavailable (to compute)
-----
:param psms: The vector of PeptideHit to be checked
:param extra_features: The list of requested extra features




.. py:method:: PercolatorFeatureSetHelper.concatMULTISEPeptideIds


Cython signature: void concatMULTISEPeptideIds(libcpp_vector[PeptideIdentification] & all_peptide_ids, libcpp_vector[PeptideIdentification] & new_peptide_ids, String search_engine)


Appends a vector of PeptideIdentification to another and prepares Percolator features in MetaInfo (With the respective key "CONCAT:" + search_engine)
-----
:param all_peptide_ids: PeptideIdentification vector to append to
:param new_peptide_ids: PeptideIdentification vector to be appended
:param search_engine: Search engine to depend on for feature creation




.. py:method:: PercolatorFeatureSetHelper.mergeMULTISEPeptideIds


Cython signature: void mergeMULTISEPeptideIds(libcpp_vector[PeptideIdentification] & all_peptide_ids, libcpp_vector[PeptideIdentification] & new_peptide_ids, String search_engine)


Merges a vector of PeptideIdentification into another and prepares the merged MetaInfo and scores for collection in addMULTISEFeatures for feature registration
-----
:param all_peptide_idsL: PeptideIdentification vector to be merged into
:param new_peptide_idsL: PeptideIdentification vector to merge
:param search_engineL: Search engine to create features from their scores




.. py:method:: PercolatorFeatureSetHelper.mergeMULTISEProteinIds


Cython signature: void mergeMULTISEProteinIds(libcpp_vector[ProteinIdentification] & all_protein_ids, libcpp_vector[ProteinIdentification] & new_protein_ids)


Concatenates SearchParameter of multiple search engine runs and merges PeptideEvidences, collects used search engines in MetaInfo for collection in addMULTISEFeatures for feature registration
-----
:param all_protein_ids: ProteinIdentification vector to be merged into
:param new_protein_ids: ProteinIdentification vector to merge




