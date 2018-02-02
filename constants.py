from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import six
from prov.identifier import Namespace

__author__ = 'Trung Dong Huynh'
__email__ = 'trungdong@donggiang.com'


XSD = Namespace('xsd', 'http://www.w3.org/2001/XMLSchema#/')
PROV = Namespace('prov', 'http://www.w3.org/ns/prov#/')
DLC = Namespace('dlc','https://purl.org/eudat/dlc/')
XSI = Namespace('xsi', 'http://www.w3.org/2001/XMLSchema-instance')
#RDFS = Namespace()

#  C1. Entities/Activities
PROV_ENTITY = PROV['Entity']
PROV_ACTIVITY = PROV['Activity']
PROV_GENERATION = PROV['Generation']
DLC_GENERATION = DLC['Generation']
PROV_USAGE = PROV['Usage']
DLC_USAGE = DLC['DlcUsage']
PROV_COMMUNICATION = PROV['Communication']
DLC_COMMUNICATION = DLC['Communication']
PROV_START = PROV['Start']
PROV_END = PROV['End']
PROV_INVALIDATION = PROV['Invalidation']
DLC_INVALIDATION = DLC['DlcInvalidation']
PROV_PARTITION = PROV['partition']
DLC_PARTITION = DLC['partition']
#  C2. Derivations
PROV_DERIVATION = PROV['Derivation']
DLC_DERIVATION =  DLC['DlcDerivation']

#  C3. Agents/Responsibility
PROV_AGENT = PROV['Agent']
PROV_ATTRIBUTION = PROV['Attribution']
DLC_ATTRIBUTION = DLC['Attribution']
PROV_ASSOCIATION = PROV['Association']
DLC_ASSOCIATION = DLC['DlcAssociation']
PROV_DELEGATION = PROV['Delegation']
DLC_DELEGATION = DLC['DlcDelegation']
PROV_INFLUENCE = PROV['Influence']
#  C4. Bundles
PROV_BUNDLE = PROV['Bundle']
#  C5. Alternate
PROV_ALTERNATE = PROV['Alternate']
PROV_SPECIALIZATION = PROV['Specialization']
PROV_MENTION = PROV['Mention']
#  C6. Collections
PROV_MEMBERSHIP = PROV['Membership']
DLC_MEMBERSHIP = DLC['DlcMembership']

PROV_N_MAP = {
    PROV_ENTITY:               u'entity',
    PROV_ACTIVITY:             u'activity',
    PROV_GENERATION:           u'wasGeneratedBy',
    DLC_GENERATION:            u'willBeGeneratedBy',
    PROV_USAGE:                u'used',
    DLC_USAGE:                 u'willUse',
    PROV_COMMUNICATION:        u'wasInformedBy',
    DLC_COMMUNICATION:         u'willBeInformedBy',
    PROV_START:                u'wasStartedBy',
    PROV_END:                  u'wasEndedBy',
    PROV_INVALIDATION:         u'wasInvalidatedBy',
    DLC_INVALIDATION:          u'willBeInvalidatedBy',
    PROV_DERIVATION:           u'wasDerivedFrom',
    DLC_DERIVATION:            u'willBeDerivedFrom',
    PROV_AGENT:                u'agent',
    PROV_ATTRIBUTION:          u'wasAttributedTo',
    DLC_ATTRIBUTION:           u'willBeAttributedTo',
    PROV_ASSOCIATION:          u'wasAssociatedWith',
    DLC_ASSOCIATION:           u'willBeAssociatedWith',
    PROV_DELEGATION:           u'actedOnBehalfOf',
    DLC_DELEGATION:            u'willActOnBehalfOf',
    PROV_INFLUENCE:            u'wasInfluencedBy',
    PROV_ALTERNATE:            u'alternateOf',
    PROV_SPECIALIZATION:       u'specializationOf',
    PROV_MENTION:              u'mentionOf',
    PROV_MEMBERSHIP:           u'hadMember',
    DLC_MEMBERSHIP:            u'willHaveMember',
    PROV_BUNDLE:               u'bundle',
    PROV_PARTITION:            u'wasPartOf',
    DLC_PARTITION:             u'willBePartOf',
}

# Records defined as subtypes in PROV-N but top level types in for example
# PROV XML also need a mapping.
ADDITIONAL_N_MAP = {
    PROV['Revision']:          u'wasRevisionOf',
    PROV['Quotation']:         u'wasQuotedFrom',
    PROV['PrimarySource']:     u'hadPrimarySource',
    PROV['SoftwareAgent']:      u'softwareAgent',
    PROV['Person']:            u'person',
    PROV['Pdb_file']:          u'pdb_file',
    PROV['mmCIF']:             u'mmCIF_file',
    PROV['Organization']:      u'organization',
    PROV['Plan']:              u'plan',
    PROV['Collection']:        u'collection',
    PROV['EmptyCollection']:   u'emptyCollection',
}

# Maps qualified names from the PROV namespace to their base class. If it
# has no baseclass it maps to itsself. This is needed for example for PROV
# XML (de)serializer where extended types are used a lot.
PROV_BASE_CLS = {
    PROV_ENTITY:               PROV_ENTITY,
    PROV_ACTIVITY:             PROV_ACTIVITY,
    PROV_GENERATION:           PROV_GENERATION,
    DLC_GENERATION:            DLC_GENERATION,
    PROV_USAGE:                PROV_USAGE,
    DLC_USAGE:                 DLC_USAGE,
    PROV_COMMUNICATION:        PROV_COMMUNICATION,
    DLC_COMMUNICATION:         DLC_COMMUNICATION,
    PROV_START:                PROV_START,
    PROV_END:                  PROV_END,
    PROV_INVALIDATION:         PROV_INVALIDATION,
    DLC_INVALIDATION:          DLC_INVALIDATION,
    PROV_DERIVATION:           PROV_DERIVATION,
    DLC_DERIVATION:            DLC_DERIVATION,
    PROV_PARTITION:            PROV_PARTITION,
    DLC_PARTITION:             DLC_PARTITION,
    PROV['Revision']:          PROV_DERIVATION,
    PROV['Quotation']:         PROV_DERIVATION,
    PROV['PrimarySource']:     PROV_DERIVATION,
    PROV_AGENT:                PROV_AGENT,
    PROV['SoftwareAgent']:      PROV_AGENT,
    PROV['Person']:            PROV_AGENT,
    PROV['Organization']:      PROV_AGENT,
    PROV_ATTRIBUTION:          PROV_ATTRIBUTION,
    DLC_ATTRIBUTION:           DLC_ATTRIBUTION,
    PROV_ASSOCIATION:          PROV_ASSOCIATION,
    DLC_ASSOCIATION:           DLC_ASSOCIATION,
    PROV['Plan']:              PROV_ENTITY,
    PROV_DELEGATION:           PROV_DELEGATION,
    PROV_INFLUENCE:            PROV_INFLUENCE,
    PROV_ALTERNATE:            PROV_ALTERNATE,
    PROV_SPECIALIZATION:       PROV_SPECIALIZATION,
    PROV_MENTION:              PROV_MENTION,
    PROV['Collection']:        PROV_ENTITY,
    PROV['EmptyCollection']:   PROV_ENTITY,
    PROV_MEMBERSHIP:           PROV_MEMBERSHIP,
    DLC_MEMBERSHIP:            DLC_MEMBERSHIP,
    PROV_BUNDLE:               PROV_ENTITY
}

# Identifiers for PROV's attributes
PROV_ATTR_ENTITY = PROV['entity']
PROV_ATTR_ACTIVITY = PROV['activity']
PROV_ATTR_TRIGGER = PROV['trigger']
PROV_ATTR_INFORMED = PROV['informed']
PROV_ATTR_INFORMANT = PROV['informant']
PROV_ATTR_STARTER = PROV['starter']
PROV_ATTR_ENDER = PROV['ender']
PROV_ATTR_AGENT = PROV['agent']
PROV_ATTR_PLAN = PROV['plan']
PROV_ATTR_DELEGATE = PROV['delegate']
PROV_ATTR_RESPONSIBLE = PROV['responsible']
PROV_ATTR_GENERATED_ENTITY = PROV['generatedEntity']
PROV_ATTR_USED_ENTITY = PROV['usedEntity']
PROV_ATTR_GENERATION = PROV['generation']
PROV_ATTR_USAGE = PROV['usage']
PROV_ATTR_SPECIFIC_ENTITY = PROV['specificEntity']
PROV_ATTR_GENERAL_ENTITY = PROV['generalEntity']
PROV_ATTR_ALTERNATE1 = PROV['alternate1']
PROV_ATTR_ALTERNATE2 = PROV['alternate2']
PROV_ATTR_BUNDLE = PROV['bundle']
PROV_ATTR_INFLUENCEE = PROV['influencee']
PROV_ATTR_INFLUENCER = PROV['influencer']
PROV_ATTR_COLLECTION = PROV['collection']

#  Literal properties
PROV_ATTR_TIME = PROV['time']
PROV_ATTR_STARTTIME = PROV['startTime']
PROV_ATTR_ENDTIME = PROV['endTime']


PROV_ATTRIBUTE_QNAMES = {
    PROV_ATTR_ENTITY,
    PROV_ATTR_ACTIVITY,
    PROV_ATTR_TRIGGER,
    PROV_ATTR_INFORMED,
    PROV_ATTR_INFORMANT,
    PROV_ATTR_STARTER,
    PROV_ATTR_ENDER,
    PROV_ATTR_AGENT,
    PROV_ATTR_PLAN,
    PROV_ATTR_DELEGATE,
    PROV_ATTR_RESPONSIBLE,
    PROV_ATTR_GENERATED_ENTITY,
    PROV_ATTR_USED_ENTITY,
    PROV_ATTR_GENERATION,
    PROV_ATTR_USAGE,
    PROV_ATTR_SPECIFIC_ENTITY,
    PROV_ATTR_GENERAL_ENTITY,
    PROV_ATTR_ALTERNATE1,
    PROV_ATTR_ALTERNATE2,
    PROV_ATTR_BUNDLE,
    PROV_ATTR_INFLUENCEE,
    PROV_ATTR_INFLUENCER,
    PROV_ATTR_COLLECTION
}
PROV_ATTRIBUTE_LITERALS = {
    PROV_ATTR_TIME, PROV_ATTR_STARTTIME, PROV_ATTR_ENDTIME
}

# Set of formal attributes of PROV records
PROV_ATTRIBUTES = PROV_ATTRIBUTE_QNAMES | PROV_ATTRIBUTE_LITERALS
PROV_RECORD_ATTRIBUTES = list((attr, six.text_type(attr)) for attr in
                              PROV_ATTRIBUTES)

PROV_RECORD_IDS_MAP = dict(
    (PROV_N_MAP[rec_type_id], rec_type_id) for rec_type_id in PROV_N_MAP
)
PROV_ID_ATTRIBUTES_MAP = dict(
    (prov_id, attribute) for (prov_id, attribute) in PROV_RECORD_ATTRIBUTES
)
PROV_ATTRIBUTES_ID_MAP = dict(
    (attribute, prov_id) for (prov_id, attribute) in PROV_RECORD_ATTRIBUTES
)

# Extra definition for convenience
PROV_TYPE = PROV['type']
PROV_LABEL = PROV['label']
PROV_VALUE = PROV['value']
PROV_LOCATION = PROV['location']
PROV_ROLE = PROV['role']

PROV_QUALIFIEDNAME = PROV['QUALIFIED_NAME']

# XSD DATA TYPES
XSD_ANYURI = XSD['anyURI']
XSD_QNAME = XSD['QName']
XSD_DATETIME = XSD['dateTime']
XSD_TIME = XSD['time']
XSD_DATE = XSD['date']
XSD_STRING = XSD['string']
XSD_BOOLEAN = XSD['boolean']
# All XSD Integer types
XSD_INTEGER = XSD['integer']
XSD_LONG = XSD['long']
XSD_INT = XSD['int']
XSD_SHORT = XSD['short']
XSD_BYTE = XSD['byte']
XSD_NONNEGATIVEINTEGER = XSD['nonNegativeInteger']
XSD_UNSIGNEDLONG = XSD['unsignedLong']
XSD_UNSIGNEDINT = XSD['unsignedInt']
XSD_UNSIGNEDSHORT = XSD['unsignedShort']
XSD_UNSIGNEDBYTE = XSD['unsignedByte']
XSD_POSITIVEINTEGER = XSD['positiveInteger']
XSD_NONPOSITIVEINTEGER = XSD['nonPositiveInteger']
XSD_NEGATIVEINTEGER = XSD['negativeInteger']
# All XSD real number types
XSD_FLOAT = XSD['float']
XSD_DOUBLE = XSD['double']
XSD_DECIMAL = XSD['decimal']
