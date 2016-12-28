#encoding=utf-8
from datetime import datetime

class GetDocuments(object):
    def __init__(self, filenames, rep, ids, doc_class):
        self.filenames = filenames
        self.rep = rep
        self.errors = {}
        self.ids = ids
        self.doc_class = doc_class
        self.__startDownload()

    def __startDownload(self):
        """This method creates a list with document IDs whether
        retrieved from the Repository's Data Base or directly by inspecting
        the properties from documents.
        """
        product_name = self.rep.info.get('productName')
        self.Ids = []
        for i in self.ids:
            if i[9:10]=='-' or i[8:9]=='-':
                if i.startswith('{') or i.endswith('}'):
                    if i.startswith('{'):
                        self.Ids.append('idd_'+i[1:])
                    elif i.endswith('}'):
                        self.Ids.append('idd_'+i[:-1])
                    elif i.startswith('{') and i.endswith('}'):
                        self.Ids.append('idd_'+i[1:-1])
                else:
                    if 'Alfresco' in product_name:
                       self.Ids.append(i)
                    else:
                        self.Ids.append('idd_'+i)
            else:
                if 'Alfresco' in product_name:
                    self.Ids.append(i)
                else:
                    self.Ids.append('idd_'+i[6:8]+i[4:6]+i[2:4]+i[0:2]+'-'+i[10:12]+i[8:10]+'-'+i[14:16]+i[12:14]+'-'+i[16:20]+'-'+i[20:32])

        self.__getFileNetDocs()

    def __getFileNetDocs(self):
        """Method that download files from repository and saves them
        locally.
        """
        docs = None
        for i in self.Ids:
            downlodedfile = ''
            try:
                docs = self.rep.getObject(i)
                props = docs.properties
                if props['cmis:objectTypeId'] != self.doc_class:
                    raise Exception('Informed class: %s is different from the Document Class: %s' %(
                        self.doc_class, props['cmis:objectTypeId']))
                    self.errors[i] = 'Informed class: %s is different from the Document Class: %s'%(
                        self.doc_class, props['cmis:objectTypeId'])
                extension = docs.name.split('.')[-1]
                for propertyname in self.filenames:
                    downlodedfile += str(props[propertyname])+'-'
                downlodedfile += datetime.now().isoformat()[-6:-3]+'.'+extension
                downlodedfile = downlodedfile.replace('/','-')

                f = open(downlodedfile,'wb')
                f.write(docs.getContentStream().read())
                f.close()

            except Exception as e:
                print("Error >>> %s"%str(e))
                self.errors[i] = str(e)