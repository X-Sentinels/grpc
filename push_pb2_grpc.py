# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import push_pb2 as push__pb2


class MessageSyncStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SubmitMessage = channel.unary_unary(
        '/MessageSync/SubmitMessage',
        request_serializer=push__pb2.SubmitRequest.SerializeToString,
        response_deserializer=push__pb2.SubmitReply.FromString,
        )
    self.PushMessageStream = channel.unary_stream(
        '/MessageSync/PushMessageStream',
        request_serializer=push__pb2.ConnRequest.SerializeToString,
        response_deserializer=push__pb2.MessageReply.FromString,
        )


class MessageSyncServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SubmitMessage(self, request, context):
    """message producer
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PushMessageStream(self, request, context):
    """message consume, push mode
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MessageSyncServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SubmitMessage': grpc.unary_unary_rpc_method_handler(
          servicer.SubmitMessage,
          request_deserializer=push__pb2.SubmitRequest.FromString,
          response_serializer=push__pb2.SubmitReply.SerializeToString,
      ),
      'PushMessageStream': grpc.unary_stream_rpc_method_handler(
          servicer.PushMessageStream,
          request_deserializer=push__pb2.ConnRequest.FromString,
          response_serializer=push__pb2.MessageReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'MessageSync', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
