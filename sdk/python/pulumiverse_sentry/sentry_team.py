# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['SentryTeamArgs', 'SentryTeam']

@pulumi.input_type
class SentryTeamArgs:
    def __init__(__self__, *,
                 organization: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 slug: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SentryTeam resource.
        :param pulumi.Input[str] organization: The slug of the organization the team should be created for.
        :param pulumi.Input[str] name: The human readable name for the team.
        :param pulumi.Input[str] slug: The unique URL slug for this team. If this is not provided a slug is automatically generated based on the name.
        """
        pulumi.set(__self__, "organization", organization)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if slug is not None:
            pulumi.set(__self__, "slug", slug)

    @property
    @pulumi.getter
    def organization(self) -> pulumi.Input[str]:
        """
        The slug of the organization the team should be created for.
        """
        return pulumi.get(self, "organization")

    @organization.setter
    def organization(self, value: pulumi.Input[str]):
        pulumi.set(self, "organization", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The human readable name for the team.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def slug(self) -> Optional[pulumi.Input[str]]:
        """
        The unique URL slug for this team. If this is not provided a slug is automatically generated based on the name.
        """
        return pulumi.get(self, "slug")

    @slug.setter
    def slug(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "slug", value)


@pulumi.input_type
class _SentryTeamState:
    def __init__(__self__, *,
                 has_access: Optional[pulumi.Input[bool]] = None,
                 is_member: Optional[pulumi.Input[bool]] = None,
                 is_pending: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization: Optional[pulumi.Input[str]] = None,
                 slug: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SentryTeam resources.
        :param pulumi.Input[str] name: The human readable name for the team.
        :param pulumi.Input[str] organization: The slug of the organization the team should be created for.
        :param pulumi.Input[str] slug: The unique URL slug for this team. If this is not provided a slug is automatically generated based on the name.
        """
        if has_access is not None:
            pulumi.set(__self__, "has_access", has_access)
        if is_member is not None:
            pulumi.set(__self__, "is_member", is_member)
        if is_pending is not None:
            pulumi.set(__self__, "is_pending", is_pending)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if organization is not None:
            pulumi.set(__self__, "organization", organization)
        if slug is not None:
            pulumi.set(__self__, "slug", slug)
        if team_id is not None:
            pulumi.set(__self__, "team_id", team_id)

    @property
    @pulumi.getter(name="hasAccess")
    def has_access(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "has_access")

    @has_access.setter
    def has_access(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "has_access", value)

    @property
    @pulumi.getter(name="isMember")
    def is_member(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "is_member")

    @is_member.setter
    def is_member(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_member", value)

    @property
    @pulumi.getter(name="isPending")
    def is_pending(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "is_pending")

    @is_pending.setter
    def is_pending(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_pending", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The human readable name for the team.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def organization(self) -> Optional[pulumi.Input[str]]:
        """
        The slug of the organization the team should be created for.
        """
        return pulumi.get(self, "organization")

    @organization.setter
    def organization(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization", value)

    @property
    @pulumi.getter
    def slug(self) -> Optional[pulumi.Input[str]]:
        """
        The unique URL slug for this team. If this is not provided a slug is automatically generated based on the name.
        """
        return pulumi.get(self, "slug")

    @slug.setter
    def slug(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "slug", value)

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "team_id", value)


class SentryTeam(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization: Optional[pulumi.Input[str]] = None,
                 slug: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## # SentryTeam Resource

        Sentry Team resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumiverse_sentry as sentry

        # Create a team
        default = sentry.SentryTeam("default",
            organization="my-organization",
            slug="my-team")
        ```

        ## Import

        This resource can be imported using an ID made up of the organization slug and project slugbash

        ```sh
         $ pulumi import sentry:index/sentryTeam:SentryTeam default org-slug/team-slug
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The human readable name for the team.
        :param pulumi.Input[str] organization: The slug of the organization the team should be created for.
        :param pulumi.Input[str] slug: The unique URL slug for this team. If this is not provided a slug is automatically generated based on the name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SentryTeamArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## # SentryTeam Resource

        Sentry Team resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumiverse_sentry as sentry

        # Create a team
        default = sentry.SentryTeam("default",
            organization="my-organization",
            slug="my-team")
        ```

        ## Import

        This resource can be imported using an ID made up of the organization slug and project slugbash

        ```sh
         $ pulumi import sentry:index/sentryTeam:SentryTeam default org-slug/team-slug
        ```

        :param str resource_name: The name of the resource.
        :param SentryTeamArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SentryTeamArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization: Optional[pulumi.Input[str]] = None,
                 slug: Optional[pulumi.Input[str]] = None,
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
            __props__ = SentryTeamArgs.__new__(SentryTeamArgs)

            __props__.__dict__["name"] = name
            if organization is None and not opts.urn:
                raise TypeError("Missing required property 'organization'")
            __props__.__dict__["organization"] = organization
            __props__.__dict__["slug"] = slug
            __props__.__dict__["has_access"] = None
            __props__.__dict__["is_member"] = None
            __props__.__dict__["is_pending"] = None
            __props__.__dict__["team_id"] = None
        super(SentryTeam, __self__).__init__(
            'sentry:index/sentryTeam:SentryTeam',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            has_access: Optional[pulumi.Input[bool]] = None,
            is_member: Optional[pulumi.Input[bool]] = None,
            is_pending: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            organization: Optional[pulumi.Input[str]] = None,
            slug: Optional[pulumi.Input[str]] = None,
            team_id: Optional[pulumi.Input[str]] = None) -> 'SentryTeam':
        """
        Get an existing SentryTeam resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The human readable name for the team.
        :param pulumi.Input[str] organization: The slug of the organization the team should be created for.
        :param pulumi.Input[str] slug: The unique URL slug for this team. If this is not provided a slug is automatically generated based on the name.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SentryTeamState.__new__(_SentryTeamState)

        __props__.__dict__["has_access"] = has_access
        __props__.__dict__["is_member"] = is_member
        __props__.__dict__["is_pending"] = is_pending
        __props__.__dict__["name"] = name
        __props__.__dict__["organization"] = organization
        __props__.__dict__["slug"] = slug
        __props__.__dict__["team_id"] = team_id
        return SentryTeam(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="hasAccess")
    def has_access(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "has_access")

    @property
    @pulumi.getter(name="isMember")
    def is_member(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "is_member")

    @property
    @pulumi.getter(name="isPending")
    def is_pending(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "is_pending")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The human readable name for the team.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def organization(self) -> pulumi.Output[str]:
        """
        The slug of the organization the team should be created for.
        """
        return pulumi.get(self, "organization")

    @property
    @pulumi.getter
    def slug(self) -> pulumi.Output[str]:
        """
        The unique URL slug for this team. If this is not provided a slug is automatically generated based on the name.
        """
        return pulumi.get(self, "slug")

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "team_id")

