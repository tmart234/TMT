## this script will parse a model's used elements
##


import xml.etree.ElementTree as ET
import csv

tree = ET.parse('sample2.xml')
root = tree.getroot()

# set up dictionaries
# multiple elements, values are a list of element dicts of those types
elements = dict.fromkeys(['flows','stencils','boundarys','interactors'])
# singular element dict
element = dict.fromkeys(['guid','ID','name','SourceGuid','TargetGuid','EleProperties'])
# create custom element properties dict as this part will change
# from <b:SelectedIndex> and the properties above

with open('model.csv', 'w', newline='') as r:
    writer = csv.writer(r)
    # write headders in csv file
    writer.writerow(['Flow','Name'])

    for child in root.findall('{http://schemas.datacontract.org/2004/07/ThreatModeling.Model}DrawingSurfaceList'):
        for ele in child.findall('{http://schemas.datacontract.org/2004/07/ThreatModeling.Model}DrawingSurfaceModel'):
            # get Boarders too? anything else?
            for ele2 in ele.findall('{http://schemas.datacontract.org/2004/07/ThreatModeling.Model}Lines'):
                # this level contains a model's elements
                for ele3 in ele2.findall('{http://schemas.microsoft.com/2003/10/Serialization/Arrays}KeyValueOfguidanyType'):
                    for ele4 in ele3.findall('{http://schemas.microsoft.com/2003/10/Serialization/Arrays}Value'):
                        for guid in ele4.findall('{http://schemas.datacontract.org/2004/07/ThreatModeling.Model.Abstracts}Guid'):
                            element['guid'] = guid.text
                        for gen_type in ele4.findall('{http://schemas.datacontract.org/2004/07/ThreatModeling.Model.Abstracts}GenericTypeId'):
                            element['id'] = gen_type.text
                        for source in ele4.findall('{http://schemas.datacontract.org/2004/07/ThreatModeling.Model.Abstracts}SourceGuid'):
                            element['SourceGuid'] = source.text
                        for source in ele4.findall('{http://schemas.datacontract.org/2004/07/ThreatModeling.Model.Abstracts}TargetGuid'):
                            element['TargetGuid'] = source.text
                        for ele5 in ele4.findall('{http://schemas.datacontract.org/2004/07/ThreatModeling.Model.Abstracts}Properties'):
                            for ele6 in ele5.iter('{http://schemas.microsoft.com/2003/10/Serialization/Arrays}anyType'):
                                for ele7 in ele6.iter():
                                   if 'StringDisplayAttribute' in ET.tostring(ele7, method='text'):
                                       print(ele7.attrib)
                                # <i:type="c:string">value</b:Value> for custom names
                                # add element to elements