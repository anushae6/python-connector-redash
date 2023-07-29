from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GFieldInfo(_message.Message):
    __slots__ = ["fieldName", "fieldType"]
    FIELDNAME_FIELD_NUMBER: _ClassVar[int]
    FIELDTYPE_FIELD_NUMBER: _ClassVar[int]
    fieldName: str
    fieldType: str
    def __init__(self, fieldName: _Optional[str] = ..., fieldType: _Optional[str] = ...) -> None: ...

class FailedSchemaElement(_message.Message):
    __slots__ = ["name", "type", "reason"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    reason: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class GetAddCatalogsResponse(_message.Message):
    __slots__ = ["status", "failures"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FAILURES_FIELD_NUMBER: _ClassVar[int]
    status: str
    failures: _containers.RepeatedCompositeFieldContainer[FailedSchemaElement]
    def __init__(self, status: _Optional[str] = ..., failures: _Optional[_Iterable[_Union[FailedSchemaElement, _Mapping]]] = ...) -> None: ...

class CatalogResponse(_message.Message):
    __slots__ = ["name", "isDefault"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ISDEFAULT_FIELD_NUMBER: _ClassVar[int]
    name: str
    isDefault: bool
    def __init__(self, name: _Optional[str] = ..., isDefault: bool = ...) -> None: ...

class ParameterValue(_message.Message):
    __slots__ = ["index", "type", "value"]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    index: int
    type: str
    value: str
    def __init__(self, index: _Optional[int] = ..., type: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class ClearRequest(_message.Message):
    __slots__ = ["engineIP", "sessionId", "queryId"]
    ENGINEIP_FIELD_NUMBER: _ClassVar[int]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    QUERYID_FIELD_NUMBER: _ClassVar[int]
    engineIP: str
    sessionId: str
    queryId: str
    def __init__(self, engineIP: _Optional[str] = ..., sessionId: _Optional[str] = ..., queryId: _Optional[str] = ...) -> None: ...

class ClearResponse(_message.Message):
    __slots__ = ["engineIP"]
    ENGINEIP_FIELD_NUMBER: _ClassVar[int]
    engineIP: str
    def __init__(self, engineIP: _Optional[str] = ...) -> None: ...

class CancelQueryRequest(_message.Message):
    __slots__ = ["engineIP", "sessionId", "queryId"]
    ENGINEIP_FIELD_NUMBER: _ClassVar[int]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    QUERYID_FIELD_NUMBER: _ClassVar[int]
    engineIP: str
    sessionId: str
    queryId: str
    def __init__(self, engineIP: _Optional[str] = ..., sessionId: _Optional[str] = ..., queryId: _Optional[str] = ...) -> None: ...

class CancelQueryResponse(_message.Message):
    __slots__ = ["engineIP"]
    ENGINEIP_FIELD_NUMBER: _ClassVar[int]
    engineIP: str
    def __init__(self, engineIP: _Optional[str] = ...) -> None: ...

class ExplainRequest(_message.Message):
    __slots__ = ["engineIP", "sessionId", "queryId"]
    ENGINEIP_FIELD_NUMBER: _ClassVar[int]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    QUERYID_FIELD_NUMBER: _ClassVar[int]
    engineIP: str
    sessionId: str
    queryId: str
    def __init__(self, engineIP: _Optional[str] = ..., sessionId: _Optional[str] = ..., queryId: _Optional[str] = ...) -> None: ...

class ExplainResponse(_message.Message):
    __slots__ = ["engineIP", "explain"]
    ENGINEIP_FIELD_NUMBER: _ClassVar[int]
    EXPLAIN_FIELD_NUMBER: _ClassVar[int]
    engineIP: str
    explain: str
    def __init__(self, engineIP: _Optional[str] = ..., explain: _Optional[str] = ...) -> None: ...

class DryRunRequest(_message.Message):
    __slots__ = ["engineIP", "sessionId", "schema", "queryString"]
    ENGINEIP_FIELD_NUMBER: _ClassVar[int]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    QUERYSTRING_FIELD_NUMBER: _ClassVar[int]
    engineIP: str
    sessionId: str
    schema: str
    queryString: str
    def __init__(self, engineIP: _Optional[str] = ..., sessionId: _Optional[str] = ..., schema: _Optional[str] = ..., queryString: _Optional[str] = ...) -> None: ...

class DryRunResponse(_message.Message):
    __slots__ = ["engineIP", "dryrunValue"]
    ENGINEIP_FIELD_NUMBER: _ClassVar[int]
    DRYRUNVALUE_FIELD_NUMBER: _ClassVar[int]
    engineIP: str
    dryrunValue: str
    def __init__(self, engineIP: _Optional[str] = ..., dryrunValue: _Optional[str] = ...) -> None: ...

class DryRunRequestV2(_message.Message):
    __slots__ = ["engineIP", "sessionId", "schema", "queryString", "catalog"]
    ENGINEIP_FIELD_NUMBER: _ClassVar[int]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    QUERYSTRING_FIELD_NUMBER: _ClassVar[int]
    CATALOG_FIELD_NUMBER: _ClassVar[int]
    engineIP: str
    sessionId: str
    schema: str
    queryString: str
    catalog: str
    def __init__(self, engineIP: _Optional[str] = ..., sessionId: _Optional[str] = ..., schema: _Optional[str] = ..., queryString: _Optional[str] = ..., catalog: _Optional[str] = ...) -> None: ...

class ExplainAnalyzeRequest(_message.Message):
    __slots__ = ["engineIP", "sessionId", "queryId"]
    ENGINEIP_FIELD_NUMBER: _ClassVar[int]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    QUERYID_FIELD_NUMBER: _ClassVar[int]
    engineIP: str
    sessionId: str
    queryId: str
    def __init__(self, engineIP: _Optional[str] = ..., sessionId: _Optional[str] = ..., queryId: _Optional[str] = ...) -> None: ...

class ExplainAnalyzeResponse(_message.Message):
    __slots__ = ["engineIP", "explainAnalyze"]
    ENGINEIP_FIELD_NUMBER: _ClassVar[int]
    EXPLAINANALYZE_FIELD_NUMBER: _ClassVar[int]
    engineIP: str
    explainAnalyze: str
    def __init__(self, engineIP: _Optional[str] = ..., explainAnalyze: _Optional[str] = ...) -> None: ...

class PrepareStatementRequest(_message.Message):
    __slots__ = ["engineIP", "sessionId", "schema", "queryString"]
    ENGINEIP_FIELD_NUMBER: _ClassVar[int]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    QUERYSTRING_FIELD_NUMBER: _ClassVar[int]
    engineIP: str
    sessionId: str
    schema: str
    queryString: str
    def __init__(self, engineIP: _Optional[str] = ..., sessionId: _Optional[str] = ..., schema: _Optional[str] = ..., queryString: _Optional[str] = ...) -> None: ...

class PrepareStatementV2Request(_message.Message):
    __slots__ = ["engineIP", "sessionId", "schema", "queryString", "catalog"]
    ENGINEIP_FIELD_NUMBER: _ClassVar[int]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    QUERYSTRING_FIELD_NUMBER: _ClassVar[int]
    CATALOG_FIELD_NUMBER: _ClassVar[int]
    engineIP: str
    sessionId: str
    schema: str
    queryString: str
    catalog: str
    def __init__(self, engineIP: _Optional[str] = ..., sessionId: _Optional[str] = ..., schema: _Optional[str] = ..., queryString: _Optional[str] = ..., catalog: _Optional[str] = ...) -> None: ...

class PrepareStatementResponse(_message.Message):
    __slots__ = ["engineIP", "queryId"]
    ENGINEIP_FIELD_NUMBER: _ClassVar[int]
    QUERYID_FIELD_NUMBER: _ClassVar[int]
    engineIP: str
    queryId: str
    def __init__(self, engineIP: _Optional[str] = ..., queryId: _Optional[str] = ...) -> None: ...

class UserAccessInfo(_message.Message):
    __slots__ = ["uuid", "userName", "tokens"]
    UUID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    userName: str
    tokens: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, uuid: _Optional[str] = ..., userName: _Optional[str] = ..., tokens: _Optional[_Iterable[str]] = ...) -> None: ...

class ExecuteStatementRequest(_message.Message):
    __slots__ = ["engineIP", "sessionId", "queryId"]
    ENGINEIP_FIELD_NUMBER: _ClassVar[int]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    QUERYID_FIELD_NUMBER: _ClassVar[int]
    engineIP: str
    sessionId: str
    queryId: str
    def __init__(self, engineIP: _Optional[str] = ..., sessionId: _Optional[str] = ..., queryId: _Optional[str] = ...) -> None: ...

class ExecuteStatementV2Request(_message.Message):
    __slots__ = ["engineIP", "sessionId", "queryId", "params"]
    ENGINEIP_FIELD_NUMBER: _ClassVar[int]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    QUERYID_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    engineIP: str
    sessionId: str
    queryId: str
    params: _containers.RepeatedCompositeFieldContainer[ParameterValue]
    def __init__(self, engineIP: _Optional[str] = ..., sessionId: _Optional[str] = ..., queryId: _Optional[str] = ..., params: _Optional[_Iterable[_Union[ParameterValue, _Mapping]]] = ...) -> None: ...

class ExecuteStatementResponse(_message.Message):
    __slots__ = ["engineIP"]
    ENGINEIP_FIELD_NUMBER: _ClassVar[int]
    engineIP: str
    def __init__(self, engineIP: _Optional[str] = ...) -> None: ...

class GetNextResultRowRequest(_message.Message):
    __slots__ = ["engineIP", "sessionId", "queryId"]
    ENGINEIP_FIELD_NUMBER: _ClassVar[int]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    QUERYID_FIELD_NUMBER: _ClassVar[int]
    engineIP: str
    sessionId: str
    queryId: str
    def __init__(self, engineIP: _Optional[str] = ..., sessionId: _Optional[str] = ..., queryId: _Optional[str] = ...) -> None: ...

class GetNextResultRowResponse(_message.Message):
    __slots__ = ["engineIP", "resultRow"]
    ENGINEIP_FIELD_NUMBER: _ClassVar[int]
    RESULTROW_FIELD_NUMBER: _ClassVar[int]
    engineIP: str
    resultRow: bytes
    def __init__(self, engineIP: _Optional[str] = ..., resultRow: _Optional[bytes] = ...) -> None: ...

class GetNextResultBatchRequest(_message.Message):
    __slots__ = ["engineIP", "sessionId", "queryId"]
    ENGINEIP_FIELD_NUMBER: _ClassVar[int]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    QUERYID_FIELD_NUMBER: _ClassVar[int]
    engineIP: str
    sessionId: str
    queryId: str
    def __init__(self, engineIP: _Optional[str] = ..., sessionId: _Optional[str] = ..., queryId: _Optional[str] = ...) -> None: ...

class GetNextResultBatchResponse(_message.Message):
    __slots__ = ["engineIP", "resultBatch"]
    ENGINEIP_FIELD_NUMBER: _ClassVar[int]
    RESULTBATCH_FIELD_NUMBER: _ClassVar[int]
    engineIP: str
    resultBatch: bytes
    def __init__(self, engineIP: _Optional[str] = ..., resultBatch: _Optional[bytes] = ...) -> None: ...

class GetResultMetadataRequest(_message.Message):
    __slots__ = ["engineIP", "sessionId", "queryId"]
    ENGINEIP_FIELD_NUMBER: _ClassVar[int]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    QUERYID_FIELD_NUMBER: _ClassVar[int]
    engineIP: str
    sessionId: str
    queryId: str
    def __init__(self, engineIP: _Optional[str] = ..., sessionId: _Optional[str] = ..., queryId: _Optional[str] = ...) -> None: ...

class GetResultMetadataResponse(_message.Message):
    __slots__ = ["engineIP", "resultMetaData"]
    ENGINEIP_FIELD_NUMBER: _ClassVar[int]
    RESULTMETADATA_FIELD_NUMBER: _ClassVar[int]
    engineIP: str
    resultMetaData: bytes
    def __init__(self, engineIP: _Optional[str] = ..., resultMetaData: _Optional[bytes] = ...) -> None: ...

class AuthenticateRequest(_message.Message):
    __slots__ = ["user", "password"]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    user: str
    password: str
    def __init__(self, user: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class AuthenticateResponse(_message.Message):
    __slots__ = ["sessionId"]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    def __init__(self, sessionId: _Optional[str] = ...) -> None: ...

class GetTablesRequest(_message.Message):
    __slots__ = ["sessionId", "schema"]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    schema: str
    def __init__(self, sessionId: _Optional[str] = ..., schema: _Optional[str] = ...) -> None: ...

class GetTablesV2Request(_message.Message):
    __slots__ = ["sessionId", "schema", "catalog"]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    CATALOG_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    schema: str
    catalog: str
    def __init__(self, sessionId: _Optional[str] = ..., schema: _Optional[str] = ..., catalog: _Optional[str] = ...) -> None: ...

class GetTablesResponse(_message.Message):
    __slots__ = ["tables"]
    TABLES_FIELD_NUMBER: _ClassVar[int]
    tables: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tables: _Optional[_Iterable[str]] = ...) -> None: ...

class GetSchemaNamesRequest(_message.Message):
    __slots__ = ["sessionId"]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    def __init__(self, sessionId: _Optional[str] = ...) -> None: ...

class GetSchemaNamesV2Request(_message.Message):
    __slots__ = ["sessionId", "catalog"]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    CATALOG_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    catalog: str
    def __init__(self, sessionId: _Optional[str] = ..., catalog: _Optional[str] = ...) -> None: ...

class GetSchemaNamesResponse(_message.Message):
    __slots__ = ["schemas"]
    SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    schemas: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, schemas: _Optional[_Iterable[str]] = ...) -> None: ...

class GetColumnsRequest(_message.Message):
    __slots__ = ["sessionId", "schema", "table"]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    schema: str
    table: str
    def __init__(self, sessionId: _Optional[str] = ..., schema: _Optional[str] = ..., table: _Optional[str] = ...) -> None: ...

class GetColumnsV2Request(_message.Message):
    __slots__ = ["sessionId", "schema", "table", "catalog"]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    TABLE_FIELD_NUMBER: _ClassVar[int]
    CATALOG_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    schema: str
    table: str
    catalog: str
    def __init__(self, sessionId: _Optional[str] = ..., schema: _Optional[str] = ..., table: _Optional[str] = ..., catalog: _Optional[str] = ...) -> None: ...

class GetColumnsResponse(_message.Message):
    __slots__ = ["fieldInfo"]
    FIELDINFO_FIELD_NUMBER: _ClassVar[int]
    fieldInfo: _containers.RepeatedCompositeFieldContainer[GFieldInfo]
    def __init__(self, fieldInfo: _Optional[_Iterable[_Union[GFieldInfo, _Mapping]]] = ...) -> None: ...

class StatusRequest(_message.Message):
    __slots__ = ["engineIP", "sessionId", "queryId"]
    ENGINEIP_FIELD_NUMBER: _ClassVar[int]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    QUERYID_FIELD_NUMBER: _ClassVar[int]
    engineIP: str
    sessionId: str
    queryId: str
    def __init__(self, engineIP: _Optional[str] = ..., sessionId: _Optional[str] = ..., queryId: _Optional[str] = ...) -> None: ...

class StatusResponse(_message.Message):
    __slots__ = ["engineIP", "status", "rowCount"]
    ENGINEIP_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ROWCOUNT_FIELD_NUMBER: _ClassVar[int]
    engineIP: str
    status: bool
    rowCount: int
    def __init__(self, engineIP: _Optional[str] = ..., status: bool = ..., rowCount: _Optional[int] = ...) -> None: ...

class AddCatalogsRequest(_message.Message):
    __slots__ = ["sessionId", "json"]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    JSON_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    json: str
    def __init__(self, sessionId: _Optional[str] = ..., json: _Optional[str] = ...) -> None: ...

class UpdateUsersRequest(_message.Message):
    __slots__ = ["users"]
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: bytes
    def __init__(self, users: _Optional[bytes] = ...) -> None: ...

class UpdateUsersResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SetPropsRequest(_message.Message):
    __slots__ = ["sessionId", "props"]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    PROPS_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    props: str
    def __init__(self, sessionId: _Optional[str] = ..., props: _Optional[str] = ...) -> None: ...

class SetPropsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetAddCatalogsRequest(_message.Message):
    __slots__ = ["sessionId"]
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    def __init__(self, sessionId: _Optional[str] = ...) -> None: ...

class AddCatalogsResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetCatalogesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetCatalogesResponse(_message.Message):
    __slots__ = ["catalogResponses"]
    CATALOGRESPONSES_FIELD_NUMBER: _ClassVar[int]
    catalogResponses: _containers.RepeatedCompositeFieldContainer[CatalogResponse]
    def __init__(self, catalogResponses: _Optional[_Iterable[_Union[CatalogResponse, _Mapping]]] = ...) -> None: ...
