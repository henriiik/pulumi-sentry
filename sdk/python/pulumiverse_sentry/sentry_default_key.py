# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['SentryDefaultKeyArgs', 'SentryDefaultKey']

@pulumi.input_type
class SentryDefaultKeyArgs:
    def __init__(__self__, *,
                 organization: pulumi.Input[str],
                 project: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 rate_limit_count: Optional[pulumi.Input[int]] = None,
                 rate_limit_window: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a SentryDefaultKey resource.
        :param pulumi.Input[str] organization: The slug of the organization the key should be created for
        :param pulumi.Input[str] project: The slug of the project the key should be created for
        :param pulumi.Input[str] name: The name of the key
        """
        pulumi.set(__self__, "organization", organization)
        pulumi.set(__self__, "project", project)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if rate_limit_count is not None:
            pulumi.set(__self__, "rate_limit_count", rate_limit_count)
        if rate_limit_window is not None:
            pulumi.set(__self__, "rate_limit_window", rate_limit_window)

    @property
    @pulumi.getter
    def organization(self) -> pulumi.Input[str]:
        """
        The slug of the organization the key should be created for
        """
        return pulumi.get(self, "organization")

    @organization.setter
    def organization(self, value: pulumi.Input[str]):
        pulumi.set(self, "organization", value)

    @property
    @pulumi.getter
    def project(self) -> pulumi.Input[str]:
        """
        The slug of the project the key should be created for
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: pulumi.Input[str]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the key
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="rateLimitCount")
    def rate_limit_count(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "rate_limit_count")

    @rate_limit_count.setter
    def rate_limit_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "rate_limit_count", value)

    @property
    @pulumi.getter(name="rateLimitWindow")
    def rate_limit_window(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "rate_limit_window")

    @rate_limit_window.setter
    def rate_limit_window(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "rate_limit_window", value)


@pulumi.input_type
class _SentryDefaultKeyState:
    def __init__(__self__, *,
                 dsn_csp: Optional[pulumi.Input[str]] = None,
                 dsn_public: Optional[pulumi.Input[str]] = None,
                 dsn_secret: Optional[pulumi.Input[str]] = None,
                 is_active: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[int]] = None,
                 public: Optional[pulumi.Input[str]] = None,
                 rate_limit_count: Optional[pulumi.Input[int]] = None,
                 rate_limit_window: Optional[pulumi.Input[int]] = None,
                 secret: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SentryDefaultKey resources.
        :param pulumi.Input[str] name: The name of the key
        :param pulumi.Input[str] organization: The slug of the organization the key should be created for
        :param pulumi.Input[str] project: The slug of the project the key should be created for
        """
        if dsn_csp is not None:
            pulumi.set(__self__, "dsn_csp", dsn_csp)
        if dsn_public is not None:
            pulumi.set(__self__, "dsn_public", dsn_public)
        if dsn_secret is not None:
            pulumi.set(__self__, "dsn_secret", dsn_secret)
        if is_active is not None:
            pulumi.set(__self__, "is_active", is_active)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if organization is not None:
            pulumi.set(__self__, "organization", organization)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if public is not None:
            pulumi.set(__self__, "public", public)
        if rate_limit_count is not None:
            pulumi.set(__self__, "rate_limit_count", rate_limit_count)
        if rate_limit_window is not None:
            pulumi.set(__self__, "rate_limit_window", rate_limit_window)
        if secret is not None:
            pulumi.set(__self__, "secret", secret)

    @property
    @pulumi.getter(name="dsnCsp")
    def dsn_csp(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "dsn_csp")

    @dsn_csp.setter
    def dsn_csp(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dsn_csp", value)

    @property
    @pulumi.getter(name="dsnPublic")
    def dsn_public(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "dsn_public")

    @dsn_public.setter
    def dsn_public(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dsn_public", value)

    @property
    @pulumi.getter(name="dsnSecret")
    def dsn_secret(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "dsn_secret")

    @dsn_secret.setter
    def dsn_secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dsn_secret", value)

    @property
    @pulumi.getter(name="isActive")
    def is_active(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "is_active")

    @is_active.setter
    def is_active(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_active", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the key
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def organization(self) -> Optional[pulumi.Input[str]]:
        """
        The slug of the organization the key should be created for
        """
        return pulumi.get(self, "organization")

    @organization.setter
    def organization(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The slug of the project the key should be created for
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def public(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "public")

    @public.setter
    def public(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public", value)

    @property
    @pulumi.getter(name="rateLimitCount")
    def rate_limit_count(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "rate_limit_count")

    @rate_limit_count.setter
    def rate_limit_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "rate_limit_count", value)

    @property
    @pulumi.getter(name="rateLimitWindow")
    def rate_limit_window(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "rate_limit_window")

    @rate_limit_window.setter
    def rate_limit_window(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "rate_limit_window", value)

    @property
    @pulumi.getter
    def secret(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "secret")

    @secret.setter
    def secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret", value)


class SentryDefaultKey(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 rate_limit_count: Optional[pulumi.Input[int]] = None,
                 rate_limit_window: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Create a SentryDefaultKey resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the key
        :param pulumi.Input[str] organization: The slug of the organization the key should be created for
        :param pulumi.Input[str] project: The slug of the project the key should be created for
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SentryDefaultKeyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a SentryDefaultKey resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param SentryDefaultKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SentryDefaultKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 rate_limit_count: Optional[pulumi.Input[int]] = None,
                 rate_limit_window: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.plugin_download_url is None:
            opts.plugin_download_url = _utilities.get_plugin_download_url()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SentryDefaultKeyArgs.__new__(SentryDefaultKeyArgs)

            __props__.__dict__["name"] = name
            if organization is None and not opts.urn:
                raise TypeError("Missing required property 'organization'")
            __props__.__dict__["organization"] = organization
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
            __props__.__dict__["rate_limit_count"] = rate_limit_count
            __props__.__dict__["rate_limit_window"] = rate_limit_window
            __props__.__dict__["dsn_csp"] = None
            __props__.__dict__["dsn_public"] = None
            __props__.__dict__["dsn_secret"] = None
            __props__.__dict__["is_active"] = None
            __props__.__dict__["project_id"] = None
            __props__.__dict__["public"] = None
            __props__.__dict__["secret"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["dsnSecret", "secret"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(SentryDefaultKey, __self__).__init__(
            'sentry:index/sentryDefaultKey:SentryDefaultKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            dsn_csp: Optional[pulumi.Input[str]] = None,
            dsn_public: Optional[pulumi.Input[str]] = None,
            dsn_secret: Optional[pulumi.Input[str]] = None,
            is_active: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            organization: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[int]] = None,
            public: Optional[pulumi.Input[str]] = None,
            rate_limit_count: Optional[pulumi.Input[int]] = None,
            rate_limit_window: Optional[pulumi.Input[int]] = None,
            secret: Optional[pulumi.Input[str]] = None) -> 'SentryDefaultKey':
        """
        Get an existing SentryDefaultKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the key
        :param pulumi.Input[str] organization: The slug of the organization the key should be created for
        :param pulumi.Input[str] project: The slug of the project the key should be created for
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SentryDefaultKeyState.__new__(_SentryDefaultKeyState)

        __props__.__dict__["dsn_csp"] = dsn_csp
        __props__.__dict__["dsn_public"] = dsn_public
        __props__.__dict__["dsn_secret"] = dsn_secret
        __props__.__dict__["is_active"] = is_active
        __props__.__dict__["name"] = name
        __props__.__dict__["organization"] = organization
        __props__.__dict__["project"] = project
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["public"] = public
        __props__.__dict__["rate_limit_count"] = rate_limit_count
        __props__.__dict__["rate_limit_window"] = rate_limit_window
        __props__.__dict__["secret"] = secret
        return SentryDefaultKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dsnCsp")
    def dsn_csp(self) -> pulumi.Output[str]:
        return pulumi.get(self, "dsn_csp")

    @property
    @pulumi.getter(name="dsnPublic")
    def dsn_public(self) -> pulumi.Output[str]:
        return pulumi.get(self, "dsn_public")

    @property
    @pulumi.getter(name="dsnSecret")
    def dsn_secret(self) -> pulumi.Output[str]:
        return pulumi.get(self, "dsn_secret")

    @property
    @pulumi.getter(name="isActive")
    def is_active(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "is_active")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the key
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def organization(self) -> pulumi.Output[str]:
        """
        The slug of the organization the key should be created for
        """
        return pulumi.get(self, "organization")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The slug of the project the key should be created for
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def public(self) -> pulumi.Output[str]:
        return pulumi.get(self, "public")

    @property
    @pulumi.getter(name="rateLimitCount")
    def rate_limit_count(self) -> pulumi.Output[int]:
        return pulumi.get(self, "rate_limit_count")

    @property
    @pulumi.getter(name="rateLimitWindow")
    def rate_limit_window(self) -> pulumi.Output[int]:
        return pulumi.get(self, "rate_limit_window")

    @property
    @pulumi.getter
    def secret(self) -> pulumi.Output[str]:
        return pulumi.get(self, "secret")

