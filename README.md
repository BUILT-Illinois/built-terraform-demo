# B[U]ILT Terraform Demo

Welcome to B[U]ILT's Terraform demo. This demo provides a starting point for provisioning a Lambda resource on Amazon Web Services (AWS) via Terraform. This is an example of Terraform modules, variables, and AWS policy attachments.

## Getting Started

 Here are some great resources to get started on Terraform and AWS if needed.
 
 1. [AWS Lambda Terraform Documentation](https://registry.terraform.io/providers/-/aws/latest/docs/resources/lambda_function)
 2. [Learn About Serverless AWS Lambda](https://aws.amazon.com/lambda/)
 3. [What is Terraform?](https://developer.hashicorp.com/terraform/intro)

### Running Terraform w/ OpenTofu
Ready to provision your AWS Lambda? Run the following commands to initiate your Terraform backend, make a plan, then apply the plan to AWS.
```
tofu init
tofu plan
tofu apply
```

## Important Files

```main.tf```

will be where all modules are declared for actual use in a Terraform plan.

```providers.tf```

defines where the Terraform state files should exist and what type of cloud provider we are using. This file is important as it guides Terraform to correctly interpret our module and resource definitions.

```iam.tf```

defines AWS roles that contain policies. These roles can be attached to resources and will allow resources to perform certain functionalities across the AWS suite.

```/src``` 

encapsulates all code that AWS Lambda will use and host. The zip file contains compressed code and is used by Terraform to send off to AWS.

```/modules/lambda``` 

is where the module defintion for a lambda resource is defined. This code alone will not make a resource, it must first be defined in the home directory's ```main.tf```. You can think of this module as a function definition, it is not used until it is called.

```/modules/lambda/lambda.tf```

This Terraform file provides the actual declaration of the AWS Lambda resource. Look through the Terraform blocks and try to find what language is being used and where we point to the source code!

```/modules/lambda/outputs.tf```

This Terraform file provides any outputs that we may have from ```lambda.tf```. These outputs can then be used by other modules if you pass the variables in ```main.tf```.

```/modules/lambda/variables.tf```

This Terraform file declares any variables that lambda takes in. These variables will all need to be filled when the module is declared in ```main.tf```. ```lambda.tf``` can then use these variables in its block defintions.