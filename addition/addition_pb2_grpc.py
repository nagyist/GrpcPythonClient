# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import addition_pb2 as addition__pb2


class AdderStub(object):
  """The greeting service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.AddNumbers = channel.unary_unary(
        '/helloworld.Adder/AddNumbers',
        request_serializer=addition__pb2.AddRequest.SerializeToString,
        response_deserializer=addition__pb2.AddReply.FromString,
        )


class AdderServicer(object):
  """The greeting service definition.
  """

  def AddNumbers(self, request, context):
    """Adds numbers
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AdderServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'AddNumbers': grpc.unary_unary_rpc_method_handler(
          servicer.AddNumbers,
          request_deserializer=addition__pb2.AddRequest.FromString,
          response_serializer=addition__pb2.AddReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'helloworld.Adder', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
