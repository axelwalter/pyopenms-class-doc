Param
=====

.. py:class:: Param


   Bases: :py:class:`object`


Cython implementation of _Param


Documentation is available at http://www.openms.de/current_doxygen/html/classOpenMS_1_1Param.html




.. py:method:: Param.addTag


Cython signature: void addTag(libcpp_utf8_string key, libcpp_utf8_string tag)




.. py:method:: Param.addTags


Cython signature: void addTags(libcpp_utf8_string key, libcpp_vector[libcpp_utf8_string] tags)




.. py:method:: Param.asDict




.. py:method:: Param.checkDefaults


- Cython signature: void checkDefaults(libcpp_utf8_string name, Param defaults, libcpp_utf8_string prefix)
- Cython signature: void checkDefaults(libcpp_utf8_string name, Param defaults)




.. py:method:: Param.clear


Cython signature: void clear()




.. py:method:: Param.clearTags


Cython signature: void clearTags(libcpp_utf8_string key)




.. py:method:: Param.copy


- Cython signature: Param copy(libcpp_utf8_string prefix, bool)
- Cython signature: Param copy(libcpp_utf8_string prefix)




.. py:method:: Param.descriptions




.. py:method:: Param.empty


Cython signature: bool empty()




.. py:method:: Param.exists


Cython signature: bool exists(libcpp_utf8_string key)




.. py:method:: Param.get




.. py:method:: Param.getDescription


Cython signature: libcpp_utf8_output_string getDescription(libcpp_utf8_string key)




.. py:method:: Param.getEntry


Cython signature: ParamEntry getEntry(libcpp_utf8_string)




.. py:method:: Param.getSectionDescription


Cython signature: libcpp_utf8_output_string getSectionDescription(libcpp_utf8_string key)




.. py:method:: Param.getTags


Cython signature: libcpp_vector[libcpp_utf8_string] getTags(libcpp_utf8_string key)




.. py:method:: Param.getValue


Cython signature: ParamValue getValue(libcpp_utf8_string key)




.. py:method:: Param.getValueType


Cython signature: ValueType getValueType(libcpp_utf8_string key)




.. py:method:: Param.hasTag


Cython signature: int hasTag(libcpp_utf8_string key, libcpp_utf8_string tag)




.. py:method:: Param.insert


Cython signature: void insert(libcpp_utf8_string prefix, Param param)




.. py:method:: Param.items




.. py:method:: Param.keys




.. py:method:: Param.merge


Cython signature: void merge(Param toMerge)




.. py:method:: Param.remove


Cython signature: void remove(libcpp_utf8_string key)




.. py:method:: Param.removeAll


Cython signature: void removeAll(libcpp_utf8_string prefix)




.. py:method:: Param.setDefaults


- Cython signature: void setDefaults(Param defaults, libcpp_utf8_string prefix, bool showMessage)
- Cython signature: void setDefaults(Param defaults, libcpp_utf8_string prefix)
- Cython signature: void setDefaults(Param defaults)




.. py:method:: Param.setMaxFloat


Cython signature: void setMaxFloat(libcpp_utf8_string key, double max)




.. py:method:: Param.setMaxInt


Cython signature: void setMaxInt(libcpp_utf8_string key, int max)




.. py:method:: Param.setMinFloat


Cython signature: void setMinFloat(libcpp_utf8_string key, double min)




.. py:method:: Param.setMinInt


Cython signature: void setMinInt(libcpp_utf8_string key, int min)




.. py:method:: Param.setSectionDescription


Cython signature: void setSectionDescription(libcpp_utf8_string key, libcpp_utf8_string desc)




.. py:method:: Param.setValidStrings


Cython signature: void setValidStrings(libcpp_utf8_string key, libcpp_vector[libcpp_utf8_string] strings)




.. py:method:: Param.setValue


- Cython signature: void setValue(libcpp_utf8_string key, ParamValue val, libcpp_utf8_string desc, libcpp_vector[libcpp_utf8_string] tags)
- Cython signature: void setValue(libcpp_utf8_string key, ParamValue val, libcpp_utf8_string desc)
- Cython signature: void setValue(libcpp_utf8_string key, ParamValue val)




.. py:method:: Param.size


Cython signature: size_t size()




.. py:method:: Param.update


use cases:


   p.update(dict d)
   p.update(Param p)
   p.update(Param p, int flag)




.. py:method:: Param.values




