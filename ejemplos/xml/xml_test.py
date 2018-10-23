#xml_file
import xml.etree.ElementTree as ET

tree = ET.parse("xml_file.xml")
tree = ET.ElementTree(ET.fromstring('xml_file'))
print(tree)