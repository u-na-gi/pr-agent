class HelpMessage:
    @staticmethod
    def get_general_commands_text():
       commands_text = "> - **/review**: Request a review of your Pull Request.   \n" \
                "> - **/describe**: Update the PR title and description based on the contents of the PR.   \n" \
                "> - **/improve [--extended]**: Suggest code improvements. Extended mode provides a higher quality feedback.   \n" \
                "> - **/ask \\<QUESTION\\>**: Ask a question about the PR.   \n" \
                "> - **/update_changelog**: Update the changelog based on the PR's contents.   \n" \
                "> - **/add_docs** 💎: Generate docstring for new components introduced in the PR.   \n" \
                "> - **/generate_labels** 💎: Generate labels for the PR based on the PR's contents.   \n" \
                "> - **/analyze** 💎: Automatically analyzes the PR, and presents changes walkthrough for each component.   \n\n" \
                ">See the [tools guide](https://github.com/Codium-ai/pr-agent/blob/main/docs/TOOLS_GUIDE.md) for more details.\n" \
                ">To list the possible configuration parameters, add a **/config** comment.   \n"
       return commands_text


    @staticmethod
    def get_general_bot_help_text():
        output = f"> To invoke the PR-Agent, add a comment using one of the following commands:  \n{HelpMessage.get_general_commands_text()} \n"
        return output

    @staticmethod
    def get_review_usage_guide():
        output ="**Overview:**\n"
        output +="The `review` tool scans the PR code changes, and generates a PR review. The tool can be triggered [automatically](https://github.com/Codium-ai/pr-agent/blob/main/Usage.md#github-app-automatic-tools) every time a new PR is opened, or can be invoked manually by commenting on any PR.\n"
        output +="""\
When commenting, to edit [configurations](https://github.com/Codium-ai/pr-agent/blob/main/pr_agent/settings/configuration.toml#L19) related to the review tool (`pr_reviewer` section), use the following template:
```
/review --pr_reviewer.some_config1=... --pr_reviewer.some_config2=...
```
With a [configuration file](https://github.com/Codium-ai/pr-agent/blob/main/Usage.md#working-with-github-app), use the following template:
```
[pr_reviewer]
some_config1=...
some_config2=...
```
    """
        output +="\n\n<table>"

        # extra instructions
        output += "<tr><td><details> <summary><strong> Utilizing extra instructions</strong></summary><hr>\n\n"
        output += '''\
The `review` tool can be configured with extra instructions, which can be used to guide the model to a feedback tailored to the needs of your project.

Be specific, clear, and concise in the instructions. With extra instructions, you are the prompter. Specify the relevant sub-tool, and the relevant aspects of the PR that you want to emphasize.

Examples for extra instructions:
```
[pr_reviewer] # /review #
extra_instructions="""
In the code feedback section, emphasize the following:
- Does the code logic cover relevant edge cases?
- Is the code logic clear and easy to understand?
- Is the code logic efficient?
...
"""
```
Use triple quotes to write multi-line instructions. Use bullet points to make the instructions more readable.
        '''
        output += "\n\n</details></td></tr>\n\n"

        # automation
        output += "<tr><td><details> <summary><strong> How to enable\\disable automation</strong></summary><hr>\n\n"
        output += """\
- When you first install PR-Agent app, the [default mode](https://github.com/Codium-ai/pr-agent/blob/main/Usage.md#github-app-automatic-tools) for the `review` tool is:
```
pr_commands = ["/review", ...]
```
meaning the `review` tool will run automatically on every PR, with the default configuration.
Edit this field to enable/disable the tool, or to change the used configurations
        """
        output += "\n\n</details></td></tr>\n\n"

        # code feedback
        output += "<tr><td><details> <summary><strong> About the 'Code feedback' section</strong></summary><hr>\n\n"
        output+="""\
The `review` tool provides several type of feedbacks, one of them is code suggestions.
If you are interested **only** in the code suggestions, it is recommended to use the [`improve`](https://github.com/Codium-ai/pr-agent/blob/main/docs/IMPROVE.md) feature instead, since it dedicated only to code suggestions, and usually gives better results.
Use the `review` tool if you want to get a more comprehensive feedback, which includes code suggestions as well.
"""
        output += "\n\n</details></td></tr>\n\n"

        # auto-labels
        output += "<tr><td><details> <summary><strong> Auto-labels</strong></summary><hr>\n\n"
        output+="""\
The `review` tool can auto-generate two specific types of labels for a PR:
- a `possible security issue` label, that detects possible [security issues](https://github.com/Codium-ai/pr-agent/blob/tr/user_description/pr_agent/settings/pr_reviewer_prompts.toml#L136) (`enable_review_labels_security` flag)
- a `Review effort [1-5]: x` label, where x is the estimated effort to review the PR (`enable_review_labels_effort` flag)
"""
        output += "\n\n</details></td></tr>\n\n"

        # extra sub-tools
        output += "<tr><td><details> <summary><strong> Extra sub-tools</strong></summary><hr>\n\n"
        output += """\
The `review` tool provides a collection of possible feedbacks about a PR.
It is recommended to review the [possible options](https://github.com/Codium-ai/pr-agent/blob/main/docs/REVIEW.md#enabledisable-features), and choose the ones relevant for your use case.
Some of the feature that are disabled by default are quite useful, and should be considered for enabling. For example: 
`require_score_review`, `require_soc2_review`, `enable_review_labels_effort`, and more.
"""
        output += "\n\n</details></td></tr>\n\n"

        # general
        output += "\n\n<tr><td><details> <summary><strong> More PR-Agent commands</strong></summary><hr> \n\n"
        output += HelpMessage.get_general_bot_help_text()
        output += "\n\n</details></td></tr>\n\n"

        output += "</table>"

        output += f"\n\nSee the [review usage](https://github.com/Codium-ai/pr-agent/blob/main/docs/REVIEW.md) page for a comprehensive guide on using this tool.\n\n"

        return output



    @staticmethod
    def get_describe_usage_guide():
        output = "**Overview:**\n"
        output += "The `describe` tool scans the PR code changes, and generates a description for the PR - title, type, summary, walkthrough and labels. "
        output += "The tool can be triggered [automatically](https://github.com/Codium-ai/pr-agent/blob/main/Usage.md#github-app-automatic-tools) every time a new PR is opened, or can be invoked manually by commenting on a PR.\n"
        output += """\

When commenting, to edit [configurations](https://github.com/Codium-ai/pr-agent/blob/main/pr_agent/settings/configuration.toml#L46) related to the describe tool (`pr_description` section), use the following template:
```
/describe --pr_description.some_config1=... --pr_description.some_config2=...
```
With a [configuration file](https://github.com/Codium-ai/pr-agent/blob/main/Usage.md#working-with-github-app), use the following template:
```
[pr_description]
some_config1=...
some_config2=...
```
"""
        output += "\n\n<table>"

        # automation
        output += "<tr><td><details> <summary><strong> Enabling\\disabling automation </strong></summary><hr>\n\n"
        output += """\
- When you first install the app, the [default mode](https://github.com/Codium-ai/pr-agent/blob/main/Usage.md#github-app-automatic-tools) for the describe tool is:
```
pr_commands = ["/describe --pr_description.add_original_user_description=true" 
                         "--pr_description.keep_original_user_title=true", ...]
```
meaning the `describe` tool will run automatically on every PR, will keep the original title, and will add the original user description above the generated description. 

- Markers are an alternative way to control the generated description, to give maximal control to the user. If you set:
```
pr_commands = ["/describe --pr_description.use_description_markers=true", ...]
```
the tool will replace every marker of the form `pr_agent:marker_name` in the PR description with the relevant content, where `marker_name` is one of the following:
  - `type`: the PR type.
  - `summary`: the PR summary.
  - `walkthrough`: the PR walkthrough.

Note that when markers are enabled, if the original PR description does not contain any markers, the tool will not alter the description at all.
        
"""
        output += "\n\n</details></td></tr>\n\n"

        output += "<tr><td><details> <summary><strong> Custom labels </strong></summary><hr>\n\n"
        output += """\
The default labels of the `describe` tool are quite generic: [`Bug fix`, `Tests`, `Enhancement`, `Documentation`, `Other`].

If you specify [custom labels](https://github.com/Codium-ai/pr-agent/blob/main/docs/DESCRIBE.md#handle-custom-labels-from-the-repos-labels-page-gem) in the repo's labels page or via configuration file, you can get tailored labels for your use cases.
Examples for custom labels:
- `Main topic:performance` - pr_agent:The main topic of this PR is performance
- `New endpoint` - pr_agent:A new endpoint was added in this PR
- `SQL query` - pr_agent:A new SQL query was added in this PR
- `Dockerfile changes` - pr_agent:The PR contains changes in the Dockerfile
- ...

The list above is eclectic, and aims to give an idea of different possibilities. Define custom labels that are relevant for your repo and use cases.
Note that Labels are not mutually exclusive, so you can add multiple label categories.
Make sure to provide proper title, and a detailed and well-phrased description for each label, so the tool will know when to suggest it.        
"""
        output += "\n\n</details></td></tr>\n\n"

        # general
        output += "\n\n<tr><td><details> <summary><strong> More PR-Agent commands</strong></summary><hr> \n\n"
        output += HelpMessage.get_general_bot_help_text()
        output += "\n\n</details></td></tr>\n\n"

        output += "</table>"

        output += f"\n\nSee the [describe usage](https://github.com/Codium-ai/pr-agent/blob/main/docs/DESCRIBE.md) page for a comprehensive guide on using this tool.\n\n"

        return output

    @staticmethod
    def get_ask_usage_guide():
        output = "**Overview:**\n"
        output += """\
The [`ask` tool](https://github.com/Codium-ai/pr-agent/blob/main/docs/ASK.md] answers questions about the PR, based on the PR code changes. Note that the tool does not have "memory" of previous questions, and answers each question independently.
It can be invoked manually by commenting on any PR:
```
/ask "..."
```        
        """
        output += "\n\n<table>"

        # general
        output += "\n\n<tr><td><details> <summary><strong> More PR-Agent commands</strong></summary><hr> \n\n"
        output += HelpMessage.get_general_bot_help_text()
        output += "\n\n</details></td></tr>\n\n"

        output += "</table>"

        output += f"\n\nSee the [review usage](https://github.com/Codium-ai/pr-agent/blob/main/docs/REVIEW.md) page for a comprehensive guide on using this tool.\n\n"

        return output
