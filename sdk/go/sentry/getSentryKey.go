// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package sentry

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// ## # SentryKey Data Source
//
// Sentry Key data source.
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
// 		_, err := sentry.LookupSentryKey(ctx, &GetSentryKeyArgs{
// 			Name:         pulumi.StringRef("Default"),
// 			Organization: "my-organization",
// 			Project:      "web-app",
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func LookupSentryKey(ctx *pulumi.Context, args *LookupSentryKeyArgs, opts ...pulumi.InvokeOption) (*LookupSentryKeyResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv LookupSentryKeyResult
	err := ctx.Invoke("sentry:index/getSentryKey:getSentryKey", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getSentryKey.
type LookupSentryKeyArgs struct {
	// Boolean flag indicating that we want the first key of the returned keys.
	First *bool `pulumi:"first"`
	// The name of the key to retrieve.
	Name *string `pulumi:"name"`
	// The slug of the organization the key should be created for.
	Organization string `pulumi:"organization"`
	// The slug of the project the key should be created for.
	Project string `pulumi:"project"`
}

// A collection of values returned by getSentryKey.
type LookupSentryKeyResult struct {
	// DSN for the Content Security Policy (CSP) for the key.
	DsnCsp string `pulumi:"dsnCsp"`
	// DSN for the key.
	DsnPublic string `pulumi:"dsnPublic"`
	// DSN (Deprecated) for the key.
	DsnSecret string `pulumi:"dsnSecret"`
	First     *bool  `pulumi:"first"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// Flag indicating the key is active.
	IsActive     bool    `pulumi:"isActive"`
	Name         *string `pulumi:"name"`
	Organization string  `pulumi:"organization"`
	Project      string  `pulumi:"project"`
	// The ID of the project that the key belongs to.
	ProjectId int `pulumi:"projectId"`
	// Public key portion of the client key.
	Public string `pulumi:"public"`
	// Number of events that can be reported within the rate limit window.
	RateLimitCount int `pulumi:"rateLimitCount"`
	// Length of time that will be considered when checking the rate limit.
	RateLimitWindow int `pulumi:"rateLimitWindow"`
	// Secret key portion of the client key.
	Secret string `pulumi:"secret"`
}

func LookupSentryKeyOutput(ctx *pulumi.Context, args LookupSentryKeyOutputArgs, opts ...pulumi.InvokeOption) LookupSentryKeyResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupSentryKeyResult, error) {
			args := v.(LookupSentryKeyArgs)
			r, err := LookupSentryKey(ctx, &args, opts...)
			var s LookupSentryKeyResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupSentryKeyResultOutput)
}

// A collection of arguments for invoking getSentryKey.
type LookupSentryKeyOutputArgs struct {
	// Boolean flag indicating that we want the first key of the returned keys.
	First pulumi.BoolPtrInput `pulumi:"first"`
	// The name of the key to retrieve.
	Name pulumi.StringPtrInput `pulumi:"name"`
	// The slug of the organization the key should be created for.
	Organization pulumi.StringInput `pulumi:"organization"`
	// The slug of the project the key should be created for.
	Project pulumi.StringInput `pulumi:"project"`
}

func (LookupSentryKeyOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSentryKeyArgs)(nil)).Elem()
}

// A collection of values returned by getSentryKey.
type LookupSentryKeyResultOutput struct{ *pulumi.OutputState }

func (LookupSentryKeyResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSentryKeyResult)(nil)).Elem()
}

func (o LookupSentryKeyResultOutput) ToLookupSentryKeyResultOutput() LookupSentryKeyResultOutput {
	return o
}

func (o LookupSentryKeyResultOutput) ToLookupSentryKeyResultOutputWithContext(ctx context.Context) LookupSentryKeyResultOutput {
	return o
}

// DSN for the Content Security Policy (CSP) for the key.
func (o LookupSentryKeyResultOutput) DsnCsp() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSentryKeyResult) string { return v.DsnCsp }).(pulumi.StringOutput)
}

// DSN for the key.
func (o LookupSentryKeyResultOutput) DsnPublic() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSentryKeyResult) string { return v.DsnPublic }).(pulumi.StringOutput)
}

// DSN (Deprecated) for the key.
func (o LookupSentryKeyResultOutput) DsnSecret() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSentryKeyResult) string { return v.DsnSecret }).(pulumi.StringOutput)
}

func (o LookupSentryKeyResultOutput) First() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupSentryKeyResult) *bool { return v.First }).(pulumi.BoolPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupSentryKeyResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSentryKeyResult) string { return v.Id }).(pulumi.StringOutput)
}

// Flag indicating the key is active.
func (o LookupSentryKeyResultOutput) IsActive() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupSentryKeyResult) bool { return v.IsActive }).(pulumi.BoolOutput)
}

func (o LookupSentryKeyResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSentryKeyResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupSentryKeyResultOutput) Organization() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSentryKeyResult) string { return v.Organization }).(pulumi.StringOutput)
}

func (o LookupSentryKeyResultOutput) Project() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSentryKeyResult) string { return v.Project }).(pulumi.StringOutput)
}

// The ID of the project that the key belongs to.
func (o LookupSentryKeyResultOutput) ProjectId() pulumi.IntOutput {
	return o.ApplyT(func(v LookupSentryKeyResult) int { return v.ProjectId }).(pulumi.IntOutput)
}

// Public key portion of the client key.
func (o LookupSentryKeyResultOutput) Public() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSentryKeyResult) string { return v.Public }).(pulumi.StringOutput)
}

// Number of events that can be reported within the rate limit window.
func (o LookupSentryKeyResultOutput) RateLimitCount() pulumi.IntOutput {
	return o.ApplyT(func(v LookupSentryKeyResult) int { return v.RateLimitCount }).(pulumi.IntOutput)
}

// Length of time that will be considered when checking the rate limit.
func (o LookupSentryKeyResultOutput) RateLimitWindow() pulumi.IntOutput {
	return o.ApplyT(func(v LookupSentryKeyResult) int { return v.RateLimitWindow }).(pulumi.IntOutput)
}

// Secret key portion of the client key.
func (o LookupSentryKeyResultOutput) Secret() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSentryKeyResult) string { return v.Secret }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupSentryKeyResultOutput{})
}
