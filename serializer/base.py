from typing import List
from google.cloud.firestore import DocumentReference
from itertools import starmap


class BaseSerializer:

    def __init__(self, object: List[DocumentReference] | DocumentReference):
        self.object = object

    @property
    def data(self):
        fields = self.Meta.fields
        
        if isinstance(self.object, list):
            docs = self.object
            to_dict = lambda doc: {"id": doc.id, **doc.to_dict()}
            datas = list(map(to_dict, docs))

            def filter_list_data(data: dict):
                filter_field = lambda field, value: (field, value) if field in fields else None
                filter_data = list(filter(None, list(starmap(filter_field, data.items()))))
                return dict(filter_data)

            filter_datas = list(map(filter_list_data, datas))
            return filter_datas

        doc = self.object
        data = {"id": doc.id, **doc.to_dict()}

        filter_field = lambda field, value: (field, value) if field in fields else None
        filter_data = list(filter(None, list(starmap(filter_field, data.items()))))
        return dict(filter_data)

    
        

