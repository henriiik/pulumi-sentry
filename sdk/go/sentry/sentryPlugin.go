// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package sentry

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// ## # SentryPlugin Resource
//
// Sentry Plugin resource.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-sentry/sdk/go/sentry"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := sentry.NewSentryPlugin(ctx, "default", &sentry.SentryPluginArgs{
// 			Config: pulumi.AnyMap{
// 				"webhook": pulumi.Any("slack://webhook"),
// 			},
// 			Organization: pulumi.String("my-organization"),
// 			Plugin:       pulumi.String("slack"),
// 			Project:      pulumi.String("web-app"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type SentryPlugin struct {
	pulumi.CustomResourceState

	// Configuration of the plugin.
	Config pulumi.MapOutput `pulumi:"config"`
	// The slug of the organization the plugin should be enabled for.
	Organization pulumi.StringOutput `pulumi:"organization"`
	// Identifier of the plugin.
	Plugin pulumi.StringOutput `pulumi:"plugin"`
	// The slug of the project the plugin should be enabled for.
	Project pulumi.StringOutput `pulumi:"project"`
}

// NewSentryPlugin registers a new resource with the given unique name, arguments, and options.
func NewSentryPlugin(ctx *pulumi.Context,
	name string, args *SentryPluginArgs, opts ...pulumi.ResourceOption) (*SentryPlugin, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Organization == nil {
		return nil, errors.New("invalid value for required argument 'Organization'")
	}
	if args.Plugin == nil {
		return nil, errors.New("invalid value for required argument 'Plugin'")
	}
	if args.Project == nil {
		return nil, errors.New("invalid value for required argument 'Project'")
	}
	opts = pkgResourceDefaultOpts(opts)
	var resource SentryPlugin
	err := ctx.RegisterResource("sentry:index/sentryPlugin:SentryPlugin", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSentryPlugin gets an existing SentryPlugin resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSentryPlugin(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SentryPluginState, opts ...pulumi.ResourceOption) (*SentryPlugin, error) {
	var resource SentryPlugin
	err := ctx.ReadResource("sentry:index/sentryPlugin:SentryPlugin", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SentryPlugin resources.
type sentryPluginState struct {
	// Configuration of the plugin.
	Config map[string]interface{} `pulumi:"config"`
	// The slug of the organization the plugin should be enabled for.
	Organization *string `pulumi:"organization"`
	// Identifier of the plugin.
	Plugin *string `pulumi:"plugin"`
	// The slug of the project the plugin should be enabled for.
	Project *string `pulumi:"project"`
}

type SentryPluginState struct {
	// Configuration of the plugin.
	Config pulumi.MapInput
	// The slug of the organization the plugin should be enabled for.
	Organization pulumi.StringPtrInput
	// Identifier of the plugin.
	Plugin pulumi.StringPtrInput
	// The slug of the project the plugin should be enabled for.
	Project pulumi.StringPtrInput
}

func (SentryPluginState) ElementType() reflect.Type {
	return reflect.TypeOf((*sentryPluginState)(nil)).Elem()
}

type sentryPluginArgs struct {
	// Configuration of the plugin.
	Config map[string]interface{} `pulumi:"config"`
	// The slug of the organization the plugin should be enabled for.
	Organization string `pulumi:"organization"`
	// Identifier of the plugin.
	Plugin string `pulumi:"plugin"`
	// The slug of the project the plugin should be enabled for.
	Project string `pulumi:"project"`
}

// The set of arguments for constructing a SentryPlugin resource.
type SentryPluginArgs struct {
	// Configuration of the plugin.
	Config pulumi.MapInput
	// The slug of the organization the plugin should be enabled for.
	Organization pulumi.StringInput
	// Identifier of the plugin.
	Plugin pulumi.StringInput
	// The slug of the project the plugin should be enabled for.
	Project pulumi.StringInput
}

func (SentryPluginArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*sentryPluginArgs)(nil)).Elem()
}

type SentryPluginInput interface {
	pulumi.Input

	ToSentryPluginOutput() SentryPluginOutput
	ToSentryPluginOutputWithContext(ctx context.Context) SentryPluginOutput
}

func (*SentryPlugin) ElementType() reflect.Type {
	return reflect.TypeOf((**SentryPlugin)(nil)).Elem()
}

func (i *SentryPlugin) ToSentryPluginOutput() SentryPluginOutput {
	return i.ToSentryPluginOutputWithContext(context.Background())
}

func (i *SentryPlugin) ToSentryPluginOutputWithContext(ctx context.Context) SentryPluginOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SentryPluginOutput)
}

// SentryPluginArrayInput is an input type that accepts SentryPluginArray and SentryPluginArrayOutput values.
// You can construct a concrete instance of `SentryPluginArrayInput` via:
//
//          SentryPluginArray{ SentryPluginArgs{...} }
type SentryPluginArrayInput interface {
	pulumi.Input

	ToSentryPluginArrayOutput() SentryPluginArrayOutput
	ToSentryPluginArrayOutputWithContext(context.Context) SentryPluginArrayOutput
}

type SentryPluginArray []SentryPluginInput

func (SentryPluginArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*SentryPlugin)(nil)).Elem()
}

func (i SentryPluginArray) ToSentryPluginArrayOutput() SentryPluginArrayOutput {
	return i.ToSentryPluginArrayOutputWithContext(context.Background())
}

func (i SentryPluginArray) ToSentryPluginArrayOutputWithContext(ctx context.Context) SentryPluginArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SentryPluginArrayOutput)
}

// SentryPluginMapInput is an input type that accepts SentryPluginMap and SentryPluginMapOutput values.
// You can construct a concrete instance of `SentryPluginMapInput` via:
//
//          SentryPluginMap{ "key": SentryPluginArgs{...} }
type SentryPluginMapInput interface {
	pulumi.Input

	ToSentryPluginMapOutput() SentryPluginMapOutput
	ToSentryPluginMapOutputWithContext(context.Context) SentryPluginMapOutput
}

type SentryPluginMap map[string]SentryPluginInput

func (SentryPluginMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*SentryPlugin)(nil)).Elem()
}

func (i SentryPluginMap) ToSentryPluginMapOutput() SentryPluginMapOutput {
	return i.ToSentryPluginMapOutputWithContext(context.Background())
}

func (i SentryPluginMap) ToSentryPluginMapOutputWithContext(ctx context.Context) SentryPluginMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SentryPluginMapOutput)
}

type SentryPluginOutput struct{ *pulumi.OutputState }

func (SentryPluginOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SentryPlugin)(nil)).Elem()
}

func (o SentryPluginOutput) ToSentryPluginOutput() SentryPluginOutput {
	return o
}

func (o SentryPluginOutput) ToSentryPluginOutputWithContext(ctx context.Context) SentryPluginOutput {
	return o
}

type SentryPluginArrayOutput struct{ *pulumi.OutputState }

func (SentryPluginArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*SentryPlugin)(nil)).Elem()
}

func (o SentryPluginArrayOutput) ToSentryPluginArrayOutput() SentryPluginArrayOutput {
	return o
}

func (o SentryPluginArrayOutput) ToSentryPluginArrayOutputWithContext(ctx context.Context) SentryPluginArrayOutput {
	return o
}

func (o SentryPluginArrayOutput) Index(i pulumi.IntInput) SentryPluginOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *SentryPlugin {
		return vs[0].([]*SentryPlugin)[vs[1].(int)]
	}).(SentryPluginOutput)
}

type SentryPluginMapOutput struct{ *pulumi.OutputState }

func (SentryPluginMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*SentryPlugin)(nil)).Elem()
}

func (o SentryPluginMapOutput) ToSentryPluginMapOutput() SentryPluginMapOutput {
	return o
}

func (o SentryPluginMapOutput) ToSentryPluginMapOutputWithContext(ctx context.Context) SentryPluginMapOutput {
	return o
}

func (o SentryPluginMapOutput) MapIndex(k pulumi.StringInput) SentryPluginOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *SentryPlugin {
		return vs[0].(map[string]*SentryPlugin)[vs[1].(string)]
	}).(SentryPluginOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SentryPluginInput)(nil)).Elem(), &SentryPlugin{})
	pulumi.RegisterInputType(reflect.TypeOf((*SentryPluginArrayInput)(nil)).Elem(), SentryPluginArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*SentryPluginMapInput)(nil)).Elem(), SentryPluginMap{})
	pulumi.RegisterOutputType(SentryPluginOutput{})
	pulumi.RegisterOutputType(SentryPluginArrayOutput{})
	pulumi.RegisterOutputType(SentryPluginMapOutput{})
}
