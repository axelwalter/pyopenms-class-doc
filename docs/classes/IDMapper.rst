IDMapper
========

.. py:class:: IDMapper


   Bases: :py:class:`object`


Cython implementation of _IDMapper


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1IDMapper.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: IDMapper.annotate


         - Cython signature: void annotate(MSExperiment & map_, libcpp_vector[PeptideIdentification] & ids, libcpp_vector[ProteinIdentification] & protein_ids, bool clear_ids, bool mapMS1)


Mapping method for peak maps
-----
The identifications stored in a PeptideIdentification instance can be added to the
corresponding spectrum
Note that a PeptideIdentication is added to ALL spectra which are within the allowed RT and MZ boundaries
-----
:param map: MSExperiment to receive the identifications
:param peptide_ids: PeptideIdentification for the MSExperiment
:param protein_ids: ProteinIdentification for the MSExperiment
:param clear_ids: Reset peptide and protein identifications of each scan before annotating
:param map_ms1: Attach Ids to MS1 spectra using RT mapping only (without precursor, without m/z)
:raises:
  Exception: MissingInformation is thrown if entries of 'peptide_ids' do not contain 'MZ' and 'RT' information
         - Cython signature: void annotate(MSExperiment & map_, FeatureMap & fmap, bool clear_ids, bool mapMS1)


Mapping method for peak maps
-----
Add peptide identifications stored in a feature map to their
corresponding spectrum
This function converts the feature map to a vector of peptide identifications (all peptide IDs from each feature are taken)
and calls the respective annotate() function
RT and m/z are taken from the peptides, or (if missing) from the feature itself
-----
:param map: MSExperiment to receive the identifications
:param fmap: FeatureMap with PeptideIdentifications for the MSExperiment
:param clear_ids: Reset peptide and protein identifications of each scan before annotating
:param map_ms1: Attach Ids to MS1 spectra using RT mapping only (without precursor, without m/z)
         - Cython signature: void annotate(FeatureMap & map_, libcpp_vector[PeptideIdentification] & ids, libcpp_vector[ProteinIdentification] & protein_ids, bool use_centroid_rt, bool use_centroid_mz, MSExperiment & spectra)


Mapping method for peak maps
-----
If all features have at least one convex hull, peptide positions are matched against the bounding boxes of the convex hulls by default. If not, the positions of the feature centroids are used. The respective coordinates of the centroids are also used for matching (in place of the corresponding ranges from the bounding boxes) if 'use_centroid_rt' or 'use_centroid_mz' are true
-----
In any case, tolerance in RT and m/z dimension is applied according to the global parameters 'rt_tolerance' and 'mz_tolerance'. Tolerance is understood as "plus or minus x", so the matching range is actually increased by twice the tolerance value
-----
If several features (incl. tolerance) overlap the position of a peptide identification, the identification is annotated to all of them
-----
:param map: MSExperiment to receive the identifications
:param ids: PeptideIdentification for the MSExperiment
:param protein_ids: ProteinIdentification for the MSExperiment
:param use_centroid_rt: Whether to use the RT value of feature centroids even if convex hulls are present
:param use_centroid_mz: Whether to use the m/z value of feature centroids even if convex hulls are present
:param spectra: Whether precursors not contained in the identifications are annotated with an empty PeptideIdentification object containing the scan index
:raises:
  Exception: MissingInformation is thrown if entries of 'ids' do not contain 'MZ' and 'RT' information
         - Cython signature: void annotate(ConsensusMap & map_, libcpp_vector[PeptideIdentification] & ids, libcpp_vector[ProteinIdentification] & protein_ids, bool measure_from_subelements, bool annotate_ids_with_subelements, MSExperiment & spectra)


Mapping method for peak maps
-----
If all features have at least one convex hull, peptide positions are matched against the bounding boxes of the convex hulls by default. If not, the positions of the feature centroids are used. The respective coordinates of the centroids are also used for matching (in place of the corresponding ranges from the bounding boxes) if 'use_centroid_rt' or 'use_centroid_mz' are true
-----
In any case, tolerance in RT and m/z dimension is applied according to the global parameters 'rt_tolerance' and 'mz_tolerance'. Tolerance is understood as "plus or minus x", so the matching range is actually increased by twice the tolerance value
-----
If several features (incl. tolerance) overlap the position of a peptide identification, the identification is annotated to all of them
-----
:param map: MSExperiment to receive the identifications
:param ids: PeptideIdentification for the MSExperiment
:param protein_ids: ProteinIdentification for the MSExperiment
:param measure_from_subelements: Boolean operator set to true if distance estimate from FeatureHandles instead of Centroid
:param annotate_ids_with_subelements: Boolean operator set to true if store map index of FeatureHandle in peptide identification
:param spectra: Whether precursors not contained in the identifications are annotated with an empty PeptideIdentification object containing the scan index
:raises:
  Exception: MissingInformation is thrown if entries of 'ids' do not contain 'MZ' and 'RT' information




.. py:method:: IDMapper.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: IDMapper.getName


Cython signature: String getName()
Returns the name




.. py:method:: IDMapper.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: IDMapper.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: IDMapper.mapPrecursorsToIdentifications


Cython signature: IDMapper_SpectraIdentificationState mapPrecursorsToIdentifications(MSExperiment spectra, libcpp_vector[PeptideIdentification] & ids, double mz_tol, double rt_tol)


Mapping of peptide identifications to spectra
This helper function partitions all spectra into those that had:
- no precursor (e.g. MS1 spectra),
- at least one identified precursor,
- or only unidentified precursor
-----
:param spectra: The mass spectra
:param ids: The peptide identifications
:param mz_tol: Tolerance used to map to precursor m/z
:param rt_tol: Tolerance used to map to spectrum retention time
:returns: A struct of vectors holding spectra indices of the partitioning




.. py:method:: IDMapper.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: IDMapper.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




