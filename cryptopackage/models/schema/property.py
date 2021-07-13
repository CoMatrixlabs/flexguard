# Copyright Contributors to the Amundsen project.
# SPDX-License-Identifier: Apache-2.0

from typing import (
    Iterator, List, Optional, Union,
)

from cryptopackage.models import RDSModel
from cryptopackage.models.badge import Badge as RDSBadge

##WIP 

class Property:
    def __init__(self, name: str, category: str):
        # Amundsen UI always formats badge display with first letter capitalized while other letters are lowercase.
        # Clicking table badges in UI always results in searching lower cases badges
        # https://github.com/amundsen-io/amundsen/blob/6ec9b398634264e52089bb9e1b7d76a6fb6a35a4/frontend/amundsen_application/static/js/components/BadgeList/index.tsx#L56
        # If badges stored in neo4j are not lowercase, they won't be searchable in UI.
        self.name = name.lower()
        self.category = category.lower()

    def __repr__(self) -> str:
        return f'Property({self.name!r}, {self.category!r})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Property):
            return NotImplemented
        return self.name == other.name and \
            self.category == other.category


class PropertyMetadata:
    """
    Property model.
    """
    PROPERTY_NODE_LABEL = 'Property'
    PROPERTY_KEY_FORMAT = '{property}'
    PROPERTY_CATEGORY = 'category'

    # Relation between entity and badge
    PROPERTY_RELATION_TYPE = 'HAS_PROPERTY'
    INVERSE_BADGE_RELATION_TYPE = 'PROPERTY_FOR'

    LABELS_PERMITTED_TO_HAVE_PROPERTY = ['DATASET','TABLE', 'MODEL', 'COLUMN', 'FEATURE']

    def __init__(self,
                 start_label: str,
                 start_key: str,
                 properties: List[Property],
                 ):
        if start_label not in PropertyMetadata.LABELS_PERMITTED_TO_HAVE_BADGE:
            raise Exception(f'badges for {start_label} are not supported')
        self.start_label = start_label
        self.start_key = start_key
        self.properties = properties

        self._node_iter = self._create_node_iterator()
        self._relation_iter = self._create_relation_iterator()
        self._record_iter = self._create_record_iterator()

    def __repr__(self) -> str:
        return f'PropertyMetadata({self.start_label!r}, {self.start_key!r}, {self.badges!r})'

    
    def create_next_record(self) -> Union[RDSModel, None]:
        try:
            return next(self._record_iter)
        except StopIteration:
            return None

    @staticmethod
    def get_property_key(name: str) -> str:
        if not name:
            return ''
        return PropertyMetadata.PROPERTY_KEY_FORMAT.format(property=name)

    def get_property_records(self) -> List[RDSModel]:
        records = []
        for property in self.properties:
            if property:
                record = DSProperty(
                    rk=self.get_property_key(property.name),
                    category=property.category
                )
                records.append(record)

        return records

    def _create_record_iterator(self) -> Iterator[RDSModel]:
        records = self.get_badge_records()
        for record in records:
            yield record