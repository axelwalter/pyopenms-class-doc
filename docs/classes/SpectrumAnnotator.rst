SpectrumAnnotator
=================

.. py:class:: SpectrumAnnotator


   Bases: :py:class:`object`


Cython implementation of _SpectrumAnnotator


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1SpectrumAnnotator.html
 -- Inherits from ['DefaultParamHandler']




.. py:method:: SpectrumAnnotator.addIonMatchStatistics


Cython signature: void addIonMatchStatistics(PeptideIdentification & pi, MSSpectrum & spec, TheoreticalSpectrumGenerator & tg, SpectrumAlignment & sa)


Adds ion match statistics to `pi` PeptideIdentifcation
-----
:param pi: A spectrum identifications to be annotated, looking up matches from a spectrum and the theoretical spectrum inferred from the identifications sequence
:param spec: A PeakSpectrum containing the peaks from which the `pi` identifications are made
:param tg: A TheoreticalSpectrumGenerator to infer the theoretical spectrum. Its own parameters define which ion types are referred
:param sa: A SpectrumAlignment to match the theoretical spectrum with the measured. Its own parameters define the match tolerance




.. py:method:: SpectrumAnnotator.annotateMatches


Cython signature: void annotateMatches(MSSpectrum & spec, PeptideHit & ph, TheoreticalSpectrumGenerator & tg, SpectrumAlignment & sa)


Adds ion match annotation to the `spec` input spectrum
-----
:param spec: A PeakSpectrum containing the peaks from which the `pi` identifications are made
:param ph: A spectrum identifications to be used for the annotation, looking up matches from a spectrum and the theoretical spectrum inferred from the identifications sequence
:param tg: A TheoreticalSpectrumGenerator to infer the theoretical spectrum. Its own parameters define which ion types are referred
:param sa: A SpectrumAlignment to match the theoretical spectrum with the measured. Its own parameters define the match tolerance




.. py:method:: SpectrumAnnotator.getDefaults


Cython signature: Param getDefaults()
Returns the default parameters




.. py:method:: SpectrumAnnotator.getName


Cython signature: String getName()
Returns the name




.. py:method:: SpectrumAnnotator.getParameters


Cython signature: Param getParameters()
Returns the parameters




.. py:method:: SpectrumAnnotator.getSubsections


Cython signature: libcpp_vector[String] getSubsections()




.. py:method:: SpectrumAnnotator.setName


Cython signature: void setName(const String &)
Sets the name




.. py:method:: SpectrumAnnotator.setParameters


Cython signature: void setParameters(Param & param)
Sets the parameters




