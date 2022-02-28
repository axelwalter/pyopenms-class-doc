FeatureMapDF
============

.. py:class:: FeatureMapDF(*args, **kwargs)
   :module: pyopenms.dataframes


   Bases: :py:class:`pyopenms.pyopenms_3.FeatureMap`




.. py:method:: FeatureMapDF.get_assigned_peptide_identifications()
   :module: pyopenms.dataframes


Generates a list with peptide identifications assigned to a feature.


Adds 'ID_native_id' (feature spectrum id), 'ID_filename' (primary MS run path of corresponding ProteinIdentification)
and 'feature_id' (unique ID of corresponding Feature) as meta values to the peptide hits.
A DataFrame from the assigned peptides generated with peptide_identifications_to_df(assigned_peptides) can be
merged with the FeatureMap DataFrame with:
merged_df = pd.merge(feature_df, assigned_peptide_df, on=['feature_id', 'ID_native_id', 'ID_filename'])


Returns:
[PeptideIdentification]: list of PeptideIdentification objects




.. py:method:: FeatureMapDF.get_df(meta_values=None, export_peptide_identifications=True)
   :module: pyopenms.dataframes


Generates a pandas DataFrame with information contained in the FeatureMap.


Optionally the feature meta values and information for the assigned PeptideHit can be exported.


Parameters:
meta_values: meta values to include (None, [custom list of meta value names] or 'all')


export_peptide_identifications (bool): export sequence and score for best PeptideHit assigned to a feature.
Additionally the ID_filename (file name of the corresponding ProteinIdentification) and the ID_native_id
(spectrum ID of the corresponding Feature) are exported. They are also annotated as meta values when
collecting all assigned PeptideIdentifications from a FeatureMap with FeatureMap.get_assigned_peptide_identifications().
A DataFrame from the assigned peptides generated with peptide_identifications_to_df(assigned_peptides) can be
merged with the FeatureMap DataFrame with:
merged_df = pd.merge(feature_df, assigned_peptide_df, on=['feature_id', 'ID_native_id', 'ID_filename'])


Returns:
pandas.DataFrame: feature information stored in a DataFrame




.. py:attribute:: MSExperiment
   :module: pyopenms.dataframes


alias of :py:class:`pyopenms.dataframes.MSExperimentDF`


