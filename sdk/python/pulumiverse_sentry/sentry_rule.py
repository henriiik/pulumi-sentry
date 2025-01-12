# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['SentryRuleArgs', 'SentryRule']

@pulumi.input_type
class SentryRuleArgs:
    def __init__(__self__, *,
                 actions: pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]],
                 conditions: pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]],
                 organization: pulumi.Input[str],
                 project: pulumi.Input[str],
                 action_match: Optional[pulumi.Input[str]] = None,
                 environment: Optional[pulumi.Input[str]] = None,
                 filter_match: Optional[pulumi.Input[str]] = None,
                 filters: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]] = None,
                 frequency: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SentryRule resource.
        :param pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]] actions: List of actions.
        :param pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]] conditions: List of conditions.
        :param pulumi.Input[str] organization: The slug of the organization the plugin should be enabled for.
        :param pulumi.Input[str] project: The slug of the project the plugin should be enabled for.
        :param pulumi.Input[str] action_match: Use `all` to trigger alerting when all conditions are met, and `any` when at. least a condition is met. Defaults to `any`.
        :param pulumi.Input[str] environment: Environment for these conditions to apply to.
        :param pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]] filters: List of filters.
        :param pulumi.Input[int] frequency: Perform actions at most once every `X` minutes for this issue. Defaults to `30`.
        :param pulumi.Input[str] name: Name for this alert.
        """
        pulumi.set(__self__, "actions", actions)
        pulumi.set(__self__, "conditions", conditions)
        pulumi.set(__self__, "organization", organization)
        pulumi.set(__self__, "project", project)
        if action_match is not None:
            pulumi.set(__self__, "action_match", action_match)
        if environment is not None:
            pulumi.set(__self__, "environment", environment)
        if filter_match is not None:
            pulumi.set(__self__, "filter_match", filter_match)
        if filters is not None:
            pulumi.set(__self__, "filters", filters)
        if frequency is not None:
            pulumi.set(__self__, "frequency", frequency)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]:
        """
        List of actions.
        """
        return pulumi.get(self, "actions")

    @actions.setter
    def actions(self, value: pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]):
        pulumi.set(self, "actions", value)

    @property
    @pulumi.getter
    def conditions(self) -> pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]:
        """
        List of conditions.
        """
        return pulumi.get(self, "conditions")

    @conditions.setter
    def conditions(self, value: pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]):
        pulumi.set(self, "conditions", value)

    @property
    @pulumi.getter
    def organization(self) -> pulumi.Input[str]:
        """
        The slug of the organization the plugin should be enabled for.
        """
        return pulumi.get(self, "organization")

    @organization.setter
    def organization(self, value: pulumi.Input[str]):
        pulumi.set(self, "organization", value)

    @property
    @pulumi.getter
    def project(self) -> pulumi.Input[str]:
        """
        The slug of the project the plugin should be enabled for.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: pulumi.Input[str]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="actionMatch")
    def action_match(self) -> Optional[pulumi.Input[str]]:
        """
        Use `all` to trigger alerting when all conditions are met, and `any` when at. least a condition is met. Defaults to `any`.
        """
        return pulumi.get(self, "action_match")

    @action_match.setter
    def action_match(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action_match", value)

    @property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[str]]:
        """
        Environment for these conditions to apply to.
        """
        return pulumi.get(self, "environment")

    @environment.setter
    def environment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "environment", value)

    @property
    @pulumi.getter(name="filterMatch")
    def filter_match(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "filter_match")

    @filter_match.setter
    def filter_match(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "filter_match", value)

    @property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]]:
        """
        List of filters.
        """
        return pulumi.get(self, "filters")

    @filters.setter
    def filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]]):
        pulumi.set(self, "filters", value)

    @property
    @pulumi.getter
    def frequency(self) -> Optional[pulumi.Input[int]]:
        """
        Perform actions at most once every `X` minutes for this issue. Defaults to `30`.
        """
        return pulumi.get(self, "frequency")

    @frequency.setter
    def frequency(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "frequency", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name for this alert.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _SentryRuleState:
    def __init__(__self__, *,
                 action_match: Optional[pulumi.Input[str]] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]] = None,
                 conditions: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]] = None,
                 environment: Optional[pulumi.Input[str]] = None,
                 filter_match: Optional[pulumi.Input[str]] = None,
                 filters: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]] = None,
                 frequency: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SentryRule resources.
        :param pulumi.Input[str] action_match: Use `all` to trigger alerting when all conditions are met, and `any` when at. least a condition is met. Defaults to `any`.
        :param pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]] actions: List of actions.
        :param pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]] conditions: List of conditions.
        :param pulumi.Input[str] environment: Environment for these conditions to apply to.
        :param pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]] filters: List of filters.
        :param pulumi.Input[int] frequency: Perform actions at most once every `X` minutes for this issue. Defaults to `30`.
        :param pulumi.Input[str] name: Name for this alert.
        :param pulumi.Input[str] organization: The slug of the organization the plugin should be enabled for.
        :param pulumi.Input[str] project: The slug of the project the plugin should be enabled for.
        """
        if action_match is not None:
            pulumi.set(__self__, "action_match", action_match)
        if actions is not None:
            pulumi.set(__self__, "actions", actions)
        if conditions is not None:
            pulumi.set(__self__, "conditions", conditions)
        if environment is not None:
            pulumi.set(__self__, "environment", environment)
        if filter_match is not None:
            pulumi.set(__self__, "filter_match", filter_match)
        if filters is not None:
            pulumi.set(__self__, "filters", filters)
        if frequency is not None:
            pulumi.set(__self__, "frequency", frequency)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if organization is not None:
            pulumi.set(__self__, "organization", organization)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter(name="actionMatch")
    def action_match(self) -> Optional[pulumi.Input[str]]:
        """
        Use `all` to trigger alerting when all conditions are met, and `any` when at. least a condition is met. Defaults to `any`.
        """
        return pulumi.get(self, "action_match")

    @action_match.setter
    def action_match(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action_match", value)

    @property
    @pulumi.getter
    def actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]]:
        """
        List of actions.
        """
        return pulumi.get(self, "actions")

    @actions.setter
    def actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]]):
        pulumi.set(self, "actions", value)

    @property
    @pulumi.getter
    def conditions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]]:
        """
        List of conditions.
        """
        return pulumi.get(self, "conditions")

    @conditions.setter
    def conditions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]]):
        pulumi.set(self, "conditions", value)

    @property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[str]]:
        """
        Environment for these conditions to apply to.
        """
        return pulumi.get(self, "environment")

    @environment.setter
    def environment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "environment", value)

    @property
    @pulumi.getter(name="filterMatch")
    def filter_match(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "filter_match")

    @filter_match.setter
    def filter_match(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "filter_match", value)

    @property
    @pulumi.getter
    def filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]]:
        """
        List of filters.
        """
        return pulumi.get(self, "filters")

    @filters.setter
    def filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]]):
        pulumi.set(self, "filters", value)

    @property
    @pulumi.getter
    def frequency(self) -> Optional[pulumi.Input[int]]:
        """
        Perform actions at most once every `X` minutes for this issue. Defaults to `30`.
        """
        return pulumi.get(self, "frequency")

    @frequency.setter
    def frequency(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "frequency", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name for this alert.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def organization(self) -> Optional[pulumi.Input[str]]:
        """
        The slug of the organization the plugin should be enabled for.
        """
        return pulumi.get(self, "organization")

    @organization.setter
    def organization(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The slug of the project the plugin should be enabled for.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


class SentryRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action_match: Optional[pulumi.Input[str]] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]] = None,
                 conditions: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]] = None,
                 environment: Optional[pulumi.Input[str]] = None,
                 filter_match: Optional[pulumi.Input[str]] = None,
                 filters: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]] = None,
                 frequency: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## # SentryRule Resource

        Sentry Rule resource. Note that there's no public documentation for the values of conditions, filters, and actions. You can either inspect the request payload sent when creating or editing an alert rule on Sentry or inspect [Sentry's rules registry in the source code](https://github.com/getsentry/sentry/tree/master/src/sentry/rules).

        ## Example Usage

        ```python
        import pulumi
        import pulumiverse_sentry as sentry

        # Create a plugin
        default = sentry.SentryRule("default",
            action_match="any",
            actions=[{
                "id": "sentry.mail.actions.NotifyEmailAction",
                "name": "Send an email to IssueOwners",
                "targetIdentifier": "",
                "targetType": "IssueOwners",
            }],
            conditions=[{
                "id": "sentry.rules.conditions.first_seen_event.FirstSeenEventCondition",
                "name": "A new issue is created",
            }],
            environment="production",
            filters=[{
                "id": "sentry.rules.filters.assigned_to.AssignedToFilter",
                "targetType": "Unassigned",
            }],
            frequency=30,
            organization="my-organization",
            project="web-app")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action_match: Use `all` to trigger alerting when all conditions are met, and `any` when at. least a condition is met. Defaults to `any`.
        :param pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]] actions: List of actions.
        :param pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]] conditions: List of conditions.
        :param pulumi.Input[str] environment: Environment for these conditions to apply to.
        :param pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]] filters: List of filters.
        :param pulumi.Input[int] frequency: Perform actions at most once every `X` minutes for this issue. Defaults to `30`.
        :param pulumi.Input[str] name: Name for this alert.
        :param pulumi.Input[str] organization: The slug of the organization the plugin should be enabled for.
        :param pulumi.Input[str] project: The slug of the project the plugin should be enabled for.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SentryRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## # SentryRule Resource

        Sentry Rule resource. Note that there's no public documentation for the values of conditions, filters, and actions. You can either inspect the request payload sent when creating or editing an alert rule on Sentry or inspect [Sentry's rules registry in the source code](https://github.com/getsentry/sentry/tree/master/src/sentry/rules).

        ## Example Usage

        ```python
        import pulumi
        import pulumiverse_sentry as sentry

        # Create a plugin
        default = sentry.SentryRule("default",
            action_match="any",
            actions=[{
                "id": "sentry.mail.actions.NotifyEmailAction",
                "name": "Send an email to IssueOwners",
                "targetIdentifier": "",
                "targetType": "IssueOwners",
            }],
            conditions=[{
                "id": "sentry.rules.conditions.first_seen_event.FirstSeenEventCondition",
                "name": "A new issue is created",
            }],
            environment="production",
            filters=[{
                "id": "sentry.rules.filters.assigned_to.AssignedToFilter",
                "targetType": "Unassigned",
            }],
            frequency=30,
            organization="my-organization",
            project="web-app")
        ```

        :param str resource_name: The name of the resource.
        :param SentryRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SentryRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action_match: Optional[pulumi.Input[str]] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]] = None,
                 conditions: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]] = None,
                 environment: Optional[pulumi.Input[str]] = None,
                 filter_match: Optional[pulumi.Input[str]] = None,
                 filters: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]] = None,
                 frequency: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 organization: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
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
            __props__ = SentryRuleArgs.__new__(SentryRuleArgs)

            __props__.__dict__["action_match"] = action_match
            if actions is None and not opts.urn:
                raise TypeError("Missing required property 'actions'")
            __props__.__dict__["actions"] = actions
            if conditions is None and not opts.urn:
                raise TypeError("Missing required property 'conditions'")
            __props__.__dict__["conditions"] = conditions
            __props__.__dict__["environment"] = environment
            __props__.__dict__["filter_match"] = filter_match
            __props__.__dict__["filters"] = filters
            __props__.__dict__["frequency"] = frequency
            __props__.__dict__["name"] = name
            if organization is None and not opts.urn:
                raise TypeError("Missing required property 'organization'")
            __props__.__dict__["organization"] = organization
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
        super(SentryRule, __self__).__init__(
            'sentry:index/sentryRule:SentryRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            action_match: Optional[pulumi.Input[str]] = None,
            actions: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]] = None,
            conditions: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]] = None,
            environment: Optional[pulumi.Input[str]] = None,
            filter_match: Optional[pulumi.Input[str]] = None,
            filters: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]]] = None,
            frequency: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            organization: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None) -> 'SentryRule':
        """
        Get an existing SentryRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action_match: Use `all` to trigger alerting when all conditions are met, and `any` when at. least a condition is met. Defaults to `any`.
        :param pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]] actions: List of actions.
        :param pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]] conditions: List of conditions.
        :param pulumi.Input[str] environment: Environment for these conditions to apply to.
        :param pulumi.Input[Sequence[pulumi.Input[Mapping[str, Any]]]] filters: List of filters.
        :param pulumi.Input[int] frequency: Perform actions at most once every `X` minutes for this issue. Defaults to `30`.
        :param pulumi.Input[str] name: Name for this alert.
        :param pulumi.Input[str] organization: The slug of the organization the plugin should be enabled for.
        :param pulumi.Input[str] project: The slug of the project the plugin should be enabled for.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SentryRuleState.__new__(_SentryRuleState)

        __props__.__dict__["action_match"] = action_match
        __props__.__dict__["actions"] = actions
        __props__.__dict__["conditions"] = conditions
        __props__.__dict__["environment"] = environment
        __props__.__dict__["filter_match"] = filter_match
        __props__.__dict__["filters"] = filters
        __props__.__dict__["frequency"] = frequency
        __props__.__dict__["name"] = name
        __props__.__dict__["organization"] = organization
        __props__.__dict__["project"] = project
        return SentryRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="actionMatch")
    def action_match(self) -> pulumi.Output[str]:
        """
        Use `all` to trigger alerting when all conditions are met, and `any` when at. least a condition is met. Defaults to `any`.
        """
        return pulumi.get(self, "action_match")

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Output[Sequence[Mapping[str, Any]]]:
        """
        List of actions.
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def conditions(self) -> pulumi.Output[Sequence[Mapping[str, Any]]]:
        """
        List of conditions.
        """
        return pulumi.get(self, "conditions")

    @property
    @pulumi.getter
    def environment(self) -> pulumi.Output[str]:
        """
        Environment for these conditions to apply to.
        """
        return pulumi.get(self, "environment")

    @property
    @pulumi.getter(name="filterMatch")
    def filter_match(self) -> pulumi.Output[str]:
        return pulumi.get(self, "filter_match")

    @property
    @pulumi.getter
    def filters(self) -> pulumi.Output[Optional[Sequence[Mapping[str, Any]]]]:
        """
        List of filters.
        """
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def frequency(self) -> pulumi.Output[int]:
        """
        Perform actions at most once every `X` minutes for this issue. Defaults to `30`.
        """
        return pulumi.get(self, "frequency")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name for this alert.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def organization(self) -> pulumi.Output[str]:
        """
        The slug of the organization the plugin should be enabled for.
        """
        return pulumi.get(self, "organization")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The slug of the project the plugin should be enabled for.
        """
        return pulumi.get(self, "project")

