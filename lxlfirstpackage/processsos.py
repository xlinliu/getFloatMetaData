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
        self.Rnamedic = {u"dbar": u"观测深度分辨率", u"degC": u"海水温度观测分辨率", u"psu": u"海水盐度观测分辨率"}
        self.RMSnamedic = {u"dbar": u"观测深度精度", u"degC": u"海水温度观测精度", u"psu": u"海水盐度观测精度"}
        self.Rdefdic = {u"dbar": u"urn:ogc:def:property:presMeasurementResolution",
                        u"degC": u"urn:ogc:def:property:tempMeasurementResolution",
                        u"psu": u"urn:ogc:def:property:cndcMeasurementResolution"}
        self.RMSdefdic = {u"dbar": u"urn:ogc:def:property:presMeasurementRMS",
                          u"degC": u"urn:ogc:def:property:tempMeasurementRMS",
                          u"psu": u"urn:ogc:def:property:cndcMeasurementRMS"}
        self.ioputdic = {u"dbar": u"观测深度", u"degC": u"海水温度", u"psu": u"海水盐度"}
        self.iodefdic = {u"dbar": u"urn:ogc:def:property:OGC:1.0:argoFloatObservationDepth",
                         u"degC": u"urn:ogc:def:property:OGC:1.0:argoFloatZtmp",
                         u"psu": u"urn:ogc:def:property:OGC:1.0:argoFloatZsal"}

    def __unicode(self, stringtmp):
        if type(stringtmp) is not unicode:
            stringtmp = stringtmp.decode('utf-8')
        return stringtmp

    def __setResolution(self, uomCode, value):
        '''根据uomCode插入观测分辨率'''
        uomCode = self.__unicode(uomCode)
        path = u"/ns:SensorML/sml:member/sml:System/sml:capabilities/swe:DataRecord"
        root = self.sensorXml.xpath(path, namespaces=sensorNS)[0]
        valueele = etree.Element(swe + "value", nsmap=sensorNS)
        valueele.text = str(value)
        uomele = etree.Element(swe + "uom", nsmap=sensorNS)
        uomele.set("code", uomCode)
        quantityele = etree.Element(swe + "Quantity", nsmap=sensorNS)
        quantityele.set("definition", self.Rdefdic[uomCode])
        quantityele.append(uomele)
        quantityele.append(valueele)
        fieldele = etree.Element(swe + "field", nsmap=sensorNS)
        fieldele.set("name", self.Rnamedic[uomCode])
        fieldele.append(quantityele)
        root.append(fieldele)

    def __setRMS(self, uomCode, value):
        '''根据uomCode插入观测精度'''
        uomCode = self.__unicode(uomCode)
        path = u"/ns:SensorML/sml:member/sml:System/sml:capabilities/swe:DataRecord"
        root = self.sensorXml.xpath(path, namespaces=sensorNS)[0]
        valueele = etree.Element(swe + "value", nsmap=sensorNS)
        valueele.text = str(value)
        uomele = etree.Element(swe + "uom", nsmap=sensorNS)
        uomele.set("code", uomCode)
        quantityele = etree.Element(swe + "Quantity", nsmap=sensorNS)
        quantityele.set("definition", self.RMSdefdic[uomCode])
        quantityele.append(uomele)
        quantityele.append(valueele)
        fieldele = etree.Element(swe + "field", nsmap=sensorNS)
        fieldele.set("name", self.RMSnamedic[uomCode])
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

    def setKeywords(self, sensorName, stationName):
        '''根据sensorName改变keyword'''
        if type(sensorName) is not unicode:
            sensorName = sensorName.decode('utf-8')
        path = "/ns:SensorML/sml:member/sml:System/sml:keywords/sml:KeywordList/sml:keyword"
        keyword = self.sensorXml.xpath(path, namespaces=sensorNS)
        keyword[3].text = sensorName
        keyword[5].text = stationName

    def setIdentifier(self, stationName, stationCode, sensorName, serialNumber, maker):
        '''根据平台Name,平台Code,传感器Name生成标识码'''
        if type(stationName) is not unicode:
            stationName = stationName.decode('utf-8')
        if type(stationCode) is not unicode:
            stationCode = stationCode.decode('utf-8')
        if type(sensorName) is not unicode:
            sensorName = sensorName.decode('utf-8')
        if type(maker) is not unicode:
            maker = maker.decode('utf-8')

        path = "/ns:SensorML/sml:member/sml:System/sml:identification/sml:IdentifierList/sml:identifier/s" \
               "ml:Term/sml:value"
        identifier = self.sensorXml.xpath(path, namespaces=sensorNS)

        identifier[
            0].text = u"urn:liesmars:insitusensor:ArgoFloat-" + stationName + u"-" + stationCode + u"-" + sensorName
        identifier[1].text = sensorName
        identifier[2].text = sensorName
        identifier[3].text = stationName
        identifier[
            4].text = u"urn:liesmars:insitusensor:platform:ArgoFloat-" + stationName + u"-" + stationCode
        identifier[5].text = serialNumber
        identifier[6].text = maker

    def setValidtime(self, time):
        '''更具平台时间设置validtime'''
        if type(time) is not unicode:
            time = time.decode('utf-8')
        path = u"/ns:SensorML/sml:member/sml:System/sml:validTime/gml:TimePeriod/gml:beginPosition"
        validtime = self.sensorXml.xpath(path, namespaces=sensorNS)
        validtime[0].text = time

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
        namevalue = u"ArgoFloat-" + stationName + u"-" + stationCode + u"-" + sensorName + u"_SOS"
        interfaceName[0].set("name", namevalue)

        path = u"/ns:SensorML/sml:member/sml:System/sml:interfaces/sml:InterfaceList/sml:interface" \
               u"/sml:InterfaceDefinition/sml:serviceLayer/swe:DataRecord/swe:field[3]/swe:Text/swe:value"
        interfaceValue = self.sensorXml.xpath(path, namespaces=sensorNS)
        interfaceValue[
            0].text = u"urn:liesmars:insitusensor:ArgoFloat-" + stationName + u"-" + stationCode + u"-" + sensorName

    def __setInput(self, uomCode):
        '''根据uomCode设置输入,与setQuantity对应'''
        uomCode = self.__unicode(uomCode)
        path = u"/ns:SensorML/sml:member/sml:System/sml:inputs/sml:InputList"
        root = self.sensorXml.xpath(path, namespaces=sensorNS)[0]
        observablePropertyele = etree.Element(swe + "ObservableProperty", nsmap=sensorNS)
        observablePropertyele.set("definition", self.iodefdic[uomCode])
        inputele = etree.Element(sml + "input", nsmap=sensorNS)
        inputele.set("name", self.ioputdic[uomCode])
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
        uomele.set("code", uomCode)

        quantityele = etree.Element(swe + "Quantity", nsmap=sensorNS)
        quantityele.set("definition", self.iodefdic[uomCode])
        quantityele.append(metaDataPropertyele)
        quantityele.append(uomele)

        outputele = etree.Element(sml + "output", nsmap=sensorNS)
        outputele.set("name", self.ioputdic[uomCode])
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

    def setDescription(self, stationName, stationCode,Description, project):
        '''根据sensorName改变浮标的description内容'''
        stationName = self.__unicode(stationName)
        stationCode=self.__unicode(stationCode)
        Description = self.__unicode(Description)
        project = self.__unicode(project)
        path = "/ns:SensorML/sml:member/sml:System/gml:description"
        description = self.stationXml.xpath(path, namespaces=sensorNS)
        description[0].text = u"Argo是“全球海洋观测业务系统计划(GOOS)”中的一个针对深海区温盐结构观测的子计" \
                              u"划。" + stationName +u" "+stationCode+ u"是" + Description + u",即" + project + u"项" \
                               u"目中采用自动剖面观测" \
                               u"海水温、盐度的漂流设备，对于研究全球海洋的温度、盐度、环流及其它们的变化情况。"

    def setKeywords(self, stationName,stationCode):
        stationCode = self.__unicode(stationCode)
        stationName = self.__unicode(stationName)
        path = u"/ns:SensorML/sml:member/sml:System/sml:keywords/sml:KeywordList/sml:keyword"
        keywords = self.stationXml.xpath(path, namespaces=sensorNS)
        keywords[2].text = stationName+u" "+stationCode

    def setIdentifier(self, stationName, stationCode):
        stationName = self.__unicode(stationName)
        stationCode = self.__unicode(stationCode)
        path = u"/ns:SensorML/sml:member/sml:System/sml:identification/sml:IdentifierList/sml:identifier" \
               u"/sml:Term/sml:value"
        identifier = self.stationXml.xpath(path, namespaces=sensorNS)
        identifier[0].text = u"urn:liesmars:insitusensor:platform:ArgoFloat" \
                             u"-" + stationName.replace(u" ",u"-") +u"-" + stationCode
        identifier[1].text = stationName+u" "+stationCode+u"剖面浮标"
        identifier[2].text = stationName+u" "+stationCode
        identifier[3].text = stationCode

    def __setSensorname(self, sensorname,sensorCode):
        sensorname = self.__unicode(sensorname)
        sensorCode = self.__unicode(sensorCode)
        path = u"/ns:SensorML/sml:member/sml:System/sml:identification/sml:IdentifierList"
        root = self.stationXml.xpath(path, namespaces=sensorNS)[0]

        valueele = etree.Element(sml + "value", nsmap=sensorNS)
        valueele.text = sensorname+u"-"+sensorCode

        termele = etree.Element(sml + "Term", nsmap=sensorNS)
        termele.set("definition", u"urn:ogc:def:identifier:OGC:1.0:associatedSensorName")
        termele.append(valueele)

        identifierele = etree.Element(sml + "identifier", nsmap=sensorNS)
        identifierele.set("name", u"搭载传感器名称")
        identifierele.append(termele)

        root.append(identifierele)

    def __setSensorid(self, stationName, stationCode, sensorName,sensorCode):
        stationName = self.__unicode(stationName)
        stationCode = self.__unicode(stationCode)
        sensorName = self.__unicode(sensorName)
        sensorCode = self.__unicode(sensorCode)

        path = u"/ns:SensorML/sml:member/sml:System/sml:identification/sml:IdentifierList"
        root = self.stationXml.xpath(path, namespaces=sensorNS)[0]

        valueele = etree.Element(sml + "value", nsmap=sensorNS)
        valueele.text = u"urn:liesmars:insitusensor:ArgoFloat-" \
                        u"" + stationName.replace(u" ",u"-") + u"-" + stationCode + u"-" + sensorName+u"-"+sensorCode

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

        for (sensorName,sensorCode) in sensorlist:
            self.__setSensorname(sensorName,sensorCode)
            self.__setSensorid(stationName, stationCode, sensorName,sensorCode)

    def setValidtime(self, time):
        '''更具平台时间设置validtime'''
        if type(time) is not unicode:
            time = time.decode('utf-8')
        path = u"/ns:SensorML/sml:member/sml:System/sml:validTime/gml:TimePeriod/gml:beginPosition"
        validtime = self.stationXml.xpath(path, namespaces=sensorNS)
        validtime[0].text = time

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
        namevalue = u"ArgoFloat-" + stationName.replace(u" ",u"-") + u"-" + stationCode + u"_SOS"
        interfaceName[0].set("name", namevalue)

        path = u"/ns:SensorML/sml:member/sml:System/sml:interfaces/sml:InterfaceList/sml:interface" \
               u"/sml:InterfaceDefinition/sml:serviceLayer/swe:DataRecord/swe:field[3]/swe:Text/swe:value"
        interfaceValue = self.stationXml.xpath(path, namespaces=sensorNS)
        interfaceValue[
            0].text = u"urn:liesmars:insitusensor:platform:ArgoFloat-" + stationName.replace(u" ",u"-") + u"-" + stationCode

    def setComponent(self, stationName, stationCode, sensorlist):
        stationName = self.__unicode(stationName)
        stationCode = self.__unicode(stationCode)
        sensorlist = [(self.__unicode(i),self.__unicode(j)) for i,j in sensorlist]

        path = u"/ns:SensorML/sml:member/sml:System/sml:components/sml:ComponentList"
        root = self.stationXml.xpath(path, namespaces=sensorNS)[0]

        for (sensorName,sensorCode) in sensorlist:
            componentele = etree.Element(sml + "component", nsmap=sensorNS)
            componentele.set("name", sensorName+u"-"+sensorCode)
            href = u"urn:liesmars:insitusensor:ArgoFloat" \
                   u"-" + stationName.replace(u" ",u"-") + u"-" + stationCode + u"-" + sensorName+u"-"+sensorCode
            componentele.set(xlink + "href", href)
            root.append(componentele)

    def toString(self):
        '''把浮标DOM变成字符串,编码格式为utf-8'''
        return etree.tostring(self.stationXml, encoding='utf-8', pretty_print=True)


# floatsensor = sensor(r"F:\PythonLearning\resource\Argo_sensor1.xml")
# floatsensor.setDescription("SBE41".decode('utf-8'))
# floatsensor.setKeywords("SBE41".decode('utf-8'), "ARVOR-5870")
# floatsensor.setIdentifier("ARVOR-5870", "48555", "SBE41", "1835", "SBE")
# floatsensor.setValidtime("2014-08-05T00:00:00.0Z")
# floatsensor.setQuantity("dbar".decode('utf-8'), 0, 0)
# floatsensor.setOrg("Naval Oceanographic Office (NAVO)")
# floatsensor.setInterface("ARVOR-5870", "48555", "SBE41")
# floatsensor.setIOput("dbar")


floatstation = station(r"F:\PythonLearning\resource\Argo_station1.xml")
floatstation.setDescription("APEX-Profiling-Float", "Argo METRI/KMA, Republic of Korea", "Argo KORDI")
floatstation.setIdentifier("APEX-Profiling-Float", "2900452")
floatstation.setKeywords("APEX-Profiling-Float")
loadsensorlist = ["SBE-CP-41", "SBE41CP", "sbe-41"]
floatstation.setLoadsensors("APEX-Profiling-Float", "2900452", loadsensorlist)
floatstation.setComponent("APEX-Profiling-Float", "2900452", loadsensorlist)
floatstation.setValidtime("2004-10-18T00:39:28.0Z")
floatstation.setCategory("APEX-Profiling-Float")
floatstation.setOrg("Korea Meteorological Administration (KMA)")
floatstation.setInterface("APEX-Profiling-Float", "2900452")

fout = open(r"F:\PythonLearning\resource\teststation.xml", 'w')
fout.write(floatstation.toString())
fout.close()
