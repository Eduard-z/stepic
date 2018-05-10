from xml.etree import ElementTree

tree = ElementTree.parse(r"C:\Users\Admin\Desktop\module3\example.xml")
root = tree.getroot()

greg = root[0]
# module1 = next(greg.iter("module1"))
# print(module1, module1.text)
# module1.text = str(float(module1.text) + 30)  # change module1 value

# certificate = greg[2]
# certificate.set("type", "with distinction")  # add attribute

# description = ElementTree.Element("description")  # add element
# description.text = "Showed excellent skills during the course"
# greg.append(description)

# description = greg.find("description")
# greg.remove(description)  # delete element

tree.write("example_modified.xml")




# print(ElementTree.ElementTree.__doc__)
# use root = ElementTree.fromstring(string_xml_data) to parse from str
"""
print(root)  # <Element 'studentsList' at 0x000000000047CD18>
print(root.tag, root.attrib)  # studentsList {}

print(root[0][0].text)  # Greg

for child in root:
    print(child.tag, child.attrib)  # student {'id': '1'} ; student {'id': '2'}

for element in root.iter("scores"):  # .findall for children (start from 'module1')
    score_sum = 0
    for child in element:
        score_sum += float(child.text)  # 240.0 ; 240.2
    print(score_sum)
"""