MRMMapping
==========

.. py:class:: MRMMapping


   Bases: :py:class:`object`


Cython implementation of _MRMMapping


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MRMMapping.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: MRMMapping.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: MRMMapping.getName


Cython signature: String getName()
Returns the name




.. py:method:: MRMMapping.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: MRMMapping.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: MRMMapping.mapExperiment


Cython signature: void mapExperiment(MSExperiment input_chromatograms, TargetedExperiment targeted_exp, MSExperiment & output)


Maps input chromatograms to assays in a targeted experiment
-----
The output chromatograms are an annotated copy of the input chromatograms
with native id, precursor information and peptide sequence (if available)
annotated in the chromatogram files
-----
The algorithm tries to match a given set of chromatograms and targeted
assays. It iterates through all the chromatograms retrieves one or more
matching targeted assay for the chromatogram. By default, the algorithm
assumes that a 1:1 mapping exists. If a chromatogram cannot be mapped
(does not have a corresponding assay) the algorithm issues a warning, the
user can specify that the program should abort in such a case (see
error_on_unmapped)
-----
:note If multiple mapping is enabled (see map_multiple_assays parameter)
then each mapped assay will get its own chromatogram that contains the
same raw data but different meta-annotation. This *can* be useful if the
same transition is used to monitor multiple analytes but may also
indicate a problem with too wide mapping tolerances




.. py:method:: MRMMapping.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: MRMMapping.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




