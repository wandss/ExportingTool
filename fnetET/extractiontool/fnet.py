#encoding=utf-8

class Conecta(object):
    @staticmethod
    def cmisConnect(server_address, user, passwd):
        """Returns a repository CmisLib object
        """
        try:
            from cmislib.model import CmisClient
            client = CmisClient(server_address, user, passwd)
            rep = client.defaultRepository
            return(rep)
        except Exception as e:
            print ('Exception>>>> '+str(e))
            return (str(e))

class Fnet(object):

    """Class to handle FileNet.
    """
    def __init__(self, server_address, username, passwd):
        """Connects to the repository and has methods: getFnetClasses,
        getClass and removeSystemProperties.
        """
        self.rep = Conecta.cmisConnect(server_address, username, passwd)
        self.classes = []
        self.systemclasses = ['WorkflowDefinition',
                            'XMLPropertyMappingScript',
                            'CodeModule',
                            'ScenarioDefinition', 'Simulation',
                            'PreferencesDocument','Email',
                            'FormData', 'FormTemplate',
                            'WebFormTemplate','FormPolicy',
                            'EntryTemplate', 'RecordsTemplate',
                            'WebContentTemplate','StoredSearch',
                            'cmis:folder','ClbTeamspace',
                            'ClbTeamspaceTemplate','PreferencesFolder',
                            'FormProxyFolder', 'PublishTemplate']
        self.systemprops = ['cmis:','MajorVersionNumber',
                            'StorageLocation',
                            'DateContentLastAccessed',
                            'ReservationType', 'CmRetentionDate',
                            'ContentElementsPresent',
                            'IsInExceptionState',
                            'EntryTemplateLaunchedWorkflowNumber',
                            'SecurityFolder', 'CurrentState',
                            'VersionStatus', 'DocumentLifecyclePolicy',
                            'CmIsMarkedForDeletion','OwnerDocument',
                            'IsVersioningEnabled','LockTimeout',
                            'IgnoreRedirect',
                            'EntryTemplateObjectStoreName',
                            'PublishingSubsidiaryFolder','Reservation',
                            'ClassificationStatus','LockOwner',
                            'LockToken','EntryTemplateId','This',
                            'IndexationId','CmIndexingFailureCode',
                            'CurrentVersion','PublicationInfo',
                            'ReleasedVersion','ContentRetentionDate',
                            'SecurityParent','CompoundDocumentState',
                            'DateCheckedIn','NumeroDePaginas',
                            'ComponentBindingLabel','StorageArea',
                            'StoragePolicy','Owner',
                            'MinorVersionNumber','IsReserved']

    def getFnetClasses(self):
        """Method that returns a list object with FileNet custom Classes
        objects, ordered by localName Property.
        The systemclasses declared on self.systemclasses will be excluded.
        """
        classes = [fnclass for fnclass in self.rep.getTypeDescendants()
            if fnclass.id not in self.systemclasses]
        ordered_names = [class_name.localName for class_name in classes]
        ordered_names.sort()
        self.classes = [class_object for name in ordered_names 
                       for class_object in classes 
                        if class_object.localName == name]
        return self.classes

    def getClass(self, fnclass_name):
        """Returns a cmislib.model Object for a
        given FileNet Class.
        """
        if not self.classes:
            self.classes = [fnclass for fnclass in
                self.rep.getTypeDescendants()
                if fnclass.id
                not in self.systemclasses]
        fnclass = [fnclass for fnclass in self.classes
                    if fnclass_name in fnclass.id]
        if fnclass:
            return fnclass[0]
        else:
            return None

    def removeSystemProperties(self, properties):
        """Remove system properties from class
        and returns a list of properties assotiated with class.
        Expects a dictionary from "myclass.properties", a cmis.lib
        object type.
        """
        properties = [props for props in properties
                    if props not in self.systemprops]
        properties = [prop for prop in properties
                    if not prop.startswith('cmis')]
        properties.sort()
        return properties
