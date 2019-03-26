
# Contributing Guidelines

Thanks for helping out Code For life's Rapid Router! Here are a few guildeines to help your contributions to be accepted :)

## Prerequisites

We use Zenhub to track our issues, you can find our workspace [here](https://app.zenhub.com/workspaces/code-for-life-team-56f2afba6e54555c586f6db3/boards?repos=18399425,49142916,22154147,39072690,96999382)

## Submitting an issue

If you find a bug, want to suggest feature request or improvement, please open an issue for it using one of the issue templates.

> One word of caution: please do not add any issues related to security. Evil hackers are everywhere nowadays... If you do find a security issue, let us know using our [contact form][c4l-contact-form].

## Pull Request Guidelines

Once you submit a PR, we will review it via [Reviewable](https://reviewable.io/). To make the review go smoothly we recommend following the guidelines below:

* Include unit tests when you contribute new features, as they help to a) prove that your code works correctly, and b) guard against future breaking changes to lower the maintenance cost.

* Bug fixes also generally require unit tests, because the presence of bugs usually indicates insufficient test coverage.

* Use the [black formatter](https://black.readthedocs.io/en/stable/installation_and_usage.html) on your code.

* When you respond to changes based on comments from a code review, please reply with "Done." so that we get a notification.

We follow [Semantic Versioning](https://semver.org/) in this project. The version automatically gets bumped up based on the content of the PR title and description. For this we follow the [Conventional Commits Specification](https://www.conventionalcommits.org). Please make sure the PR title and description follows this specification.

[c4l-contact-form]: https://www.codeforlife.education/help/#contact
