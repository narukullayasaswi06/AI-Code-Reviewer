from langchain_core.prompts import PromptTemplate

review_prompt=PromptTemplate(
input_variables=["lamguage","review_type","code"],
template="""
You are good at coding!.

Review this {language} code.

Review Type:{review_type}

Provide:
1.Summary
2.Syntax Errors
3.Logic Errors
4.Performance Tmprovements
5.Security Issues
6.Best Practises
7.Improved Code
8.Explanation

Code:
```{language}
{code}
```
Return Markdown.
""")