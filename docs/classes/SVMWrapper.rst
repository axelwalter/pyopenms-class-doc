SVMWrapper
==========

.. py:class:: SVMWrapper


   Bases: :py:class:`object`


Cython implementation of _SVMWrapper


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1SVMWrapper.html




.. py:attribute:: SVMWrapper.SVM_kernel_type


alias of :py:class:`pyopenms.pyopenms_4.__SVM_kernel_type`


.. py:attribute:: SVMWrapper.SVM_parameter_type


alias of :py:class:`pyopenms.pyopenms_4.__SVM_parameter_type`


.. py:method:: SVMWrapper.calculateGaussTable


Cython signature: void calculateGaussTable(size_t border_length, double sigma, libcpp_vector[double] & gauss_table)




.. py:method:: SVMWrapper.createRandomPartitions


Cython signature: void createRandomPartitions(SVMData & problem, size_t number, libcpp_vector[SVMData] & problems)




.. py:method:: SVMWrapper.getDoubleParameter


Cython signature: double getDoubleParameter(SVM_parameter_type type_)




.. py:method:: SVMWrapper.getIntParameter


Cython signature: int getIntParameter(SVM_parameter_type type_)




.. py:method:: SVMWrapper.getPValue


Cython signature: double getPValue(double sigma1, double sigma2, libcpp_pair[double,double] point)




.. py:method:: SVMWrapper.getSVRProbability


Cython signature: double getSVRProbability()




.. py:method:: SVMWrapper.getSignificanceBorders


Cython signature: void getSignificanceBorders(SVMData & data, libcpp_pair[double,double] & sigmas, double confidence, size_t number_of_runs, size_t number_of_partitions, double step_size, size_t max_iterations)




.. py:method:: SVMWrapper.loadModel


Cython signature: void loadModel(String modelFilename)
The svm-model is loaded. After this, the svm is ready for prediction




.. py:method:: SVMWrapper.mergePartitions


Cython signature: void mergePartitions(libcpp_vector[SVMData] & problems, size_t except_, SVMData & merged_problem)




.. py:method:: SVMWrapper.predict


Cython signature: void predict(SVMData & problem, libcpp_vector[double] & results)
The prediction process is started and the results are stored in 'predicted_labels'




.. py:method:: SVMWrapper.saveModel


Cython signature: void saveModel(String modelFilename)
The model of the trained svm is saved into 'modelFilename'




.. py:method:: SVMWrapper.setParameter


- Cython signature: void setParameter(SVM_parameter_type type_, int value)
- Cython signature: void setParameter(SVM_parameter_type type_, double value)




.. py:method:: SVMWrapper.setTrainingSample


Cython signature: void setTrainingSample(SVMData & training_sample)




.. py:method:: SVMWrapper.setWeights


Cython signature: void setWeights(libcpp_vector[int] & weight_labels, libcpp_vector[double] & weights)




.. py:method:: SVMWrapper.train


Cython signature: int train(SVMData & problem)
The svm is trained with the data stored in the 'svm_problem' structure




