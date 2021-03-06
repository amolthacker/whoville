# coding: utf-8

"""
    Cloudbreak API

    Cloudbreak is a powerful left surf that breaks over a coral reef, a mile off southwest the island of Tavarua, Fiji. Cloudbreak is a cloud agnostic Hadoop as a Service API. Abstracts the provisioning and ease management and monitoring of on-demand clusters. SequenceIQ's Cloudbreak is a RESTful application development platform with the goal of helping developers to build solutions for deploying Hadoop YARN clusters in different environments. Once it is deployed in your favourite servlet container it exposes a REST API allowing to span up Hadoop clusters of arbitary sizes and cloud providers. Provisioning Hadoop has never been easier. Cloudbreak is built on the foundation of cloud providers API (Amazon AWS, Microsoft Azure, Google Cloud Platform, Openstack), Apache Ambari, Docker lightweight containers, Swarm and Consul. For further product documentation follow the link: <a href=\"http://hortonworks.com/apache/cloudbreak/\">http://hortonworks.com/apache/cloudbreak/</a>

    OpenAPI spec version: 2.9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UpdateCluster(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'host_group_adjustment': 'HostGroupAdjustment',
        'status': 'str',
        'user_name_password_json': 'UserNamePassword',
        'blueprint_id': 'int',
        'validate_blueprint': 'bool',
        'hostgroups': 'list[HostGroupRequest]',
        'ambari_stack_details': 'AmbariStackDetails',
        'kerberos_password': 'str',
        'kerberos_principal': 'str'
    }

    attribute_map = {
        'host_group_adjustment': 'hostGroupAdjustment',
        'status': 'status',
        'user_name_password_json': 'userNamePasswordJson',
        'blueprint_id': 'blueprintId',
        'validate_blueprint': 'validateBlueprint',
        'hostgroups': 'hostgroups',
        'ambari_stack_details': 'ambariStackDetails',
        'kerberos_password': 'kerberosPassword',
        'kerberos_principal': 'kerberosPrincipal'
    }

    def __init__(self, host_group_adjustment=None, status=None, user_name_password_json=None, blueprint_id=None, validate_blueprint=False, hostgroups=None, ambari_stack_details=None, kerberos_password=None, kerberos_principal=None):
        """
        UpdateCluster - a model defined in Swagger
        """

        self._host_group_adjustment = None
        self._status = None
        self._user_name_password_json = None
        self._blueprint_id = None
        self._validate_blueprint = None
        self._hostgroups = None
        self._ambari_stack_details = None
        self._kerberos_password = None
        self._kerberos_principal = None

        if host_group_adjustment is not None:
          self.host_group_adjustment = host_group_adjustment
        if status is not None:
          self.status = status
        if user_name_password_json is not None:
          self.user_name_password_json = user_name_password_json
        if blueprint_id is not None:
          self.blueprint_id = blueprint_id
        if validate_blueprint is not None:
          self.validate_blueprint = validate_blueprint
        if hostgroups is not None:
          self.hostgroups = hostgroups
        if ambari_stack_details is not None:
          self.ambari_stack_details = ambari_stack_details
        if kerberos_password is not None:
          self.kerberos_password = kerberos_password
        if kerberos_principal is not None:
          self.kerberos_principal = kerberos_principal

    @property
    def host_group_adjustment(self):
        """
        Gets the host_group_adjustment of this UpdateCluster.
        host group adjustment

        :return: The host_group_adjustment of this UpdateCluster.
        :rtype: HostGroupAdjustment
        """
        return self._host_group_adjustment

    @host_group_adjustment.setter
    def host_group_adjustment(self, host_group_adjustment):
        """
        Sets the host_group_adjustment of this UpdateCluster.
        host group adjustment

        :param host_group_adjustment: The host_group_adjustment of this UpdateCluster.
        :type: HostGroupAdjustment
        """

        self._host_group_adjustment = host_group_adjustment

    @property
    def status(self):
        """
        Gets the status of this UpdateCluster.
        request status

        :return: The status of this UpdateCluster.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UpdateCluster.
        request status

        :param status: The status of this UpdateCluster.
        :type: str
        """
        allowed_values = ["SYNC", "FULL_SYNC", "REPAIR_FAILED_NODES", "STOPPED", "STARTED"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def user_name_password_json(self):
        """
        Gets the user_name_password_json of this UpdateCluster.
        user details

        :return: The user_name_password_json of this UpdateCluster.
        :rtype: UserNamePassword
        """
        return self._user_name_password_json

    @user_name_password_json.setter
    def user_name_password_json(self, user_name_password_json):
        """
        Sets the user_name_password_json of this UpdateCluster.
        user details

        :param user_name_password_json: The user_name_password_json of this UpdateCluster.
        :type: UserNamePassword
        """

        self._user_name_password_json = user_name_password_json

    @property
    def blueprint_id(self):
        """
        Gets the blueprint_id of this UpdateCluster.
        blueprint id for the cluster

        :return: The blueprint_id of this UpdateCluster.
        :rtype: int
        """
        return self._blueprint_id

    @blueprint_id.setter
    def blueprint_id(self, blueprint_id):
        """
        Sets the blueprint_id of this UpdateCluster.
        blueprint id for the cluster

        :param blueprint_id: The blueprint_id of this UpdateCluster.
        :type: int
        """

        self._blueprint_id = blueprint_id

    @property
    def validate_blueprint(self):
        """
        Gets the validate_blueprint of this UpdateCluster.
        blueprint validation

        :return: The validate_blueprint of this UpdateCluster.
        :rtype: bool
        """
        return self._validate_blueprint

    @validate_blueprint.setter
    def validate_blueprint(self, validate_blueprint):
        """
        Sets the validate_blueprint of this UpdateCluster.
        blueprint validation

        :param validate_blueprint: The validate_blueprint of this UpdateCluster.
        :type: bool
        """

        self._validate_blueprint = validate_blueprint

    @property
    def hostgroups(self):
        """
        Gets the hostgroups of this UpdateCluster.
        collection of hostgroups

        :return: The hostgroups of this UpdateCluster.
        :rtype: list[HostGroupRequest]
        """
        return self._hostgroups

    @hostgroups.setter
    def hostgroups(self, hostgroups):
        """
        Sets the hostgroups of this UpdateCluster.
        collection of hostgroups

        :param hostgroups: The hostgroups of this UpdateCluster.
        :type: list[HostGroupRequest]
        """

        self._hostgroups = hostgroups

    @property
    def ambari_stack_details(self):
        """
        Gets the ambari_stack_details of this UpdateCluster.
        details of the Ambari stack

        :return: The ambari_stack_details of this UpdateCluster.
        :rtype: AmbariStackDetails
        """
        return self._ambari_stack_details

    @ambari_stack_details.setter
    def ambari_stack_details(self, ambari_stack_details):
        """
        Sets the ambari_stack_details of this UpdateCluster.
        details of the Ambari stack

        :param ambari_stack_details: The ambari_stack_details of this UpdateCluster.
        :type: AmbariStackDetails
        """

        self._ambari_stack_details = ambari_stack_details

    @property
    def kerberos_password(self):
        """
        Gets the kerberos_password of this UpdateCluster.
        kerberos admin password

        :return: The kerberos_password of this UpdateCluster.
        :rtype: str
        """
        return self._kerberos_password

    @kerberos_password.setter
    def kerberos_password(self, kerberos_password):
        """
        Sets the kerberos_password of this UpdateCluster.
        kerberos admin password

        :param kerberos_password: The kerberos_password of this UpdateCluster.
        :type: str
        """
        if kerberos_password is not None and len(kerberos_password) > 50:
            raise ValueError("Invalid value for `kerberos_password`, length must be less than or equal to `50`")
        if kerberos_password is not None and len(kerberos_password) < 5:
            raise ValueError("Invalid value for `kerberos_password`, length must be greater than or equal to `5`")

        self._kerberos_password = kerberos_password

    @property
    def kerberos_principal(self):
        """
        Gets the kerberos_principal of this UpdateCluster.
        kerberos principal

        :return: The kerberos_principal of this UpdateCluster.
        :rtype: str
        """
        return self._kerberos_principal

    @kerberos_principal.setter
    def kerberos_principal(self, kerberos_principal):
        """
        Sets the kerberos_principal of this UpdateCluster.
        kerberos principal

        :param kerberos_principal: The kerberos_principal of this UpdateCluster.
        :type: str
        """

        self._kerberos_principal = kerberos_principal

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, UpdateCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
