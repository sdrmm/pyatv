# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Optional as typing___Optional,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class PlaybackQueueCapabilities(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    requestByRange = ... # type: builtin___bool
    requestByIdentifiers = ... # type: builtin___bool
    requestByRequest = ... # type: builtin___bool

    def __init__(self,
        *,
        requestByRange : typing___Optional[builtin___bool] = None,
        requestByIdentifiers : typing___Optional[builtin___bool] = None,
        requestByRequest : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> PlaybackQueueCapabilities: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> PlaybackQueueCapabilities: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"requestByIdentifiers",b"requestByIdentifiers",u"requestByRange",b"requestByRange",u"requestByRequest",b"requestByRequest"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"requestByIdentifiers",b"requestByIdentifiers",u"requestByRange",b"requestByRange",u"requestByRequest",b"requestByRequest"]) -> None: ...
