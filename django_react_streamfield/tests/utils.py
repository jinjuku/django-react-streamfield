def streamfield(items):
    """
    Takes a list of (block_type, value) tuples and turns it in to
    StreamField form data. Use this within a :func:`nested_form_data`
    call, with the field name as the key.
    .. code-block:: python
        nested_form_data({'content': streamfield([
            ('text', 'Hello, world'),
        ])})
        # Returns:
        # {
        #     'content-count': '1',
        #     'content-0-type': 'text',
        #     'content-0-value': 'Hello, world',
        #     'content-0-order': '0',
        #     'content-0-deleted': '',
        # }
    """

    def to_block(index, item):
        block, value = item
        return {"type": block, "value": value, "deleted": "", "order": str(index)}

    data_dict = {str(index): to_block(index, item) for index, item in enumerate(items)}
    data_dict["count"] = str(len(data_dict))
    return data_dict
