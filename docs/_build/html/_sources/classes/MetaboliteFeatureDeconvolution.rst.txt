MetaboliteFeatureDeconvolution
==============================

.. py:class:: MetaboliteFeatureDeconvolution


   Bases: :py:class:`object`


Cython implementation of _MetaboliteFeatureDeconvolution


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MetaboliteFeatureDeconvolution.html
 -- Inherits from ['DefaultParamHandler']




.. py:attribute:: MetaboliteFeatureDeconvolution.CHARGEMODE_MFD


alias of :py:class:`pyopenms.pyopenms_7.__CHARGEMODE_MFD`


.. py:method:: MetaboliteFeatureDeconvolution.compute


Cython signature: void compute(FeatureMap & fm_in, FeatureMap & fm_out, ConsensusMap & cons_map, ConsensusMap & cons_map_p)


Compute a zero-charge feature map from a set of charged features
-----
Find putative ChargePairs, then score them and hand over to ILP
-----
:param fm_in: Input feature-map
:param fm_out: Output feature-map (sorted by position and augmented with user params)
:param cons_map: Output of grouped features belonging to a charge group
:param cons_map_p: Output of paired features connected by an edge




.. py:method:: MetaboliteFeatureDeconvolution.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: MetaboliteFeatureDeconvolution.getName


Cython signature: String getName()
Returns the name




.. py:method:: MetaboliteFeatureDeconvolution.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: MetaboliteFeatureDeconvolution.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: MetaboliteFeatureDeconvolution.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: MetaboliteFeatureDeconvolution.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




