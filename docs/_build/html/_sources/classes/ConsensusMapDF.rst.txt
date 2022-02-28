ConsensusMapDF
==============

.. py:class:: ConsensusMapDF(*args, **kwargs)
   :module: pyopenms.dataframes


   Bases: :py:class:`pyopenms.pyopenms_6.ConsensusMap`




.. py:method:: ConsensusMapDF.get_df()
   :module: pyopenms.dataframes


Generates a pandas DataFrame with both consensus feature meta data and intensities from each sample.


Returns:
pandas.DataFrame: meta data and intensity DataFrame




.. py:method:: ConsensusMapDF.get_intensity_df()
   :module: pyopenms.dataframes


Generates a pandas DataFrame with feature intensities from each sample in long format (over files).


For labelled analyses channel intensities will be in one row, therefore resulting in a semi-long/block format.
Resulting DataFrame can be joined with result from get_metadata_df by their index 'id'.


Returns:
pandas.DataFrame: intensity DataFrame




.. py:method:: ConsensusMapDF.get_metadata_df()
   :module: pyopenms.dataframes


Generates a pandas DataFrame with feature meta data (sequence, charge, mz, RT, quality).


Resulting DataFrame can be joined with result from get_intensity_df by their index 'id'.


Returns:
pandas.DataFrame: DataFrame with metadata for each feature (such as: best identified sequence, charge, centroid RT/mz, fitting quality)




.. py:attribute:: FeatureMap
   :module: pyopenms.dataframes


alias of :py:class:`pyopenms.dataframes.FeatureMapDF`


