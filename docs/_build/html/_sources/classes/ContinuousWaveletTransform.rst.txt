ContinuousWaveletTransform
==========================

.. py:class:: ContinuousWaveletTransform


   Bases: :py:class:`object`


Cython implementation of _ContinuousWaveletTransform


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1ContinuousWaveletTransform.html




.. py:method:: ContinuousWaveletTransform.getLeftPaddingIndex


Cython signature: ptrdiff_t getLeftPaddingIndex()
Returns the position where the signal starts (in the interval [0,end_left_padding_) are the padded zeros)




.. py:method:: ContinuousWaveletTransform.getRightPaddingIndex


Cython signature: ptrdiff_t getRightPaddingIndex()
Returns the position where the signal ends (in the interval (begin_right_padding_,end] are the padded zeros)




.. py:method:: ContinuousWaveletTransform.getScale


Cython signature: double getScale()
Returns the scale of the wavelet




.. py:method:: ContinuousWaveletTransform.getSignal


Cython signature: libcpp_vector[Peak1D] getSignal()
Returns the wavelet transform of the signal




.. py:method:: ContinuousWaveletTransform.getSignalLength


Cython signature: ptrdiff_t getSignalLength()
Returns the signal length [end_left_padding,begin_right_padding]




.. py:method:: ContinuousWaveletTransform.getSize


Cython signature: int getSize()
Returns the signal length including padded zeros [0,end]




.. py:method:: ContinuousWaveletTransform.getSpacing


Cython signature: double getSpacing()
Returns the spacing of raw data




.. py:method:: ContinuousWaveletTransform.getWavelet


Cython signature: libcpp_vector[double] getWavelet()
Returns the wavelet




.. py:method:: ContinuousWaveletTransform.init


Cython signature: void init(double scale, double spacing)
Perform possibly necessary preprocessing steps, like tabulating the Wavelet




.. py:method:: ContinuousWaveletTransform.setLeftPaddingIndex


Cython signature: void setLeftPaddingIndex(ptrdiff_t end_left_padding)
Sets the position where the signal starts




.. py:method:: ContinuousWaveletTransform.setRightPaddingIndex


Cython signature: void setRightPaddingIndex(ptrdiff_t begin_right_padding)
Sets the position where the signal starts




.. py:method:: ContinuousWaveletTransform.setScale


Cython signature: void setScale(double scale)
Sets the spacing of raw data




.. py:method:: ContinuousWaveletTransform.setSignal


Cython signature: void setSignal(libcpp_vector[Peak1D] & signal)
Sets the wavelet transform of the signal




.. py:method:: ContinuousWaveletTransform.setSignalLength


Cython signature: void setSignalLength(ptrdiff_t signal_length)
Sets the signal length [end_left_padding,begin_right_padding]




.. py:method:: ContinuousWaveletTransform.setSpacing


Cython signature: void setSpacing(double spacing)
Sets the spacing of raw data




.. py:method:: ContinuousWaveletTransform.setWavelet


Cython signature: void setWavelet(libcpp_vector[double] & wavelet)
Sets the signal




