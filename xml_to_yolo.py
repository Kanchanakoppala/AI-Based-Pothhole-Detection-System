import os
import xml.etree.ElementTree as ET

XML_DIR = "dataset/annotations"
LABEL_DIR = "dataset/labels"

os.makedirs(LABEL_DIR, exist_ok=True)

count = 0

for xml_file in os.listdir(XML_DIR):

    if not xml_file.endswith(".xml"):
        continue

    xml_path = os.path.join(XML_DIR, xml_file)

    tree = ET.parse(xml_path)
    root = tree.getroot()

    width = int(root.find("size/width").text)
    height = int(root.find("size/height").text)

    txt_path = os.path.join(
        LABEL_DIR,
        xml_file.replace(".xml", ".txt")
    )

    with open(txt_path, "w") as f:

        for obj in root.findall("object"):

            xmin = float(obj.find("bndbox/xmin").text)
            ymin = float(obj.find("bndbox/ymin").text)
            xmax = float(obj.find("bndbox/xmax").text)
            ymax = float(obj.find("bndbox/ymax").text)

            x_center = ((xmin + xmax) / 2) / width
            y_center = ((ymin + ymax) / 2) / height

            box_width = (xmax - xmin) / width
            box_height = (ymax - ymin) / height

            f.write(
                f"0 {x_center} {y_center} {box_width} {box_height}\n"
            )

    count += 1

print(f"Converted {count} XML files.")