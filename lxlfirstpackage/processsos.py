# -*- coding:utf-8 -*-
from lxml import etree

# 命名空间的设置
fin = open(r'F:\PythonLearning\resource\Argo_sensor.xml', 'r')
stationtext = unicode(fin.read(), "utf-8")
stationXml = etree.fromstring(stationtext)
fin.close()
sensorNS = stationXml.nsmap
ns = "{%s}" % sensorNS[None]
sensorNS['ns'] = sensorNS[None]
del sensorNS[None]
sml = "{%s}" % sensorNS['sml']
swe = "{%s}" % sensorNS['swe']
xsi = "{%s}" % sensorNS['xsi']
gml = "{%s}" % sensorNS['gml']
xlink = "{%s}" % sensorNS['xlink']


class sensor():
    '''处理传感器xml'''

    def __init__(self, sensorXmlPath=r'F:\PythonLearning\resource\Argo_sensor1.xml'):
        '''构造函数,读取传入的sensorxml,生成一个sensor的DOM'''
        fin = open(sensorXmlPath, 'r')
        sensortext = unicode(fin.read(), "utf-8")
        self.sensorXml = etree.fromstring(sensortext)
        fin.close()
        self.Rnamedic = {
            u"CTD_PRES": [u"dbar", u"观测深度分辨率"],
            u"PRES": [u"dbar", u"观测深度分辨率"],
            u"CTD_TEMP": [u"degC", u"海水温度观测分辨率"],
            u"TEMP": [u"degC", u"海水温度观测分辨率"],
            u"CTD_CNDC": [u"psu", u"海水盐度观测分辨率"],
            u"CNDC": [u"psu", u"海水盐度观测分辨率"],
            u"PSAL": [u"psu", u"海水盐度观测分辨率"],
            u"S/m": [u"海水盐度观测分辨率"],
            u"Siemens/meter": u"海水盐度观测分辨率"}
        self.RMSnamedic = {
            u"CTD_PRES": [u"dbar", u"观测深度精度"],
            u"PRES": [u"dbar", u"观测深度精度"],
            u"CTD_TEMP": [u"degC", u"海水温度观测精度"],
            u"TEMP": [u"degC", u"海水温度观测精度"],
            u"CTD_CNDC": [u"psu", u"海水盐度观测精度"],
            u"CNDC": [u"psu", u"海水盐度观测精度"],
            u"PSAL": [u"psu", u"海水盐度观测精度"],
            u"S/m": u"海水盐度观测精度",
            u"Siemens/meter": u"海水盐度观测精度"}
        self.Rdefdic = {
            u"CTD_PRES": [u"dbar", u"urn:ogc:def:property:presMeasurementResolution"],
            u"PRES": [u"dbar", u"urn:ogc:def:property:presMeasurementResolution"],
            u"CTD_TEMP": [u"degC", u"urn:ogc:def:property:tempMeasurementResolution"],
            u"TEMP": [u"degC", u"urn:ogc:def:property:tempMeasurementResolution"],
            u"CTD_CNDC": [u"psu", u"urn:ogc:def:property:cndcMeasurementResolution"],
            u"CNDC": [u"psu", u"urn:ogc:def:property:cndcMeasurementResolution"],
            u"PSAL": [u"psu", u"urn:ogc:def:property:cndcMeasurementResolution"],
            u"S/m": u"urn:ogc:def:property:cndcMeasurementResolution",
            u"Siemens/meter": u"urn:ogc:def:property:cndcMeasurementRMS"}
        self.RMSdefdic = {
            u"CTD_PRES": [u"dbar", u"urn:ogc:def:property:presMeasurementRMS"],
            u"PRES": [u"dbar", u"urn:ogc:def:property:presMeasurementRMS"],
            u"CTD_TEMP": [u"degC", u"urn:ogc:def:property:tempMeasurementRMS"],
            u"TEMP": [u"degC", u"urn:ogc:def:property:tempMeasurementRMS"],
            u"CTD_CNDC": [u"psu", u"urn:ogc:def:property:cndcMeasurementRMS"],
            u"CNDC": [u"psu", u"urn:ogc:def:property:cndcMeasurementRMS"],
            u"PSAL": [u"psu", u"urn:ogc:def:property:cndcMeasurementRMS"],
            u"S/m": u"urn:ogc:def:property:cndcMeasurementRMS",
            u"Siemens/meter": u"urn:ogc:def:property:cndcMeasurementRMS"}
        self.ioputdic = {
            u"CTD_PRES": [u"dbar", u"观测深度"],
            u"PRES": [u"dbar", u"观测深度"],
            u"CTD_TEMP": [u"degC", u"海水温度"],
            u"TEMP": [u"degC", u"海水温度"],
            u"CTD_CNDC": [u"psu", u"海水盐度"],
            u"CNDC": [u"psu", u"海水盐度"],
            u"PSAL": [u"psu", u"海水盐度"],
            u"S/m": [u"海水盐度"],
            u"Siemens/meter": [u"海水盐度"]}
        self.iodefdic = {
            u"CTD_PRES": [u"dbar", u"urn:ogc:def:property:OGC:1.0:argoFloatObservationDepth"],
            u"PRES": [u"dbar", u"urn:ogc:def:property:OGC:1.0:argoFloatObservationDepth"],
            u"CTD_TEMP": [u"degC", u"urn:ogc:def:property:OGC:1.0:argoFloatZtmp"],
            u"TEMP": [u"degC", u"urn:ogc:def:property:OGC:1.0:argoFloatZtmp"],
            u"CTD_CNDC": [u"psu", u"urn:ogc:def:property:OGC:1.0:argoFloatZsal"],
            u"CNDC": [u"psu", u"urn:ogc:def:property:OGC:1.0:argoFloatZsal"],
            u"PSAL": [u"psu", u"urn:ogc:def:property:OGC:1.0:argoFloatZsal"],
            u"S/m": u"urn:ogc:def:property:OGC:1.0:argoFloatZsal",
            u"Siemens/meter": u"urn:ogc:def:property:OGC:1.0:argoFloatZsal"}

    def __unicode(self, stringtmp):
        if type(stringtmp) is not unicode:
            stringtmp = stringtmp.decode('utf-8')
        return stringtmp

    def __setResolution(self, uomCode, value):
        '''根据uomCode插入观测分辨率'''
        uomCode = self.__unicode(uomCode.replace(' ', ''))
        value = self.__unicode(value)
        path = u"/ns:SensorML/sml:member/sml:System/sml:capabilities/swe:DataRecord"
        root = self.sensorXml.xpath(path, namespaces=sensorNS)[0]
        valueele = etree.Element(swe + "value", nsmap=sensorNS)
        valueele.text = value
        uomele = etree.Element(swe + "uom", nsmap=sensorNS)
        uomele.set("code", self.Rnamedic[uomCode][0])
        quantityele = etree.Element(swe + "Quantity", nsmap=sensorNS)
        quantityele.set("definition", self.Rdefdic[uomCode][1])
        quantityele.append(uomele)
        quantityele.append(valueele)
        fieldele = etree.Element(swe + "field", nsmap=sensorNS)
        fieldele.set("name", self.Rnamedic[uomCode][1])
        fieldele.append(quantityele)
        root.append(fieldele)

    def __setRMS(self, uomCode, value):
        '''根据uomCode插入观测精度'''
        uomCode = self.__unicode(uomCode)
        value = self.__unicode(value)
        path = u"/ns:SensorML/sml:member/sml:System/sml:capabilities/swe:DataRecord"
        root = self.sensorXml.xpath(path, namespaces=sensorNS)[0]
        valueele = etree.Element(swe + "value", nsmap=sensorNS)
        valueele.text = value
        uomele = etree.Element(swe + "uom", nsmap=sensorNS)
        uomele.set("code", self.RMSdefdic[uomCode][0])
        quantityele = etree.Element(swe + "Quantity", nsmap=sensorNS)
        quantityele.set("definition", self.RMSdefdic[uomCode][1])
        quantityele.append(uomele)
        quantityele.append(valueele)
        fieldele = etree.Element(swe + "field", nsmap=sensorNS)
        fieldele.set("name", self.RMSnamedic[uomCode][1])
        fieldele.append(quantityele)
        root.append(fieldele)

    def setDescription(self, sensorName):
        '''根据sensorName改变传感器的description内容'''
        if type(sensorName) is not unicode:
            sensorName = sensorName.decode('utf-8')
        path = "/ns:SensorML/sml:member/sml:System/gml:description"
        description = self.sensorXml.xpath(path, namespaces=sensorNS)
        description[0].text = sensorName + u"传感器是Argo剖面浮标的海水温、盐度信息采集漂流设备，集数据采集存储、无线数据通信、GPS、" \
                                           u"以及无线扩展等功能于一体,负责Argo剖面浮标位移等工作情况的远程监测与控制，以及全球海洋温" \
                                           u"度、盐度、环流及其它们变化情况的动态监测。"

    def setKeywords(self, sensorName, stationName, stationCode):
        '''根据sensorName改变keyword'''
        sensorName = self.__unicode(sensorName)
        stationCode = self.__unicode(stationCode)
        path = "/ns:SensorML/sml:member/sml:System/sml:keywords/sml:KeywordList/sml:keyword"
        keyword = self.sensorXml.xpath(path, namespaces=sensorNS)
        keyword[3].text = sensorName
        keyword[5].text = stationName + u" " + stationCode

    def appendKeywords(self, uomcode):
        '''根据观测能力,添加关键字'''
        uomcode = self.__unicode(uomcode)
        path = "/ns:SensorML/sml:member/sml:System/sml:keywords/sml:KeywordList"
        keyword = self.sensorXml.xpath(path, namespaces=sensorNS)
        newkeyword = etree.Element(sml + 'keyword', nsmap=sensorNS)
        newkeyword.text = self.ioputdic[uomcode][1] + u"观测"
        keyword[0].append(newkeyword)

    def setIdentifier(self, stationName, stationCode, sensorName, serialNumber, maker):
        '''根据平台Name,平台Code,传感器Name生成标识码'''
        stationName = self.__unicode(stationName)
        stationCode = self.__unicode(stationCode)
        sensorName = self.__unicode(sensorName)

        path = "/ns:SensorML/sml:member/sml:System/sml:identification/sml:IdentifierList/sml:identifier/s" \
               "ml:Term/sml:value"
        identifier = self.sensorXml.xpath(path, namespaces=sensorNS)

        identifier[
            0].text = u"urn:liesmars:insitusensor:ArgoFloat" \
                      u"-" + stationName.replace(u" ",u"-") + u"-" + stationCode + u"-" + sensorName
        identifier[1].text = sensorName
        identifier[2].text = sensorName
        identifier[3].text = stationName + u" " + stationCode
        identifier[
            4].text = u"urn:liesmars:insitusensor:platform:ArgoFloat-" + stationName.replace(u" ",
                                                                                             u"-") + u"-" + stationCode
        identifier[5].text = serialNumber
        identifier[6].text = maker

    def setValidtime(self, Time):
        '''更具平台时间设置validtime'''
        if type(Time) is not unicode:
            Time = Time.decode('utf-8')
        path = u"/ns:SensorML/sml:member/sml:System/sml:validTime/gml:TimePeriod/gml:beginPosition"
        validtime = self.sensorXml.xpath(path, namespaces=sensorNS)
        validtime[0].text = Time

    def setQuantity(self, uomcode, Rvalue, RMSvalue):
        '''根据uomcode生成各个field的内容'''
        self.__setResolution(uomcode, Rvalue)
        self.__setRMS(uomcode, RMSvalue)

    def setOrg(self, institution):
        '''设置联系单位名称'''
        institution = self.__unicode(institution)
        path = u"/ns:SensorML/sml:member/sml:System/sml:contact/sml:ResponsibleParty/sml:organizationName"
        org = self.sensorXml.xpath(path, namespaces=sensorNS)
        org[0].text = institution

    def setInterface(self, stationName, stationCode, sensorName):
        '''根据stationName,stationCode,sensorName设置interface'''
        stationName = self.__unicode(stationName)
        stationCode = self.__unicode(stationCode)
        sensorName = self.__unicode(sensorName)
        path = u"/ns:SensorML/sml:member/sml:System/sml:interfaces/sml:InterfaceList/sml:interface"
        interfaceName = self.sensorXml.xpath(path, namespaces=sensorNS)
        namevalue = u"ArgoFloat-" + stationName.replace(u" ", u"-") + u"-" + stationCode + u"-" + sensorName + u"_SOS"
        interfaceName[0].set("name", namevalue)

        path = u"/ns:SensorML/sml:member/sml:System/sml:interfaces/sml:InterfaceList/sml:interface" \
               u"/sml:InterfaceDefinition/sml:serviceLayer/swe:DataRecord/swe:field[3]/swe:Text/swe:value"
        interfaceValue = self.sensorXml.xpath(path, namespaces=sensorNS)
        interfaceValue[
            0].text = u"urn:liesmars:insitusensor:ArgoFloat-" + stationName.replace(u" ",
                                                                                    u"-") + u"-" + stationCode + u"-" + sensorName

    def __setInput(self, uomCode):
        '''根据uomCode设置输入,与setQuantity对应'''
        uomCode = self.__unicode(uomCode)
        path = u"/ns:SensorML/sml:member/sml:System/sml:inputs/sml:InputList"
        root = self.sensorXml.xpath(path, namespaces=sensorNS)[0]
        observablePropertyele = etree.Element(swe + "ObservableProperty", nsmap=sensorNS)
        observablePropertyele.set("definition", self.iodefdic[uomCode][1])
        inputele = etree.Element(sml + "input", nsmap=sensorNS)
        inputele.set("name", self.ioputdic[uomCode][1])
        inputele.append(observablePropertyele)
        root.append(inputele)

    def __setOutput(self, uomCode):
        '''根据uomCode设置输出,与setQuantity对应'''
        uomCode = self.__unicode(uomCode)
        path = u"/ns:SensorML/sml:member/sml:System/sml:outputs/sml:OutputList"
        root = self.sensorXml.xpath(path, namespaces=sensorNS)[0]

        idele = etree.Element("id")
        idele.text = u"LIESMARS"

        nameele = etree.Element("name")
        nameele.text = u"测绘遥感信息工程国家重点实验室（武汉大学)"

        offeringele = etree.Element("offering")
        offeringele.append(idele)
        offeringele.append(nameele)

        metaDataPropertyele = etree.Element(gml + "metaDataProperty", nsmap=sensorNS)
        metaDataPropertyele.append(offeringele)

        uomele = etree.Element(swe + "uom", nsmap=sensorNS)
        uomele.set("code", self.iodefdic[uomCode][0])

        quantityele = etree.Element(swe + "Quantity", nsmap=sensorNS)
        quantityele.set("definition", self.iodefdic[uomCode][1])
        quantityele.append(metaDataPropertyele)
        quantityele.append(uomele)

        outputele = etree.Element(sml + "output", nsmap=sensorNS)
        outputele.set("name", self.ioputdic[uomCode][1])
        outputele.append(quantityele)

        root.append(outputele)

    def setIOput(self, uomCode):
        '''根据uomCode设置输入输出,与setQuantity对应'''
        uomCode = self.__unicode(uomCode)
        self.__setInput(uomCode)
        self.__setOutput(uomCode)

    def toString(self):
        '''把传感器DOM变成字符串,编码格式为utf-8'''
        return etree.tostring(self.sensorXml, encoding='utf-8', pretty_print=True)


class station():
    '''处理浮标xml'''

    def __init__(self, stationXmlPath=r'F:\PythonLearning\resource\Argo_station1.xml'):
        '''构造函数,读取传入的sensorxml,生成一个sensor的DOM'''
        fin = open(stationXmlPath, 'r')
        stationtext = unicode(fin.read(), "utf-8")
        self.stationXml = etree.fromstring(stationtext)
        fin.close()

    def __unicode(self, stringtmp):
        if type(stringtmp) is not unicode:
            stringtmp = stringtmp.decode('utf-8')
        return stringtmp

    def setDescription(self, stationName, stationCode, Description, project):
        '''根据sensorName改变浮标的description内容'''
        stationName = self.__unicode(stationName)
        stationCode = self.__unicode(stationCode)
        Description = self.__unicode(Description)
        project = self.__unicode(project)
        path = "/ns:SensorML/sml:member/sml:System/gml:description"
        description = self.stationXml.xpath(path, namespaces=sensorNS)
        description[0].text = u"Argo是“全球海洋观测业务系统计划(GOOS)”中的一个针对深海区温盐结构观测的子计" \
                              u"划。" + stationName + u" " + stationCode + u"是" + Description + u",即" + project + u"项" \
                                                                                                                u"目中采用自动剖面观测" \
                                                                                                                u"海水温、盐度的漂流设备，对于研究全球海洋的温度、盐度、环流及其它们的变化情况。"

    def setKeywords(self, stationName, stationCode):
        stationCode = self.__unicode(stationCode)
        stationName = self.__unicode(stationName)
        path = u"/ns:SensorML/sml:member/sml:System/sml:keywords/sml:KeywordList/sml:keyword"
        keywords = self.stationXml.xpath(path, namespaces=sensorNS)
        keywords[2].text = stationName + u"-" + stationCode

    def setIdentifier(self, stationName, stationCode):
        stationName = self.__unicode(stationName)
        stationCode = self.__unicode(stationCode)
        path = u"/ns:SensorML/sml:member/sml:System/sml:identification/sml:IdentifierList/sml:identifier" \
               u"/sml:Term/sml:value"
        identifier = self.stationXml.xpath(path, namespaces=sensorNS)
        identifier[0].text = u"urn:liesmars:insitusensor:platform:ArgoFloat" \
                             u"-" + stationName.replace(u" ", u"-") + u"-" + stationCode
        identifier[1].text = stationName + u" " + stationCode + u"剖面浮标"
        identifier[2].text = stationName + u" " + stationCode
        identifier[3].text = stationCode

    def __setSensorname(self, sensorname):
        sensorname = self.__unicode(sensorname)
        path = u"/ns:SensorML/sml:member/sml:System/sml:identification/sml:IdentifierList"
        root = self.stationXml.xpath(path, namespaces=sensorNS)[0]

        valueele = etree.Element(sml + "value", nsmap=sensorNS)
        valueele.text = sensorname

        termele = etree.Element(sml + "Term", nsmap=sensorNS)
        termele.set("definition", u"urn:ogc:def:identifier:OGC:1.0:associatedSensorName")
        termele.append(valueele)

        identifierele = etree.Element(sml + "identifier", nsmap=sensorNS)
        identifierele.set("name", u"搭载传感器名称")
        identifierele.append(termele)

        root.append(identifierele)

    def __setSensorid(self, stationName, stationCode, sensorName):
        stationName = self.__unicode(stationName)
        stationCode = self.__unicode(stationCode)
        sensorName = self.__unicode(sensorName)

        path = u"/ns:SensorML/sml:member/sml:System/sml:identification/sml:IdentifierList"
        root = self.stationXml.xpath(path, namespaces=sensorNS)[0]

        valueele = etree.Element(sml + "value", nsmap=sensorNS)
        valueele.text = u"urn:liesmars:insitusensor:ArgoFloat-" \
                        u"" + stationName.replace(u" ", u"-") + u"-" + stationCode + u"-" + sensorName

        termele = etree.Element(sml + "Term", nsmap=sensorNS)
        termele.set("definition", u"urn:ogc:def:identifier:OGC:1.0:associatedSensorUniqueID")
        termele.append(valueele)

        identifierele = etree.Element(sml + "identifier", nsmap=sensorNS)
        identifierele.set("name", u"搭载传感器标识码")
        identifierele.append(termele)

        root.append(identifierele)

    def setLoadsensors(self, stationName, stationCode, sensorlist):
        stationName = self.__unicode(stationName)
        stationCode = self.__unicode(stationCode)

        for sensorName in sensorlist:
            self.__setSensorname(sensorName)
            self.__setSensorid(stationName, stationCode, sensorName)

    def setValidtime(self, Time):
        '''更具平台时间设置validtime'''
        if type(Time) is not unicode:
            Time = Time.decode('utf-8')
        path = u"/ns:SensorML/sml:member/sml:System/sml:validTime/gml:TimePeriod/gml:beginPosition"
        validtime = self.stationXml.xpath(path, namespaces=sensorNS)
        validtime[0].text = Time

    def setCategory(self, stationName):
        stationName = self.__unicode(stationName)
        path = u"/ns:SensorML/sml:member/sml:System/sml:characteristics/swe:DataRecord/swe:field[1]" \
               u"/swe:Category/swe:value"
        category = self.stationXml.xpath(path, namespaces=sensorNS)
        category[0].text = stationName

    def setOrg(self, institution):
        '''设置联系单位名称'''
        institution = self.__unicode(institution)
        path = u"/ns:SensorML/sml:member/sml:System/sml:contact/sml:ResponsibleParty/sml:organizationName"
        org = self.stationXml.xpath(path, namespaces=sensorNS)
        org[0].text = institution

    def setInterface(self, stationName, stationCode):
        '''根据stationName,stationCode,sensorName设置interface'''
        stationName = self.__unicode(stationName)
        stationCode = self.__unicode(stationCode)
        path = u"/ns:SensorML/sml:member/sml:System/sml:interfaces/sml:InterfaceList/sml:interface"
        interfaceName = self.stationXml.xpath(path, namespaces=sensorNS)
        namevalue = u"ArgoFloat-" + stationName.replace(u" ", u"-") + u"-" + stationCode + u"_SOS"
        interfaceName[0].set("name", namevalue)

        path = u"/ns:SensorML/sml:member/sml:System/sml:interfaces/sml:InterfaceList/sml:interface" \
               u"/sml:InterfaceDefinition/sml:serviceLayer/swe:DataRecord/swe:field[3]/swe:Text/swe:value"
        interfaceValue = self.stationXml.xpath(path, namespaces=sensorNS)
        interfaceValue[
            0].text = u"urn:liesmars:insitusensor:platform:ArgoFloat-" + stationName.replace(u" ",
                                                                                             u"-") + u"-" + stationCode

    def setComponent(self, stationName, stationCode, sensorlist):
        stationName = self.__unicode(stationName)
        stationCode = self.__unicode(stationCode)
        sensorlist = [self.__unicode(item) for item in sensorlist]

        path = u"/ns:SensorML/sml:member/sml:System/sml:components/sml:ComponentList"
        root = self.stationXml.xpath(path, namespaces=sensorNS)[0]

        for sensorName in sensorlist:
            componentele = etree.Element(sml + "component", nsmap=sensorNS)
            componentele.set("name", sensorName)
            href = u"urn:liesmars:insitusensor:ArgoFloat" \
                   u"-" + stationName.replace(u" ", u"-") + u"-" + stationCode + u"-" + sensorName
            componentele.set(xlink + "href", href)
            root.append(componentele)

    def toString(self):
        '''把浮标DOM变成字符串,编码格式为utf-8'''
        return etree.tostring(self.stationXml, encoding='utf-8', pretty_print=True)


def setstation(stationName, stationCode, description, project, institution, Time, loadsensorNamelist):
    # loadsensorNamelist = ["SBE-CP-41-1518", "SBE-CP-41-1835", "SBE-CP-41-5838"]
    # stationName = "APEX Profiling Float"
    # stationCode = "2900452"
    # description = "Argo METRI/KMA, Republic of Korea"
    # project = "Argo KORDI"
    # time = "2004-10-18T00:39:28.0Z"
    # institution = "Korea Meteorological Administration (KMA)"
    floatstation = station(r"F:\PythonLearning\resource\Argo_station1.xml")
    floatstation.setDescription(stationName, stationCode, description, project)
    floatstation.setIdentifier(stationName, stationCode)
    floatstation.setKeywords(stationName, stationCode)
    floatstation.setLoadsensors(stationName, stationCode, loadsensorNamelist)
    floatstation.setComponent(stationName, stationCode, loadsensorNamelist)
    floatstation.setValidtime(Time)
    floatstation.setCategory(stationName)
    floatstation.setOrg(institution)
    floatstation.setInterface(stationName, stationCode)
    fout = open("F:\\PythonLearning\\resource\\stations\\" + stationName + "-" + stationCode + ".xml", 'w')
    fout.write(floatstation.toString())
    fout.close()


def setsensor(stationName, stationCode, institution, Time, sensorName, sensornum, maker, uomlist):
    # uomlist = [("dbar", '2.4', '1')]
    # stationName = "APEX Profiling Float"
    # stationCode = "2900452"
    # institution = "Korea Meteorological Administration (KMA)"
    # time = "2004-10-18T00:39:28.0Z"
    # sensorName = "SBE-CP-41-1518"
    # sensornum = "1518"
    # maker = "SBE"
    floatsensor = sensor(r"F:\PythonLearning\resource\Argo_sensor1.xml")
    floatsensor.setDescription(sensorName)
    floatsensor.setKeywords(sensorName, stationName, stationCode)
    floatsensor.setIdentifier(stationName, stationCode, sensorName, sensornum, maker)
    floatsensor.setValidtime(Time)
    for (uom, rvalue, rmsvalue) in uomlist:
        floatsensor.setQuantity(uom, rvalue, rmsvalue)
        floatsensor.setIOput(uom)
        floatsensor.appendKeywords(uom)
    floatsensor.setOrg(institution)
    floatsensor.setInterface(stationName, stationCode, sensorName)

    fout = open("F:\\PythonLearning\\resource\\sensors\\" + stationName + "-" + stationCode + "-" + sensorName + ".xml",
                'w')
    fout.write(floatsensor.toString())
    fout.close()
