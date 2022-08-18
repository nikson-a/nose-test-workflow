import xml.etree.ElementTree as ET


def coverage_export(path):
    coverage = ET.parse(path + '/coverage.xml')
    coverage = coverage.getroot()
    return coverage.get("lines-valid"), coverage.get("lines-covered"), float(coverage.get("line-rate")) * 100

    # from lxml import etree
    # doc = etree.parse(filename)
    #
    # memoryElem = doc.find('memory')
    # return memoryElem.get('unit')
