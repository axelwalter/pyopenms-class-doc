TargetedSpectraExtractor
========================

.. py:class:: TargetedSpectraExtractor


   Bases: :py:class:`object`


Cython implementation of _TargetedSpectraExtractor


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1TargetedSpectraExtractor.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: TargetedSpectraExtractor.annotateSpectra


- Cython signature: void annotateSpectra(libcpp_vector[MSSpectrum] &, TargetedExperiment &, libcpp_vector[MSSpectrum] &, FeatureMap &)
- Cython signature: void annotateSpectra(libcpp_vector[MSSpectrum] &, TargetedExperiment &, libcpp_vector[MSSpectrum] &)
- Cython signature: void annotateSpectra(libcpp_vector[MSSpectrum] &, FeatureMap &, FeatureMap &, libcpp_vector[MSSpectrum] &)




.. py:method:: TargetedSpectraExtractor.extractSpectra


- Cython signature: void extractSpectra(MSExperiment &, TargetedExperiment &, libcpp_vector[MSSpectrum] &, FeatureMap &)
- Cython signature: void extractSpectra(MSExperiment &, TargetedExperiment &, libcpp_vector[MSSpectrum] &)




.. py:method:: TargetedSpectraExtractor.getDefaultParameters


Cython signature: void getDefaultParameters(Param &)




.. py:method:: TargetedSpectraExtractor.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: TargetedSpectraExtractor.getName


Cython signature: String getName()
Returns the name




.. py:method:: TargetedSpectraExtractor.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: TargetedSpectraExtractor.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: TargetedSpectraExtractor.mergeFeatures


Cython signature: void mergeFeatures(FeatureMap &, FeatureMap &)




.. py:method:: TargetedSpectraExtractor.pickSpectrum


Cython signature: void pickSpectrum(MSSpectrum &, MSSpectrum &)




.. py:method:: TargetedSpectraExtractor.scoreSpectra


- Cython signature: void scoreSpectra(libcpp_vector[MSSpectrum] &, libcpp_vector[MSSpectrum] &, FeatureMap &, libcpp_vector[MSSpectrum] &)
- Cython signature: void scoreSpectra(libcpp_vector[MSSpectrum] &, libcpp_vector[MSSpectrum] &, libcpp_vector[MSSpectrum] &)




.. py:method:: TargetedSpectraExtractor.searchSpectrum


Cython signature: void searchSpectrum(FeatureMap &, FeatureMap &)




.. py:method:: TargetedSpectraExtractor.selectSpectra


- Cython signature: void selectSpectra(libcpp_vector[MSSpectrum] &, FeatureMap &, libcpp_vector[MSSpectrum] &, FeatureMap &)
- Cython signature: void selectSpectra(libcpp_vector[MSSpectrum] &, libcpp_vector[MSSpectrum] &)




.. py:method:: TargetedSpectraExtractor.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: TargetedSpectraExtractor.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




.. py:method:: TargetedSpectraExtractor.storeSpectraMSP


Cython signature: void storeSpectraMSP(const String &, MSExperiment &)




.. py:method:: TargetedSpectraExtractor.storeSpectraTraML


Cython signature: void storeSpectraTraML(const String &, FeatureMap &, FeatureMap &)




