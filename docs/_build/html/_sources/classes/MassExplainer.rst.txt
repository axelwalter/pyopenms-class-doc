MassExplainer
=============

.. py:class:: MassExplainer


   Bases: :py:class:`object`


Cython implementation of _MassExplainer


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1MassExplainer.html




.. py:method:: MassExplainer.compute


Cython signature: void compute()
Fill map with possible mass-differences along with their explanation




.. py:method:: MassExplainer.getAdductBase


Cython signature: libcpp_vector[Adduct] getAdductBase()
Returns the set of adducts




.. py:method:: MassExplainer.getCompomerById


Cython signature: Compomer getCompomerById(size_t id)
Returns a compomer by its Id (useful after a query() )




.. py:method:: MassExplainer.setAdductBase


Cython signature: void setAdductBase(libcpp_vector[Adduct] adduct_base)
Sets the set of possible adducts




