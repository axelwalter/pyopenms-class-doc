PeptideAndProteinQuant
======================

.. py:class:: PeptideAndProteinQuant


   Bases: :py:class:`object`


Cython implementation of _PeptideAndProteinQuant


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1PeptideAndProteinQuant.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: PeptideAndProteinQuant.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: PeptideAndProteinQuant.getName


Cython signature: String getName()
Returns the name




.. py:method:: PeptideAndProteinQuant.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: PeptideAndProteinQuant.getStatistics


Cython signature: PeptideAndProteinQuant_Statistics getStatistics()




.. py:method:: PeptideAndProteinQuant.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: PeptideAndProteinQuant.quantifyPeptides


Cython signature: void quantifyPeptides(libcpp_vector[PeptideIdentification] & peptides)


Compute peptide abundances
-----
Based on quantitative data for individual charge states (in member `pep_quant_`), overall abundances for peptides are computed (and stored again in `pep_quant_`)
Quantitative data must first be read via readQuantData()
Optional (peptide-level) protein inference information (e.g. from Fido or ProteinProphet) can be supplied via `peptides`. In that case, peptide-to-protein associations - the basis for protein-level quantification - will also be read from `peptides`!




.. py:method:: PeptideAndProteinQuant.quantifyProteins


Cython signature: void quantifyProteins(ProteinIdentification & proteins)


Compute protein abundances
-----
Peptide abundances must be computed first with quantifyPeptides(). Optional protein inference information (e.g. from Fido or ProteinProphet) can be supplied via `proteins`




.. py:method:: PeptideAndProteinQuant.readQuantData


         - Cython signature: void readQuantData(FeatureMap & map_in, ExperimentalDesign & ed)


Read quantitative data from a feature map
-----
Parameters should be set before using this method, as setting parameters will clear all results
         - Cython signature: void readQuantData(ConsensusMap & map_in, ExperimentalDesign & ed)


Read quantitative data from a consensus map
-----
Parameters should be set before using this method, as setting parameters will clear all results
         - Cython signature: void readQuantData(libcpp_vector[ProteinIdentification] & proteins, libcpp_vector[PeptideIdentification] & peptides, ExperimentalDesign & ed)


Read quantitative data from identification results (for quantification via spectral counting)
-----
Parameters should be set before using this method, as setting parameters will clear all results




.. py:method:: PeptideAndProteinQuant.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: PeptideAndProteinQuant.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




