#encoding=utf-8
import mimetypes
from datetime import datetime


class GetDocuments(object):
    def __init__(self, doc_class, object_ids, search_by, compose_doc_name, rep):
        self.doc_class = doc_class
        self.object_ids = object_ids
        self.search_by = search_by
        self.compose_doc_name = compose_doc_name
        self.rep = rep


        #self.__startDownload()

    def getContentWithQuery(self):
        queries = []
        for object_id in self.object_ids:
            queries.append("select * from %s where %s='%s'"%(self.doc_class,
                                                      self.search_by,
                                                      object_id.strip('\r')))
        results = [self.rep.query(q).getResults() for q in queries]            
        self.__saveContent(results)


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

    def getFileNetDocs(self):
        """Method that downloads files from repository and saves them
        locally.
        """
        docs = None
        for i in self.Ids:
            downlodedfile = ''
            try:
                docs = self.rep.getObject(i)
                props = docs.properties
                if props['cmis:objectTypeId'] != self.doc_class:
                    raise Exception('Informed class: %s is different \
                                    from the Document Class: %s' %(
                                        self.doc_class, props['cmis:objectTypeId']))
                    self.errors[i] = 'Informed class: %s is different from \
                            the Document Class: %s'%(self.doc_class, 
                                                     props['cmis:objectTypeId'])
                extension = docs.name.split('.')[-1]
                for propertyname in self.compose_doc_names:
                    downlodedfile += str(props[propertyname])+'-'
                downlodedfile += datetime.now().isoformat()[-6:-3]+'.'+extension
                downlodedfile = downlodedfile.replace('/','-')

                f = open(downlodedfile,'wb')
                f.write(docs.getContentStream().read())
                f.close()

            except Exception as e:
                print("Error >>> %s"%str(e))
                self.errors[i] = str(e)

    def __saveContent(self, results):
        for result in results:
            for res in result:
                doc_name = self.__createDocName(res)
                f = open(doc_name, 'wb')
                f.write(res.getContentStream().read())
                f.close()

    def __createDocName(self, content):
        props = content.properties
        doc_name = ('-').join([str(props[doc.strip(' ')]) for doc in self.compose_doc_name])
        doc_name.strip('.')
        extension = content.name.split('.')[-1] 
        doc_name += content.id[-13:]
        doc_name += '.'+extension

        return doc_name


