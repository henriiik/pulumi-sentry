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
    /// ## # sentry.SentryTeam Resource
    /// 
    /// Sentry Team resource.
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
    ///         // Create a team
    ///         var @default = new Sentry.SentryTeam("default", new Sentry.SentryTeamArgs
    ///         {
    ///             Organization = "my-organization",
    ///             Slug = "my-team",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// This resource can be imported using an ID made up of the organization slug and project slugbash
    /// 
    /// ```sh
    ///  $ pulumi import sentry:index/sentryTeam:SentryTeam default org-slug/team-slug
    /// ```
    /// </summary>
    [SentryResourceType("sentry:index/sentryTeam:SentryTeam")]
    public partial class SentryTeam : Pulumi.CustomResource
    {
        [Output("hasAccess")]
        public Output<bool> HasAccess { get; private set; } = null!;

        [Output("isMember")]
        public Output<bool> IsMember { get; private set; } = null!;

        [Output("isPending")]
        public Output<bool> IsPending { get; private set; } = null!;

        /// <summary>
        /// The human readable name for the team.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The slug of the organization the team should be created for.
        /// </summary>
        [Output("organization")]
        public Output<string> Organization { get; private set; } = null!;

        /// <summary>
        /// The unique URL slug for this team. If this is not provided a slug is automatically generated based on the name.
        /// </summary>
        [Output("slug")]
        public Output<string> Slug { get; private set; } = null!;

        [Output("teamId")]
        public Output<string> TeamId { get; private set; } = null!;


        /// <summary>
        /// Create a SentryTeam resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SentryTeam(string name, SentryTeamArgs args, CustomResourceOptions? options = null)
            : base("sentry:index/sentryTeam:SentryTeam", name, args ?? new SentryTeamArgs(), MakeResourceOptions(options, ""))
        {
        }

        private SentryTeam(string name, Input<string> id, SentryTeamState? state = null, CustomResourceOptions? options = null)
            : base("sentry:index/sentryTeam:SentryTeam", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing SentryTeam resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SentryTeam Get(string name, Input<string> id, SentryTeamState? state = null, CustomResourceOptions? options = null)
        {
            return new SentryTeam(name, id, state, options);
        }
    }

    public sealed class SentryTeamArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The human readable name for the team.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The slug of the organization the team should be created for.
        /// </summary>
        [Input("organization", required: true)]
        public Input<string> Organization { get; set; } = null!;

        /// <summary>
        /// The unique URL slug for this team. If this is not provided a slug is automatically generated based on the name.
        /// </summary>
        [Input("slug")]
        public Input<string>? Slug { get; set; }

        public SentryTeamArgs()
        {
        }
    }

    public sealed class SentryTeamState : Pulumi.ResourceArgs
    {
        [Input("hasAccess")]
        public Input<bool>? HasAccess { get; set; }

        [Input("isMember")]
        public Input<bool>? IsMember { get; set; }

        [Input("isPending")]
        public Input<bool>? IsPending { get; set; }

        /// <summary>
        /// The human readable name for the team.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The slug of the organization the team should be created for.
        /// </summary>
        [Input("organization")]
        public Input<string>? Organization { get; set; }

        /// <summary>
        /// The unique URL slug for this team. If this is not provided a slug is automatically generated based on the name.
        /// </summary>
        [Input("slug")]
        public Input<string>? Slug { get; set; }

        [Input("teamId")]
        public Input<string>? TeamId { get; set; }

        public SentryTeamState()
        {
        }
    }
}
