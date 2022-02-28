TheoreticalSpectrumGenerator
============================

.. py:class:: TheoreticalSpectrumGenerator


   Bases: :py:class:`object`


Cython implementation of _TheoreticalSpectrumGenerator


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1TheoreticalSpectrumGenerator.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: TheoreticalSpectrumGenerator.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: TheoreticalSpectrumGenerator.getName


Cython signature: String getName()
Returns the name




.. py:method:: TheoreticalSpectrumGenerator.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: TheoreticalSpectrumGenerator.getSpectrum


Cython signature: void getSpectrum(MSSpectrum & spec, AASequence & peptide, int min_charge, int max_charge)
Generates a spectrum for a peptide sequence, with the ion types that are set in the tool parameters. If precursor_charge is set to 0 max_charge + 1 will be used




.. py:method:: TheoreticalSpectrumGenerator.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: TheoreticalSpectrumGenerator.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: TheoreticalSpectrumGenerator.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




