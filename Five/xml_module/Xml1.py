"""
1 xml是实现不同语言或程序之间进行数据交换的协议，跟json差不多，但json使用起来更简单，不过，
古时候，在json还没诞生的黑暗年代，大家只能选择用xml呀，至今很多传统公司如金融行业的很
多系统的接口还主要是xml。

2 xml的格式如下，就是通过<>节点来区别数据结构的:

3 读取xml文件格式数据

"""
import xml.etree.ElementTree as ET

# 写上要处理的文件名称
tree = ET.parse("moudle_xml.xml")
#
root = tree.getroot()
print(root.tag)

# # 遍历xml文档
# for child in root:
#     # tag 就是country attribut 就是属性值
#     print(child.tag, child.attrib)
#     for i in child:
#         # i.tag rank i.text就是rank值
#         print(i.tag, i.text, i.attrib)

# 只遍历year 节点
for node in root.iter('year'):
    print(node.tag, node.text)
