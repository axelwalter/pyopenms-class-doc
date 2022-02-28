IsotopeWaveletTransform
=======================

.. py:class:: IsotopeWaveletTransform


   Bases: :py:class:`object`


Cython implementation of _IsotopeWaveletTransform[_Peak1D]


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1IsotopeWaveletTransform[_Peak1D].html




.. py:method:: IsotopeWaveletTransform.computeMinSpacing


Cython signature: void computeMinSpacing(MSSpectrum & c_ref)




.. py:method:: IsotopeWaveletTransform.getLinearInterpolation


Cython signature: double getLinearInterpolation(double mz_a, double intens_a, double mz_pos, double mz_b, double intens_b)


Computes a linear (intensity) interpolation
-----
:param mz_a: The m/z value of the point left to the query
:param intens_a: The intensity value of the point left to the query
:param mz_pos: The query point
:param mz_b: The m/z value of the point right to the query
:param intens_b: The intensity value of the point left to the query




.. py:method:: IsotopeWaveletTransform.getMaxScanSize


Cython signature: size_t getMaxScanSize()




.. py:method:: IsotopeWaveletTransform.getMinSpacing


Cython signature: double getMinSpacing()




.. py:method:: IsotopeWaveletTransform.getSigma


Cython signature: double getSigma()




.. py:method:: IsotopeWaveletTransform.getTransform


Cython signature: void getTransform(MSSpectrum & c_trans, MSSpectrum & c_ref, unsigned int c)


Computes the isotope wavelet transform of charge state `c`
-----
:param c_trans: The transform
:param c_ref: The reference spectrum
:param c: The charge state minus 1 (e.g. c=2 means charge state 3) at which you want to compute the transform




.. py:method:: IsotopeWaveletTransform.getTransformHighRes


Cython signature: void getTransformHighRes(MSSpectrum & c_trans, MSSpectrum & c_ref, unsigned int c)


Computes the isotope wavelet transform of charge state `c`
-----
:param c_trans: The transform
:param c_ref: The reference spectrum
:param c: The charge state minus 1 (e.g. c=2 means charge state 3) at which you want to compute the transform




.. py:method:: IsotopeWaveletTransform.identifyCharge


Cython signature: void identifyCharge(MSSpectrum & candidates, MSSpectrum & ref, unsigned int scan_index, unsigned int c, double ampl_cutoff, bool check_PPMs)


Given an isotope wavelet transformed spectrum 'candidates', this function assigns to every significant
pattern its corresponding charge state and a score indicating the reliability of the prediction. The result of this
process is stored internally. Important: Before calling this function, apply updateRanges() to the original map
-----
:param candidates: A isotope wavelet transformed spectrum. Entry "number i" in this vector must correspond to the
charge-"(i-1)"-transform of its mass signal. (This is exactly the output of the function `getTransforms`.)
:param ref: The reference scan (the untransformed raw data) corresponding to `candidates`
:param c: The corresponding charge state minus 1 (e.g. c=2 means charge state 3)
:param scan_index: The index of the scan (w.r.t. to some map) currently under consideration
:param ampl_cutoff: The thresholding parameter. This parameter is the only (and hence a really important)
parameter of the isotope wavelet transform. On the basis of `ampl_cutoff` the program tries to distinguish between
noise and signal. Please note that it is not a "simple" hard thresholding parameter in the sense of drawing a virtual
line in the spectrum, which is then used as a guillotine cut. Maybe you should play around a bit with this parameter to
get a feeling about its range. For peptide mass fingerprints on small data sets (like single MALDI-scans e.g.), it
makes sense to start `ampl_cutoff=0` or even `ampl_cutoff=-1`,
indicating no thresholding at all. Note that also ampl_cutoff=0 triggers (a moderate) thresholding based on the
average intensity in the wavelet transform
:param check_PPMs: If enabled, the algorithm will check each monoisotopic mass candidate for its plausibility
by computing the ppm difference between this mass and the averagine model




.. py:method:: IsotopeWaveletTransform.initializeScan


Cython signature: void initializeScan(MSSpectrum & c_ref, unsigned int c)




.. py:method:: IsotopeWaveletTransform.mapSeeds2Features


Cython signature: FeatureMap mapSeeds2Features(MSExperiment & map_, unsigned int RT_votes_cutoff)


Filters the candidates further more and maps the internally used data structures to the OpenMS framework
-----
:param map: The original map containing the data set to be analyzed
:param max_charge: The maximal charge state under consideration
:param RT_votes_cutoff: See the IsotopeWaveletFF class




.. py:method:: IsotopeWaveletTransform.setSigma


Cython signature: void setSigma(double sigma)




.. py:method:: IsotopeWaveletTransform.updateBoxStates


Cython signature: void updateBoxStates(MSExperiment & map_, size_t scan_index, unsigned int RT_interleave, unsigned int RT_votes_cutoff, int front_bound, int end_bound)


A function keeping track of currently open and closed sweep line boxes
This function is used by the isotope wavelet feature finder and must be called for each processed scan
-----
:param map: The original map containing the data set to be analyzed
:param scan_index: The index of the scan currently under consideration w.r.t. its MS map
This information is necessary to sweep across the map after each scan has been evaluated
:param RT_votes_cutoff: See the IsotopeWaveletFF class




