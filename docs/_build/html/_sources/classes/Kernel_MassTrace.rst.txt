Kernel_MassTrace
================

.. py:class:: Kernel_MassTrace


   Bases: :py:class:`object`


Cython implementation of _Kernel_MassTrace


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1Kernel_MassTrace.html




.. py:method:: Kernel_MassTrace.computeFwhmArea


Cython signature: double computeFwhmArea()




.. py:method:: Kernel_MassTrace.computeFwhmAreaSmooth


Cython signature: double computeFwhmAreaSmooth()
Computes chromatographic peak area within the FWHM range.




.. py:method:: Kernel_MassTrace.computePeakArea


Cython signature: double computePeakArea()
Sums intensities of all peaks in the mass trace




.. py:method:: Kernel_MassTrace.computeSmoothedPeakArea


Cython signature: double computeSmoothedPeakArea()
Sums all non-negative (smoothed!) intensities in the mass trace




.. py:method:: Kernel_MassTrace.estimateFWHM


Cython signature: size_t estimateFWHM(bool)
Estimates FWHM of chromatographic peak in seconds (based on either raw or smoothed intensities)




.. py:method:: Kernel_MassTrace.findMaxByIntPeak


Cython signature: size_t findMaxByIntPeak(bool)
Returns the index of the mass trace's highest peak within the MassTrace container (based either on raw or smoothed intensities)




.. py:attribute:: Kernel_MassTrace.fwhm_mz_avg




.. py:method:: Kernel_MassTrace.getAverageMS1CycleTime


Cython signature: double getAverageMS1CycleTime()
Returns average scan time of mass trace




.. py:method:: Kernel_MassTrace.getCentroidMZ


Cython signature: double getCentroidMZ()
Returns the centroid m/z




.. py:method:: Kernel_MassTrace.getCentroidRT


Cython signature: double getCentroidRT()
Returns the centroid RT




.. py:method:: Kernel_MassTrace.getCentroidSD


Cython signature: double getCentroidSD()
Returns the centroid SD




.. py:method:: Kernel_MassTrace.getConvexhull


Cython signature: ConvexHull2D getConvexhull()
Returns the mass trace's convex hull




.. py:method:: Kernel_MassTrace.getFWHM


Cython signature: double getFWHM()
Returns FWHM




.. py:method:: Kernel_MassTrace.getFWHMborders


Cython signature: libcpp_pair[size_t,size_t] getFWHMborders()
Returns FWHM boarders




.. py:method:: Kernel_MassTrace.getIntensity


Cython signature: double getIntensity(bool)
Returns the intensity




.. py:method:: Kernel_MassTrace.getLabel


Cython signature: String getLabel()
Returns label of mass trace




.. py:method:: Kernel_MassTrace.getMaxIntensity


Cython signature: double getMaxIntensity(bool)
Returns the max intensity




.. py:method:: Kernel_MassTrace.getQuantMethod


Cython signature: MT_QUANTMETHOD getQuantMethod()
Check if area or median is used for quantification




.. py:method:: Kernel_MassTrace.getSize


Cython signature: size_t getSize()
Returns the number of peaks contained in the mass trace




.. py:method:: Kernel_MassTrace.getSmoothedIntensities


Cython signature: libcpp_vector[double] getSmoothedIntensities()
Returns smoothed intensities (empty if no smoothing was explicitly done beforehand!)




.. py:method:: Kernel_MassTrace.getTraceLength


Cython signature: double getTraceLength()
Returns the length of the trace (as difference in RT)




.. py:method:: Kernel_MassTrace.setCentroidSD


Cython signature: void setCentroidSD(double & tmp_sd)




.. py:method:: Kernel_MassTrace.setLabel


Cython signature: void setLabel(String label)
Sets label of mass trace




.. py:method:: Kernel_MassTrace.setQuantMethod


Cython signature: void setQuantMethod(MT_QUANTMETHOD method)
Determine if area or median is used for quantification




.. py:method:: Kernel_MassTrace.setSmoothedIntensities


Cython signature: void setSmoothedIntensities(libcpp_vector[double] & db_vec)
Sets smoothed intensities (smoothing is done externally, e.g. by LowessSmoothing)




.. py:method:: Kernel_MassTrace.updateMeanMZ


Cython signature: void updateMeanMZ()
Compute & update centroid m/z as mean of m/z values




.. py:method:: Kernel_MassTrace.updateMedianMZ


Cython signature: void updateMedianMZ()
Compute & update centroid m/z as median of m/z values




.. py:method:: Kernel_MassTrace.updateMedianRT


Cython signature: void updateMedianRT()
Compute & update centroid RT as median position of intensities




.. py:method:: Kernel_MassTrace.updateSmoothedMaxRT


Cython signature: void updateSmoothedMaxRT()




.. py:method:: Kernel_MassTrace.updateSmoothedWeightedMeanRT


Cython signature: void updateSmoothedWeightedMeanRT()




.. py:method:: Kernel_MassTrace.updateWeightedMZsd


Cython signature: void updateWeightedMZsd()


Compute & update m/z standard deviation of mass trace as weighted mean of m/z values
-----
Make sure to call update(Weighted)(Mean|Median)MZ() first! <br>
use getCentroidSD() to get result




.. py:method:: Kernel_MassTrace.updateWeightedMeanMZ


Cython signature: void updateWeightedMeanMZ()
Compute & update centroid m/z as weighted mean of m/z values




.. py:method:: Kernel_MassTrace.updateWeightedMeanRT


Cython signature: void updateWeightedMeanRT()
Compute & update centroid RT as a intensity-weighted mean of RTs




