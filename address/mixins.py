class ActionSpecificSerializerMixin(object):
    """
    Mixin to support serializer for each action/method on ApiView/ViewSet.
    usage with ViewSet :
    serializer_classes = {
        'retrieve': serializer
        'partial_update': serializer
        'custom_action': serializer
    }
    usage with ApiView :
    serializer_classes = {
        'get': serializer
        'post': serializer
        'put': serializer
    }
    For any missing method/action, It will fallback to original behaviour, i.e. use serializer from
    serializer_class.
    """
    serializer_classes = NotImplemented

    def get_serializer_class(self):
        """
        Sets the appropriate permission class.
        """
        action = self.action if hasattr(self, 'action') else self.method
        self.serializer_class = self.serializer_classes.get(action, self.serializer_class)
        return super(ActionSpecificSerializerMixin, self).get_serializer_class()