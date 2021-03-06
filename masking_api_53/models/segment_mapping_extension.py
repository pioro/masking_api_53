# coding: utf-8

"""
    Masking API

    Schema for the Masking Engine API  # noqa: E501

    OpenAPI spec version: 5.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SegmentMappingExtension(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'preserved_ranges': 'list[SegmentMappingPreservedRange]',
        'ignore_characters': 'list[int]',
        'segments': 'list[SegmentMappingSegment]',
        'segments_group_length': 'list[int]',
        'error_handling_mode': 'str'
    }

    attribute_map = {
        'preserved_ranges': 'preservedRanges',
        'ignore_characters': 'ignoreCharacters',
        'segments': 'segments',
        'segments_group_length': 'segmentsGroupLength',
        'error_handling_mode': 'errorHandlingMode'
    }

    def __init__(self, preserved_ranges=None, ignore_characters=None, segments=None, segments_group_length=None, error_handling_mode='DEFAULT'):  # noqa: E501
        """SegmentMappingExtension - a model defined in Swagger"""  # noqa: E501

        self._preserved_ranges = None
        self._ignore_characters = None
        self._segments = None
        self._segments_group_length = None
        self._error_handling_mode = None
        self.discriminator = None

        if preserved_ranges is not None:
            self.preserved_ranges = preserved_ranges
        if ignore_characters is not None:
            self.ignore_characters = ignore_characters
        if segments is not None:
            self.segments = segments
        if segments_group_length is not None:
            self.segments_group_length = segments_group_length
        if error_handling_mode is not None:
            self.error_handling_mode = error_handling_mode

    @property
    def preserved_ranges(self):
        """Gets the preserved_ranges of this SegmentMappingExtension.  # noqa: E501

        List of character {offset, length} values specifying ranges of the real value to preserve. Offsets begin at 0  # noqa: E501

        :return: The preserved_ranges of this SegmentMappingExtension.  # noqa: E501
        :rtype: list[SegmentMappingPreservedRange]
        """
        return self._preserved_ranges

    @preserved_ranges.setter
    def preserved_ranges(self, preserved_ranges):
        """Sets the preserved_ranges of this SegmentMappingExtension.

        List of character {offset, length} values specifying ranges of the real value to preserve. Offsets begin at 0  # noqa: E501

        :param preserved_ranges: The preserved_ranges of this SegmentMappingExtension.  # noqa: E501
        :type: list[SegmentMappingPreservedRange]
        """

        self._preserved_ranges = preserved_ranges

    @property
    def ignore_characters(self):
        """Gets the ignore_characters of this SegmentMappingExtension.  # noqa: E501

        List of decimal values specifying UTF-16 codepoints of characters to ignore (not mask, not count as part of any segment) in the real value. For example, 65 would ignore 'A'  # noqa: E501

        :return: The ignore_characters of this SegmentMappingExtension.  # noqa: E501
        :rtype: list[int]
        """
        return self._ignore_characters

    @ignore_characters.setter
    def ignore_characters(self, ignore_characters):
        """Sets the ignore_characters of this SegmentMappingExtension.

        List of decimal values specifying UTF-16 codepoints of characters to ignore (not mask, not count as part of any segment) in the real value. For example, 65 would ignore 'A'  # noqa: E501

        :param ignore_characters: The ignore_characters of this SegmentMappingExtension.  # noqa: E501
        :type: list[int]
        """

        self._ignore_characters = ignore_characters

    @property
    def segments(self):
        """Gets the segments of this SegmentMappingExtension.  # noqa: E501


        :return: The segments of this SegmentMappingExtension.  # noqa: E501
        :rtype: list[SegmentMappingSegment]
        """
        return self._segments

    @segments.setter
    def segments(self, segments):
        """Sets the segments of this SegmentMappingExtension.


        :param segments: The segments of this SegmentMappingExtension.  # noqa: E501
        :type: list[SegmentMappingSegment]
        """

        self._segments = segments

    @property
    def segments_group_length(self):
        """Gets the segments_group_length of this SegmentMappingExtension.  # noqa: E501

        The array to hold UI display length of each Segment group.  # noqa: E501

        :return: The segments_group_length of this SegmentMappingExtension.  # noqa: E501
        :rtype: list[int]
        """
        return self._segments_group_length

    @segments_group_length.setter
    def segments_group_length(self, segments_group_length):
        """Sets the segments_group_length of this SegmentMappingExtension.

        The array to hold UI display length of each Segment group.  # noqa: E501

        :param segments_group_length: The segments_group_length of this SegmentMappingExtension.  # noqa: E501
        :type: list[int]
        """

        self._segments_group_length = segments_group_length

    @property
    def error_handling_mode(self):
        """Gets the error_handling_mode of this SegmentMappingExtension.  # noqa: E501

        The behavior should a non-conformant, segment mapping data pattern be encountered by the algorithm.  # noqa: E501

        :return: The error_handling_mode of this SegmentMappingExtension.  # noqa: E501
        :rtype: str
        """
        return self._error_handling_mode

    @error_handling_mode.setter
    def error_handling_mode(self, error_handling_mode):
        """Sets the error_handling_mode of this SegmentMappingExtension.

        The behavior should a non-conformant, segment mapping data pattern be encountered by the algorithm.  # noqa: E501

        :param error_handling_mode: The error_handling_mode of this SegmentMappingExtension.  # noqa: E501
        :type: str
        """
        allowed_values = ["DEFAULT", "DONT_MASK", "FAIL"]  # noqa: E501
        if error_handling_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `error_handling_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(error_handling_mode, allowed_values)
            )

        self._error_handling_mode = error_handling_mode

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SegmentMappingExtension, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SegmentMappingExtension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
