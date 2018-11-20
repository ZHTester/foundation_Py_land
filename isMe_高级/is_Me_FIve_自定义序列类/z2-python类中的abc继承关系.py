# ecoding=utf-8
"""
���������е�Э�� :
1 from collections import abc   ����������������ص�Э�鶼�Ǵ����collections����� abcģ���µ�
2 "Sequence",---> ���ɱ���������� "MutableSequence", ------> �ɱ���������� ��������������صĳ������
   ���õĳ��������԰������Ǹ��ӿ��ٵ����python�����õ����ݽṹ�����õ�����������ʲô���ӵ�
   ����Sequence�Ǳ�MutableSequence ���ӻ����Ļ��� Ҳ��������
3 "Sequence",---> ���ɱ����������  ��Щħ�������Ĺ��������ǲ��ɱ����������Э�飬
   �������ǵĲ��ɱ���������Ͷ��������������Ľӿ�,����˵���������ԣ������ܹ������ǲ��ɱ�������������ݡ�
class Sequence(Reversible�����ݵķ�ת abc---cba��, Collection):
Collection   -----> class Collection(Sized, Iterable, Container): ----> size ʵ��len������������Collection�ĳ���
                                                                        iterable ������ ���ǾͿ��Խ���forѭ�� Ҳ���ǿɵ�����
                                                                        Container ���ǾͿ���ʹ��if in

4  MutableSequence -------> �ɱ��������������
**2** �ɱ����������벻�ɱ������������������������� ���ֵ��ɾ��ֵ __setitem__�����ֵ�� &&  __delitem__��ɾ��ֵ��
class MutableSequence(Sequence):

    @abstractmethod ���󷽷�
    def __setitem__(self, index, value):
        raise IndexError

    @abstractmethod
    def __delitem__(self, index):
        raise IndexError

���� �ɱ�������������ͻ����кܶຯ�� -----> ����鿴Դ��
    def append(self, value):
        'S.append(value) -- append value to the end of the sequence'
        self.insert(len(self), value)

    def clear(self):
        'S.clear() -> None -- remove all items from S'
        try:
            while True:
                self.pop()
        except IndexError:
            pass

    def reverse(self):
        'S.reverse() -- reverse *IN PLACE*'
        n = len(self)
        for i in range(n//2):
            self[i], self[n-i-1] = self[n-i-1], self[i]

    def extend(self, values):
        'S.extend(iterable) -- extend sequence by appending elements from the iterable'
        for v in values:
            self.append(v)


1 ��Щ������ħ�������Լ������͹����������������͵�Э��
2
"""
from collections import abc

