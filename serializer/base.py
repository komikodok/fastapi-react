from typing import List
from google.cloud.firestore import DocumentSnapshot
from itertools import starmap


class BaseSerializer:

    def __init__(self, doc_snaps: List[DocumentSnapshot] | DocumentSnapshot):
        self.doc_snaps = doc_snaps

    @property
    def data(self):        
        if isinstance(self.doc_snaps, list):
            docs = self.doc_snaps
            to_dict = lambda doc: {"id": doc.id, **doc.to_dict()}
            datas = list(map(to_dict, docs))

            filter_datas = list(map(self.filter_data_by_field, datas))
            return filter_datas

        doc = self.doc_snaps
        data = {"id": doc.id, **doc.to_dict()}

        filter_data = self.filter_data_by_field(data)
        return filter_data
    
    def filter_data_by_field(self, data: dict):
        fields = self.Meta.fields

        filter_field = lambda field, value: (field, value) if field in fields else None
        filter_data = list(filter(None, list(starmap(filter_field, data.items()))))
        return dict(filter_data)