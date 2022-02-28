DIAScoring
==========

.. py:class:: DIAScoring


   Bases: :py:class:`object`


Cython implementation of _DIAScoring


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1DIAScoring.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: DIAScoring.dia_by_ion_score




.. py:method:: DIAScoring.dia_ms1_isotope_scores


Cython signature: void dia_ms1_isotope_scores(double precursor_mz, shared_ptr[OSSpectrum] spectrum, double & isotope_corr, double & isotope_overlap, EmpiricalFormula & sum_formula)




.. py:method:: DIAScoring.dia_ms1_isotope_scores_averagine


Cython signature: void dia_ms1_isotope_scores_averagine(double precursor_mz, shared_ptr[OSSpectrum] spectrum, double & isotope_corr, double & isotope_overlap, int charge_state)




.. py:method:: DIAScoring.dia_ms1_massdiff_score


Cython signature: bool dia_ms1_massdiff_score(double precursor_mz, shared_ptr[OSSpectrum] spectrum, double & ppm_score)




.. py:method:: DIAScoring.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: DIAScoring.getName


Cython signature: String getName()
Returns the name




.. py:method:: DIAScoring.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: DIAScoring.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: DIAScoring.score_with_isotopes


Cython signature: void score_with_isotopes(shared_ptr[OSSpectrum] spectrum, libcpp_vector[LightTransition] transitions, double & dotprod, double & manhattan)




.. py:method:: DIAScoring.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: DIAScoring.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




