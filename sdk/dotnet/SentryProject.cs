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
    /// ## # sentry.SentryProject Resource
    /// 
    /// Sentry Project resource.
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
    ///         // Create a project
    ///         var @default = new Sentry.SentryProject("default", new Sentry.SentryProjectArgs
    ///         {
    ///             Organization = "my-organization",
    ///             Platform = "javascript",
    ///             ResolveAge = 720,
    ///             Slug = "web-app",
    ///             Team = "my-team",
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
    ///  $ pulumi import sentry:index/sentryProject:SentryProject default org-slug/project-slug
    /// ```
    /// </summary>
    [SentryResourceType("sentry:index/sentryProject:SentryProject")]
    public partial class SentryProject : Pulumi.CustomResource
    {
        [Output("color")]
        public Output<string> Color { get; private set; } = null!;

        /// <summary>
        /// The maximum amount of time (in seconds) to wait between scheduling digests for delivery.
        /// </summary>
        [Output("digestsMaxDelay")]
        public Output<int> DigestsMaxDelay { get; private set; } = null!;

        /// <summary>
        /// The minimum amount of time (in seconds) to wait between scheduling digests for delivery after the initial scheduling.
        /// </summary>
        [Output("digestsMinDelay")]
        public Output<int> DigestsMinDelay { get; private set; } = null!;

        [Output("features")]
        public Output<ImmutableArray<string>> Features { get; private set; } = null!;

        [Output("isBookmarked")]
        public Output<bool> IsBookmarked { get; private set; } = null!;

        [Output("isPublic")]
        public Output<bool> IsPublic { get; private set; } = null!;

        /// <summary>
        /// The human readable name for the project.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The slug of the organization the project should be created for.
        /// </summary>
        [Output("organization")]
        public Output<string> Organization { get; private set; } = null!;

        /// <summary>
        /// The integration platform.
        /// </summary>
        [Output("platform")]
        public Output<string> Platform { get; private set; } = null!;

        [Output("projectId")]
        public Output<string> ProjectId { get; private set; } = null!;

        /// <summary>
        /// Hours in which an issue is automatically resolve if not seen after this amount of time.
        /// </summary>
        [Output("resolveAge")]
        public Output<int> ResolveAge { get; private set; } = null!;

        /// <summary>
        /// The unique URL slug for this project. If this is not provided a slug is automatically generated based on the name.
        /// </summary>
        [Output("slug")]
        public Output<string> Slug { get; private set; } = null!;

        [Output("status")]
        public Output<string> Status { get; private set; } = null!;

        /// <summary>
        /// The slug of the team the project should be created for.
        /// </summary>
        [Output("team")]
        public Output<string> Team { get; private set; } = null!;


        /// <summary>
        /// Create a SentryProject resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SentryProject(string name, SentryProjectArgs args, CustomResourceOptions? options = null)
            : base("sentry:index/sentryProject:SentryProject", name, args ?? new SentryProjectArgs(), MakeResourceOptions(options, ""))
        {
        }

        private SentryProject(string name, Input<string> id, SentryProjectState? state = null, CustomResourceOptions? options = null)
            : base("sentry:index/sentryProject:SentryProject", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing SentryProject resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SentryProject Get(string name, Input<string> id, SentryProjectState? state = null, CustomResourceOptions? options = null)
        {
            return new SentryProject(name, id, state, options);
        }
    }

    public sealed class SentryProjectArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The maximum amount of time (in seconds) to wait between scheduling digests for delivery.
        /// </summary>
        [Input("digestsMaxDelay")]
        public Input<int>? DigestsMaxDelay { get; set; }

        /// <summary>
        /// The minimum amount of time (in seconds) to wait between scheduling digests for delivery after the initial scheduling.
        /// </summary>
        [Input("digestsMinDelay")]
        public Input<int>? DigestsMinDelay { get; set; }

        /// <summary>
        /// The human readable name for the project.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The slug of the organization the project should be created for.
        /// </summary>
        [Input("organization", required: true)]
        public Input<string> Organization { get; set; } = null!;

        /// <summary>
        /// The integration platform.
        /// </summary>
        [Input("platform")]
        public Input<string>? Platform { get; set; }

        /// <summary>
        /// Hours in which an issue is automatically resolve if not seen after this amount of time.
        /// </summary>
        [Input("resolveAge")]
        public Input<int>? ResolveAge { get; set; }

        /// <summary>
        /// The unique URL slug for this project. If this is not provided a slug is automatically generated based on the name.
        /// </summary>
        [Input("slug")]
        public Input<string>? Slug { get; set; }

        /// <summary>
        /// The slug of the team the project should be created for.
        /// </summary>
        [Input("team", required: true)]
        public Input<string> Team { get; set; } = null!;

        public SentryProjectArgs()
        {
        }
    }

    public sealed class SentryProjectState : Pulumi.ResourceArgs
    {
        [Input("color")]
        public Input<string>? Color { get; set; }

        /// <summary>
        /// The maximum amount of time (in seconds) to wait between scheduling digests for delivery.
        /// </summary>
        [Input("digestsMaxDelay")]
        public Input<int>? DigestsMaxDelay { get; set; }

        /// <summary>
        /// The minimum amount of time (in seconds) to wait between scheduling digests for delivery after the initial scheduling.
        /// </summary>
        [Input("digestsMinDelay")]
        public Input<int>? DigestsMinDelay { get; set; }

        [Input("features")]
        private InputList<string>? _features;
        public InputList<string> Features
        {
            get => _features ?? (_features = new InputList<string>());
            set => _features = value;
        }

        [Input("isBookmarked")]
        public Input<bool>? IsBookmarked { get; set; }

        [Input("isPublic")]
        public Input<bool>? IsPublic { get; set; }

        /// <summary>
        /// The human readable name for the project.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The slug of the organization the project should be created for.
        /// </summary>
        [Input("organization")]
        public Input<string>? Organization { get; set; }

        /// <summary>
        /// The integration platform.
        /// </summary>
        [Input("platform")]
        public Input<string>? Platform { get; set; }

        [Input("projectId")]
        public Input<string>? ProjectId { get; set; }

        /// <summary>
        /// Hours in which an issue is automatically resolve if not seen after this amount of time.
        /// </summary>
        [Input("resolveAge")]
        public Input<int>? ResolveAge { get; set; }

        /// <summary>
        /// The unique URL slug for this project. If this is not provided a slug is automatically generated based on the name.
        /// </summary>
        [Input("slug")]
        public Input<string>? Slug { get; set; }

        [Input("status")]
        public Input<string>? Status { get; set; }

        /// <summary>
        /// The slug of the team the project should be created for.
        /// </summary>
        [Input("team")]
        public Input<string>? Team { get; set; }

        public SentryProjectState()
        {
        }
    }
}
