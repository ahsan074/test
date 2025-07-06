Part 3: Conceptual Understanding & System Proficiency

QUESTION: How would you measure whether your agent is taking the correct action in response to the prompt?

ANSWER: To measure correctness, I would:

Define expected behavior for each type of tool (e.g., weather tool should respond with location-specific weather data). A behavior check is also implemneted in the code.

Create test prompts with known outputs and validate tool selection and response.

Log tool usage and compare it against the intended tool per prompt.


---------------------------------------------------------------
QUESTION: Propose a mechanism to detect conflicting or stale results.

ANSWER: Conflicting or stale results can be detected using the following mechanisms:

Timestamp validation: For APIs like weather, verify if data is real-time or outdated

Redundant querying: Write the same query and match the results.

Versioning: Track tool versions and their data sources to detect inconsistencies.

---------------------------------------------------------------

QUESTION: How do you design system prompts to guide agent behavior effectively?

ANSWER: Effective system prompts are designed by:

Specifying clear role and tone like adding you are helpful assistant and respond politely.

Setting tool usage preferences like always prefer tools when available over generating hallucinated facts.

Outlining fallbacks like if unable to retrive info then say I am unable to retrive information.

---------------------------------------------------------------

QUESTION: What constraints, tone, and structure do you enforce, and how do you test them?

ANSWER: 
Constraints:

Use tools for external data.

Avoid hallucinated or speculative answers.

Use fallbacks for invalid input.

Tone:

Polite and professional.

Structure:

Always prepend SYSTEM_PROMPT.

Include the tool name used in the response JSON.

Testing:

Prompt the agent with varied inputs and verify consistent tone and structure.

Perform unit testing on tool trigger conditions.