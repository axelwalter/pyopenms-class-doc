MSExperimentDF
==============

.. py:class:: MSExperimentDF(*args, **kwargs)
   :module: pyopenms.dataframes


   Bases: :py:class:`pyopenms.pyopenms_1.MSExperiment`




.. py:method:: MSExperimentDF.get_df(long: bool = False)
   :module: pyopenms.dataframes


Generates a pandas DataFrame with all peaks in the MSExperiment


Parameters:
long: set to True if you want to have a long/expanded/melted dataframe with one row per peak. Faster but
    replicated RT information. If False, returns rows in the style: rt, np.array(mz), np.array(int)


Returns:
pandas.DataFrame: feature information stored in a DataFrame




.. py:method:: MSExperimentDF.get_massql_df()
   :module: pyopenms.dataframes


Exports data from MSExperiment to pandas DataFrames to be used with MassQL.


The Python module massql allows queries in mass spectrometry data (MS1 and MS2
data frames) in a SQL like fashion (https://github.com/mwang87/MassQueryLanguage).


Both dataframes contain the columns:
'i': intensity of a peak
'i_norm': intensity normalized by the maximun intensity in the spectrum
'i_tic_norm': intensity normalized by the sum of intensities (TIC) in the spectrum
'mz': mass to charge of a peak
'scan': number of the spectrum
'rt': retention time of the spectrum
'polarity': ion mode of the spectrum as integer value (positive: 1, negative: 2)


The MS2 dataframe contains additional columns:
'precmz': mass to charge of the precursor ion
'ms1scan': number of the corresponding MS1 spectrum
'charge': charge of the precursor ion


Returns:
ms1_df (pandas.DataFrame): peak data of MS1 spectra
ms2_df (pandas.DataFrame): peak data of MS2 spectra with precursor information




.. py:attribute:: PeakMap
   :module: pyopenms.dataframes


alias of :py:class:`pyopenms.dataframes.MSExperimentDF`


.. py:function:: peptide_identifications_to_df(peps: List[pyopenms.pyopenms_3.PeptideIdentification], decode_ontology: bool = True, default_missing_values: dict = {<class 'bool'>: False, <class 'int'>: -9999, <class 'float'>: nan, <class 'str'>: ''}, export_unidentified: bool = True)
   :module: pyopenms.dataframes


Converts a list of peptide identifications to a pandas DataFrame.
Parameters:
peps (List[PeptideIdentification]): list of PeptideIdentification objects
decode_ontology (bool): decode meta value names
default_missing_values: default value for missing values for each data type
export_unidentified: export PeptideIdentifications without PeptideHit
Returns:
pandas.DataFrame: peptide identifications in a DataFrame




.. py:module:: pyopenms.pyopenms_1




