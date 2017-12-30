xmls = {
    'preDo': '''<?xml version="1.0" encoding="utf-8"?>
                <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                  <soap:Body>
                    <loginverifystudent_B xmlns="http://murpcn.com/murpwebservice/">
                      <loginname>2015118140</loginname>
                      <loginpass>2015118140</loginpass>
                      <tec>string</tec>
                      <logininfo>string</logininfo>
                      <strbak>string</strbak>
                    </loginverifystudent_B>
                  </soap:Body>
                </soap:Envelope>
                ''',

    'getAllGrade': '<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><GetMyGrades xmlns="http://murpcn.com/murpwebservice/"><umcid>80213</umcid></GetMyGrades></soap:Body></soap:Envelope>',

    'getTermGrage': '''<?xml version="1.0" encoding="utf-8"?>
                        <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                          <soap:Body>
                            <Mark xmlns="http://murpcn.com/murpwebservice/">
                              <umcid>80213</umcid>
                            </Mark>
                          </soap:Body>
                        </soap:Envelope>
                        '''
}