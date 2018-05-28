import xml.etree.ElementTree as ET 
from xml.etree.ElementTree import SubElement
import sys
from xml.dom import minidom

def anchorString():
    global anc_string
    for anchor in root.iter('anchor'):
        if anchor is None:
            continue
        temp = anchor.text.split(':')[-1]
        if temp.isalnum():
            anc_string = temp
            break
    if not anc_string:
        sys.exit("Error: anchor_string is empty Exiting...")
        

def validation():
    if not cdProcess_value:
        sys.exit("Error: cdProcess_value is empty Exiting...")
    if not destFilename_value:
        sys.exit("destFilename_value is empty Exiting...")
    if not ndmSnode_value:
        sys.exit("Error: ndm_Snode_value is empty Exiting...")

def XMLCreation():
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for child in root:
        print child
        completeSub = SubElement(child, 'completeSubscription')
        sub = SubElement(completeSub, 'subscription')
        appRef = SubElement(sub, 'applicationReference')
        appRef.text = 'SSCAction'
        folder = SubElement(sub, 'folder')
        folder.text = '/'+which_ndm
        anchor = SubElement(sub, 'anchor')
        anchor.text = '/'+which_ndm+':'+anc_string
        customAttr = SubElement(sub, 'customAttributes')
        customProp = SubElement(customAttr, 'customProperties')
        entry1 = SubElement(customProp, 'entry', key='actionCode')
        entry1.text = 'NDM'
        entry2 = SubElement(customProp, 'entry', key='actionSequence')
        entry2.text = which_ndm[-2:]
        entry3 = SubElement(customProp, 'entry', key='cdProcess')
        entry3.text = cdProcess_value
        entry4 = SubElement(customProp, 'entry', key='cdSite')
        entry4.text = cdSite_value
        entry5 = SubElement(customProp, 'entry', key='destFilename')
        entry5.text = destFilename_value
        entry6 = SubElement(customProp, 'entry', key='destFolder')
        entry6.text = destFolder_value
        entry7 = SubElement(customProp, 'entry', key='fileExtension')
        entry7.text = fileExtension_value
        entry8 = SubElement(customProp, 'entry', key='ndmSnode')
        entry8.text = ndmSnode_value
        entry9 = SubElement(customProp, 'entry', key='userPass')
        entry9.text = userPass_value
        localCert = SubElement(customAttr, 'localCertificates')
        partnerCert = SubElement(customAttr, 'partnerCertificates')
        userCert = SubElement(customAttr, 'userCertificates')
        #child.append(completeSub)
        #print tostring(completeSub)
        #print '================'
        #tostring(child, pretty_print=True)
        #using minidom just for pretty print 
#    xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="\t")
#    with open("New_Database.xml", "w") as f:
#        f.write(xmlstr.encode('utf-8'))
    tree.write(open('new_xml.xml', 'w'),  xml_declaration=True, encoding='utf-8')
      

if __name__ == '__main__':
    anc_string = ''
    xml_file = 'C:\Users\\admin\Desktop\scripts\\account_export_w572415_uat.xml'

    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    which_ndm = raw_input("Please Enter which_ndm: ") or "NDM01"
    cdProcess_value = raw_input("Please enter valid cdProcess_value: ") or "zos_txt1000x1004_vb"
    cdSite_value = raw_input("Please enter cdSite value: ") or "zos_txt1000x1004_vb"
    destFilename_value = raw_input("Please enter destFilename_value : ") or "KFT.TRN.D768K7E.ETD(+1)"
    destFolder_value = raw_input("please enter destincation folder : ") or "/alfg06/lfg/cdudata/mm06_seblux/in/"
    ndmSnode_value = raw_input("please enter ndmSnode_value: ") or "SSB.MVS.W.VIP"
    fileExtension_value = raw_input("Please enter fileextension value") or ""
    userPass_value = raw_input("please enter user pass value: ") or ""
    

    validation()
    anchorString()
    XMLCreation()

