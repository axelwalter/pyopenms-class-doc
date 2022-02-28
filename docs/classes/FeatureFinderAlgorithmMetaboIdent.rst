FeatureFinderAlgorithmMetaboIdent
=================================

.. py:class:: FeatureFinderAlgorithmMetaboIdent


   Bases: :py:class:`object`


Cython implementation of _FeatureFinderAlgorithmMetaboIdent


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1FeatureFinderAlgorithmMetaboIdent.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: FeatureFinderAlgorithmMetaboIdent.getChromatograms


Cython signature: MSExperiment & getChromatograms()
Retrieves chromatograms (empty if run was not executed)




.. py:method:: FeatureFinderAlgorithmMetaboIdent.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: FeatureFinderAlgorithmMetaboIdent.getLibrary


Cython signature: const TargetedExperiment & getLibrary()
Retrieves the assay library (e.g., to store as TraML, empty if run was not executed)




.. py:method:: FeatureFinderAlgorithmMetaboIdent.getMSData


Cython signature: const MSExperiment & getMSData()
Returns spectra




.. py:method:: FeatureFinderAlgorithmMetaboIdent.getNShared


Cython signature: size_t getNShared()
Retrieves number of features with shared identifications




.. py:method:: FeatureFinderAlgorithmMetaboIdent.getName


Cython signature: String getName()
Returns the name




.. py:method:: FeatureFinderAlgorithmMetaboIdent.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: FeatureFinderAlgorithmMetaboIdent.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: FeatureFinderAlgorithmMetaboIdent.getTransformations


Cython signature: const TransformationDescription & getTransformations()
Retrieves deviations between provided coordinates and extacted ones (e.g., to store as TrafoXML or for plotting)




.. py:method:: FeatureFinderAlgorithmMetaboIdent.run


Cython signature: void run(const libcpp_vector[FeatureFinderMetaboIdentCompound] metaboIdentTable, FeatureMap & features, String spectra_path)


Run feature extraction. spectra_path get's annotated as primaryMSRunPath in the resulting feature map.




.. py:method:: FeatureFinderAlgorithmMetaboIdent.setMSData


Cython signature: void setMSData(MSExperiment & input)
Sets spectra




.. py:method:: FeatureFinderAlgorithmMetaboIdent.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: FeatureFinderAlgorithmMetaboIdent.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




