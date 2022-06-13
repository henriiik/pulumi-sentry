// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package sentry

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// ## # SentryOrganization Resource
//
// Sentry Organization resource.
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
// 		_, err := sentry.NewSentryOrganization(ctx, "default", &sentry.SentryOrganizationArgs{
// 			AgreeTerms: pulumi.Bool(true),
// 			Slug:       pulumi.String("my-organization"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Import
//
// This resource can be imported using an ID made up of the organization slugbash
//
// ```sh
//  $ pulumi import sentry:index/sentryOrganization:SentryOrganization default org-slug
// ```
type SentryOrganization struct {
	pulumi.CustomResourceState

	// You agree to the applicable terms of service and privacy policy.
	AgreeTerms pulumi.BoolOutput `pulumi:"agreeTerms"`
	// The human readable name for the organization.
	Name pulumi.StringOutput `pulumi:"name"`
	// The unique URL slug for this organization. If this is not provided a slug is automatically generated based on the name.
	Slug pulumi.StringOutput `pulumi:"slug"`
}

// NewSentryOrganization registers a new resource with the given unique name, arguments, and options.
func NewSentryOrganization(ctx *pulumi.Context,
	name string, args *SentryOrganizationArgs, opts ...pulumi.ResourceOption) (*SentryOrganization, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AgreeTerms == nil {
		return nil, errors.New("invalid value for required argument 'AgreeTerms'")
	}
	opts = pkgResourceDefaultOpts(opts)
	var resource SentryOrganization
	err := ctx.RegisterResource("sentry:index/sentryOrganization:SentryOrganization", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSentryOrganization gets an existing SentryOrganization resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSentryOrganization(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SentryOrganizationState, opts ...pulumi.ResourceOption) (*SentryOrganization, error) {
	var resource SentryOrganization
	err := ctx.ReadResource("sentry:index/sentryOrganization:SentryOrganization", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SentryOrganization resources.
type sentryOrganizationState struct {
	// You agree to the applicable terms of service and privacy policy.
	AgreeTerms *bool `pulumi:"agreeTerms"`
	// The human readable name for the organization.
	Name *string `pulumi:"name"`
	// The unique URL slug for this organization. If this is not provided a slug is automatically generated based on the name.
	Slug *string `pulumi:"slug"`
}

type SentryOrganizationState struct {
	// You agree to the applicable terms of service and privacy policy.
	AgreeTerms pulumi.BoolPtrInput
	// The human readable name for the organization.
	Name pulumi.StringPtrInput
	// The unique URL slug for this organization. If this is not provided a slug is automatically generated based on the name.
	Slug pulumi.StringPtrInput
}

func (SentryOrganizationState) ElementType() reflect.Type {
	return reflect.TypeOf((*sentryOrganizationState)(nil)).Elem()
}

type sentryOrganizationArgs struct {
	// You agree to the applicable terms of service and privacy policy.
	AgreeTerms bool `pulumi:"agreeTerms"`
	// The human readable name for the organization.
	Name *string `pulumi:"name"`
	// The unique URL slug for this organization. If this is not provided a slug is automatically generated based on the name.
	Slug *string `pulumi:"slug"`
}

// The set of arguments for constructing a SentryOrganization resource.
type SentryOrganizationArgs struct {
	// You agree to the applicable terms of service and privacy policy.
	AgreeTerms pulumi.BoolInput
	// The human readable name for the organization.
	Name pulumi.StringPtrInput
	// The unique URL slug for this organization. If this is not provided a slug is automatically generated based on the name.
	Slug pulumi.StringPtrInput
}

func (SentryOrganizationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*sentryOrganizationArgs)(nil)).Elem()
}

type SentryOrganizationInput interface {
	pulumi.Input

	ToSentryOrganizationOutput() SentryOrganizationOutput
	ToSentryOrganizationOutputWithContext(ctx context.Context) SentryOrganizationOutput
}

func (*SentryOrganization) ElementType() reflect.Type {
	return reflect.TypeOf((**SentryOrganization)(nil)).Elem()
}

func (i *SentryOrganization) ToSentryOrganizationOutput() SentryOrganizationOutput {
	return i.ToSentryOrganizationOutputWithContext(context.Background())
}

func (i *SentryOrganization) ToSentryOrganizationOutputWithContext(ctx context.Context) SentryOrganizationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SentryOrganizationOutput)
}

// SentryOrganizationArrayInput is an input type that accepts SentryOrganizationArray and SentryOrganizationArrayOutput values.
// You can construct a concrete instance of `SentryOrganizationArrayInput` via:
//
//          SentryOrganizationArray{ SentryOrganizationArgs{...} }
type SentryOrganizationArrayInput interface {
	pulumi.Input

	ToSentryOrganizationArrayOutput() SentryOrganizationArrayOutput
	ToSentryOrganizationArrayOutputWithContext(context.Context) SentryOrganizationArrayOutput
}

type SentryOrganizationArray []SentryOrganizationInput

func (SentryOrganizationArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*SentryOrganization)(nil)).Elem()
}

func (i SentryOrganizationArray) ToSentryOrganizationArrayOutput() SentryOrganizationArrayOutput {
	return i.ToSentryOrganizationArrayOutputWithContext(context.Background())
}

func (i SentryOrganizationArray) ToSentryOrganizationArrayOutputWithContext(ctx context.Context) SentryOrganizationArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SentryOrganizationArrayOutput)
}

// SentryOrganizationMapInput is an input type that accepts SentryOrganizationMap and SentryOrganizationMapOutput values.
// You can construct a concrete instance of `SentryOrganizationMapInput` via:
//
//          SentryOrganizationMap{ "key": SentryOrganizationArgs{...} }
type SentryOrganizationMapInput interface {
	pulumi.Input

	ToSentryOrganizationMapOutput() SentryOrganizationMapOutput
	ToSentryOrganizationMapOutputWithContext(context.Context) SentryOrganizationMapOutput
}

type SentryOrganizationMap map[string]SentryOrganizationInput

func (SentryOrganizationMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*SentryOrganization)(nil)).Elem()
}

func (i SentryOrganizationMap) ToSentryOrganizationMapOutput() SentryOrganizationMapOutput {
	return i.ToSentryOrganizationMapOutputWithContext(context.Background())
}

func (i SentryOrganizationMap) ToSentryOrganizationMapOutputWithContext(ctx context.Context) SentryOrganizationMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SentryOrganizationMapOutput)
}

type SentryOrganizationOutput struct{ *pulumi.OutputState }

func (SentryOrganizationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SentryOrganization)(nil)).Elem()
}

func (o SentryOrganizationOutput) ToSentryOrganizationOutput() SentryOrganizationOutput {
	return o
}

func (o SentryOrganizationOutput) ToSentryOrganizationOutputWithContext(ctx context.Context) SentryOrganizationOutput {
	return o
}

type SentryOrganizationArrayOutput struct{ *pulumi.OutputState }

func (SentryOrganizationArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*SentryOrganization)(nil)).Elem()
}

func (o SentryOrganizationArrayOutput) ToSentryOrganizationArrayOutput() SentryOrganizationArrayOutput {
	return o
}

func (o SentryOrganizationArrayOutput) ToSentryOrganizationArrayOutputWithContext(ctx context.Context) SentryOrganizationArrayOutput {
	return o
}

func (o SentryOrganizationArrayOutput) Index(i pulumi.IntInput) SentryOrganizationOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *SentryOrganization {
		return vs[0].([]*SentryOrganization)[vs[1].(int)]
	}).(SentryOrganizationOutput)
}

type SentryOrganizationMapOutput struct{ *pulumi.OutputState }

func (SentryOrganizationMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*SentryOrganization)(nil)).Elem()
}

func (o SentryOrganizationMapOutput) ToSentryOrganizationMapOutput() SentryOrganizationMapOutput {
	return o
}

func (o SentryOrganizationMapOutput) ToSentryOrganizationMapOutputWithContext(ctx context.Context) SentryOrganizationMapOutput {
	return o
}

func (o SentryOrganizationMapOutput) MapIndex(k pulumi.StringInput) SentryOrganizationOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *SentryOrganization {
		return vs[0].(map[string]*SentryOrganization)[vs[1].(string)]
	}).(SentryOrganizationOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SentryOrganizationInput)(nil)).Elem(), &SentryOrganization{})
	pulumi.RegisterInputType(reflect.TypeOf((*SentryOrganizationArrayInput)(nil)).Elem(), SentryOrganizationArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*SentryOrganizationMapInput)(nil)).Elem(), SentryOrganizationMap{})
	pulumi.RegisterOutputType(SentryOrganizationOutput{})
	pulumi.RegisterOutputType(SentryOrganizationArrayOutput{})
	pulumi.RegisterOutputType(SentryOrganizationMapOutput{})
}
