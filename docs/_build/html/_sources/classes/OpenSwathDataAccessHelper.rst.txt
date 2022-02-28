OpenSwathDataAccessHelper
=========================

.. py:class:: OpenSwathDataAccessHelper


   Bases: :py:class:`object`


Cython implementation of _OpenSwathDataAccessHelper


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1OpenSwathDataAccessHelper.html




.. py:method:: OpenSwathDataAccessHelper.convertPeptideToAASequence


Cython signature: void convertPeptideToAASequence(LightCompound & peptide, AASequence & aa_sequence)
Converts from the LightCompound to an OpenMS AASequence (with correct modifications)




.. py:method:: OpenSwathDataAccessHelper.convertTargetedCompound


Cython signature: void convertTargetedCompound(Peptide pep, LightCompound & p)
Converts from the OpenMS TargetedExperiment Peptide to the LightTargetedExperiment Peptide




.. py:method:: OpenSwathDataAccessHelper.convertTargetedExp


Cython signature: void convertTargetedExp(TargetedExperiment & transition_exp_, LightTargetedExperiment & transition_exp)
Converts from the OpenMS TargetedExperiment to the OpenMs LightTargetedExperiment




.. py:method:: OpenSwathDataAccessHelper.convertToChromatogramPtr




.. py:method:: OpenSwathDataAccessHelper.convertToOpenMSChromatogram


Cython signature: void convertToOpenMSChromatogram(shared_ptr[OSChromatogram] cptr, MSChromatogram & chromatogram)
Converts a ChromatogramPtr to an OpenMS Chromatogram




.. py:method:: OpenSwathDataAccessHelper.convertToOpenMSChromatogramFilter


Cython signature: void convertToOpenMSChromatogramFilter(MSChromatogram & chromatogram, shared_ptr[OSChromatogram] cptr, double rt_min, double rt_max)




.. py:method:: OpenSwathDataAccessHelper.convertToOpenMSSpectrum


Cython signature: void convertToOpenMSSpectrum(shared_ptr[OSSpectrum] sptr, MSSpectrum & spectrum)
Converts a SpectrumPtr to an OpenMS Spectrum




.. py:method:: OpenSwathDataAccessHelper.convertToSpectrumPtr




