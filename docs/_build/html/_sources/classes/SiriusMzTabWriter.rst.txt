SiriusMzTabWriter
=================

.. py:class:: SiriusMzTabWriter


   Bases: :py:class:`object`


Cython implementation of _SiriusMzTabWriter


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1SiriusMzTabWriter.html




.. py:method:: SiriusMzTabWriter.extractFeatureId


Cython signature: String extractFeatureId(const String & path)




.. py:method:: SiriusMzTabWriter.extractScanIndex


Cython signature: int extractScanIndex(const String & path)




.. py:method:: SiriusMzTabWriter.extractScanNumber


Cython signature: int extractScanNumber(const String & path)




.. py:method:: SiriusMzTabWriter.extractSpectrumMSInfo


Cython signature: SiriusMzTabWriter_SiriusSpectrumMSInfo extractSpectrumMSInfo(const String & single_sirius_path)




.. py:method:: SiriusMzTabWriter.extract_columnname_to_columnindex


Cython signature: libcpp_map[libcpp_string,size_t] extract_columnname_to_columnindex(CsvFile & csvfile)




.. py:method:: SiriusMzTabWriter.read


Cython signature: void read(libcpp_vector[String] & sirius_output_paths, const String & original_input_mzml, size_t top_n_hits, MzTab & result)




