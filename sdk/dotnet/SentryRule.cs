// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Sentry
{
    /// <summary>
    /// ## # sentry.SentryRule Resource
    /// 
    /// Sentry Rule resource. Note that there's no public documentation for the values of conditions, filters, and actions. You can either inspect the request payload sent when creating or editing an alert rule on Sentry or inspect [Sentry's rules registry in the source code](https://github.com/getsentry/sentry/tree/master/src/sentry/rules).
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Sentry = Pulumiverse.Sentry;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         // Create a plugin
    ///         var @default = new Sentry.SentryRule("default", new Sentry.SentryRuleArgs
    ///         {
    ///             ActionMatch = "any",
    ///             Actions = 
    ///             {
    ///                 
    ///                 {
    ///                     { "id", "sentry.mail.actions.NotifyEmailAction" },
    ///                     { "name", "Send an email to IssueOwners" },
    ///                     { "targetIdentifier", "" },
    ///                     { "targetType", "IssueOwners" },
    ///                 },
    ///             },
    ///             Conditions = 
    ///             {
    ///                 
    ///                 {
    ///                     { "id", "sentry.rules.conditions.first_seen_event.FirstSeenEventCondition" },
    ///                     { "name", "A new issue is created" },
    ///                 },
    ///             },
    ///             Environment = "production",
    ///             Filters = 
    ///             {
    ///                 
    ///                 {
    ///                     { "id", "sentry.rules.filters.assigned_to.AssignedToFilter" },
    ///                     { "targetType", "Unassigned" },
    ///                 },
    ///             },
    ///             Frequency = 30,
    ///             Organization = "my-organization",
    ///             Project = "web-app",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    [SentryResourceType("sentry:index/sentryRule:SentryRule")]
    public partial class SentryRule : Pulumi.CustomResource
    {
        /// <summary>
        /// Use `all` to trigger alerting when all conditions are met, and `any` when at. least a condition is met. Defaults to `any`.
        /// </summary>
        [Output("actionMatch")]
        public Output<string> ActionMatch { get; private set; } = null!;

        /// <summary>
        /// List of actions.
        /// </summary>
        [Output("actions")]
        public Output<ImmutableArray<ImmutableDictionary<string, object>>> Actions { get; private set; } = null!;

        /// <summary>
        /// List of conditions.
        /// </summary>
        [Output("conditions")]
        public Output<ImmutableArray<ImmutableDictionary<string, object>>> Conditions { get; private set; } = null!;

        /// <summary>
        /// Environment for these conditions to apply to.
        /// </summary>
        [Output("environment")]
        public Output<string> Environment { get; private set; } = null!;

        [Output("filterMatch")]
        public Output<string> FilterMatch { get; private set; } = null!;

        /// <summary>
        /// List of filters.
        /// </summary>
        [Output("filters")]
        public Output<ImmutableArray<ImmutableDictionary<string, object>>> Filters { get; private set; } = null!;

        /// <summary>
        /// Perform actions at most once every `X` minutes for this issue. Defaults to `30`.
        /// </summary>
        [Output("frequency")]
        public Output<int> Frequency { get; private set; } = null!;

        /// <summary>
        /// Name for this alert.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The slug of the organization the plugin should be enabled for.
        /// </summary>
        [Output("organization")]
        public Output<string> Organization { get; private set; } = null!;

        /// <summary>
        /// The slug of the project the plugin should be enabled for.
        /// </summary>
        [Output("project")]
        public Output<string> Project { get; private set; } = null!;


        /// <summary>
        /// Create a SentryRule resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SentryRule(string name, SentryRuleArgs args, CustomResourceOptions? options = null)
            : base("sentry:index/sentryRule:SentryRule", name, args ?? new SentryRuleArgs(), MakeResourceOptions(options, ""))
        {
        }

        private SentryRule(string name, Input<string> id, SentryRuleState? state = null, CustomResourceOptions? options = null)
            : base("sentry:index/sentryRule:SentryRule", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "https://github.com/pulumiverse/pulumi-sentry/releases/download/${VERSION}",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing SentryRule resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SentryRule Get(string name, Input<string> id, SentryRuleState? state = null, CustomResourceOptions? options = null)
        {
            return new SentryRule(name, id, state, options);
        }
    }

    public sealed class SentryRuleArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Use `all` to trigger alerting when all conditions are met, and `any` when at. least a condition is met. Defaults to `any`.
        /// </summary>
        [Input("actionMatch")]
        public Input<string>? ActionMatch { get; set; }

        [Input("actions", required: true)]
        private InputList<ImmutableDictionary<string, object>>? _actions;

        /// <summary>
        /// List of actions.
        /// </summary>
        public InputList<ImmutableDictionary<string, object>> Actions
        {
            get => _actions ?? (_actions = new InputList<ImmutableDictionary<string, object>>());
            set => _actions = value;
        }

        [Input("conditions", required: true)]
        private InputList<ImmutableDictionary<string, object>>? _conditions;

        /// <summary>
        /// List of conditions.
        /// </summary>
        public InputList<ImmutableDictionary<string, object>> Conditions
        {
            get => _conditions ?? (_conditions = new InputList<ImmutableDictionary<string, object>>());
            set => _conditions = value;
        }

        /// <summary>
        /// Environment for these conditions to apply to.
        /// </summary>
        [Input("environment")]
        public Input<string>? Environment { get; set; }

        [Input("filterMatch")]
        public Input<string>? FilterMatch { get; set; }

        [Input("filters")]
        private InputList<ImmutableDictionary<string, object>>? _filters;

        /// <summary>
        /// List of filters.
        /// </summary>
        public InputList<ImmutableDictionary<string, object>> Filters
        {
            get => _filters ?? (_filters = new InputList<ImmutableDictionary<string, object>>());
            set => _filters = value;
        }

        /// <summary>
        /// Perform actions at most once every `X` minutes for this issue. Defaults to `30`.
        /// </summary>
        [Input("frequency")]
        public Input<int>? Frequency { get; set; }

        /// <summary>
        /// Name for this alert.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The slug of the organization the plugin should be enabled for.
        /// </summary>
        [Input("organization", required: true)]
        public Input<string> Organization { get; set; } = null!;

        /// <summary>
        /// The slug of the project the plugin should be enabled for.
        /// </summary>
        [Input("project", required: true)]
        public Input<string> Project { get; set; } = null!;

        public SentryRuleArgs()
        {
        }
    }

    public sealed class SentryRuleState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Use `all` to trigger alerting when all conditions are met, and `any` when at. least a condition is met. Defaults to `any`.
        /// </summary>
        [Input("actionMatch")]
        public Input<string>? ActionMatch { get; set; }

        [Input("actions")]
        private InputList<ImmutableDictionary<string, object>>? _actions;

        /// <summary>
        /// List of actions.
        /// </summary>
        public InputList<ImmutableDictionary<string, object>> Actions
        {
            get => _actions ?? (_actions = new InputList<ImmutableDictionary<string, object>>());
            set => _actions = value;
        }

        [Input("conditions")]
        private InputList<ImmutableDictionary<string, object>>? _conditions;

        /// <summary>
        /// List of conditions.
        /// </summary>
        public InputList<ImmutableDictionary<string, object>> Conditions
        {
            get => _conditions ?? (_conditions = new InputList<ImmutableDictionary<string, object>>());
            set => _conditions = value;
        }

        /// <summary>
        /// Environment for these conditions to apply to.
        /// </summary>
        [Input("environment")]
        public Input<string>? Environment { get; set; }

        [Input("filterMatch")]
        public Input<string>? FilterMatch { get; set; }

        [Input("filters")]
        private InputList<ImmutableDictionary<string, object>>? _filters;

        /// <summary>
        /// List of filters.
        /// </summary>
        public InputList<ImmutableDictionary<string, object>> Filters
        {
            get => _filters ?? (_filters = new InputList<ImmutableDictionary<string, object>>());
            set => _filters = value;
        }

        /// <summary>
        /// Perform actions at most once every `X` minutes for this issue. Defaults to `30`.
        /// </summary>
        [Input("frequency")]
        public Input<int>? Frequency { get; set; }

        /// <summary>
        /// Name for this alert.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The slug of the organization the plugin should be enabled for.
        /// </summary>
        [Input("organization")]
        public Input<string>? Organization { get; set; }

        /// <summary>
        /// The slug of the project the plugin should be enabled for.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        public SentryRuleState()
        {
        }
    }
}
