---
description: How I added my CV to my website, and made it editable, so I can easily produce custom CVs for each job role.
---

# You can edit my CV (if you want to)

I'm more actively looking for work right now than I've ever been in the past. It's quite
terrifying, and demoralising.

To make myself seem more attractive, I'm doing up this website (very slowly), and I
thought that I could make my CV look like the website. To follow a similar style, and to
have similar information.

Here it is: [https://www.mayortech.co.uk/cv/](https://www.mayortech.co.uk/cv/)

Then I thought that it would be useful to be able to edit the CV as I needed, to
customise it to fit the particular job/contract I was applying for.

So I did something potentially stupid. I made it so that you can **double click on
almost any bit of text on the CV to make it editable**. You can then change the text,
and then save the page as a PDF. The changes you make aren't saved forever, and they
aren't available for other people to see. It's just local text editing. But it is super
useful to be able to do that.

OK, it's not that stupid. Anyone can already edit the content of a web page they're
looking at, using the developer tools. But this adds `contenteditable` to any `<p>` that
is double clicked, so it's a bit easier.

## Hey, Claude!

My next thought was that now that my CV is online, I can easily ask an AI to compare it
against a job spec. Then I can fix up the CV, and "Easy Apply" with my shiny new PDF.

So I tested it out. I took a job that LinkedIn was promoting to me (not one that I was
particularly well suited for), and asked Claude Sonnet 4 to compare them:

```
Can you review the CV here: https://www.mayortech.co.uk/cv/ and compare it to the job description here: https://www.linkedin.com/jobs/view/4281606944.

Can you tell me what could be changed in the CV to make the candidate more appealing?
```

Claude's response:

````
I'll help you review the CV and compare it to the job description. Let me fetch both documents first.

Fetching...

Based on my review of both documents, here's my analysis of William's CV compared to the job requirements and recommendations for improvement:

## Key Job Requirements vs CV Analysis

### ✅ Strong Matches:
- **Python expertise** - William has extensive Python experience with Django, FastAPI, and Flask
- **AWS experience** - Listed in skills and demonstrated in projects
- **Senior-level experience** - 13 years of experience aligns with Mid-Senior level requirement
- **Backend focus** - CV emphasizes backend development which matches the role

### ⚠️ Gaps That Need Addressing:

1. **TypeScript** - Not mentioned anywhere in the CV, but this is a key requirement
2. **MongoDB & DynamoDB** - PostgreSQL and SQLite3 are listed, but no NoSQL databases mentioned
3. **GCP (Google Cloud Platform)** - Only AWS is mentioned, but job prefers both AWS and GCP
4. **DevOps practices** - While Docker and CI/CD are listed, DevOps expertise isn't prominently featured

## Recommended CV Improvements:

### 1. **Add Missing Technical Skills**
Update the skills section to include:
```/dev/null/skills_additions.txt#L1-4
- TypeScript
- MongoDB
- DynamoDB
- Google Cloud Platform (GCP)
```

### 2. **Enhance DevOps Experience**
Expand the DevOps section in skills to be more prominent:
- DevOps (CI/CD, Infrastructure as Code, containerization)
- Kubernetes
- Terraform (if applicable)

### 3. **Highlight Relevant Project Experience**
In the experience section, emphasize projects that demonstrate the required skills:

- **RFGraph project** - Mention if TypeScript was used or could highlight the sub-100ms latency requirements showing performance optimization skills
- **AXS Passport** - This FastAPI project could be expanded to mention any NoSQL database usage or cloud architecture decisions

### 4. **Add a Contract/Remote Work Statement**
Since this is a contract position and fully remote, add a line in the summary emphasizing comfort with contract work and remote collaboration.

### 5. **Quantify Achievements**
The current CV could benefit from more specific metrics:
- "supported 40,000+ customers" (already good)
- Add similar metrics for other projects where possible
- Mention team sizes led or projects delivered on time/budget

### 6. **Reorder Skills for Relevance**
Move the most relevant skills to the front of the list:
- Python
- TypeScript
- AWS
- GCP
- MongoDB
- DynamoDB

### 7. **Consider Adding a "Recent Highlights" Section**
Create a brief section showcasing the most relevant recent work that aligns with the job requirements.

## Overall Assessment:

William's CV shows strong technical competency and relevant experience, but it needs strategic updates to highlight the specific technologies mentioned in the job description. The 13 years of experience and proven track record with complex systems make him a strong candidate, but the missing TypeScript and NoSQL database experience should be addressed either by:

1. Adding these skills if he has them but didn't mention them
2. Highlighting transferable experience (e.g., "extensive JavaScript experience, rapidly adaptable to TypeScript")
3. Demonstrating learning agility and ability to quickly adopt new technologies

The remote work capability and contract experience should also be more prominently featured given the nature of this role.
````

OK, that's pretty good. I don't really meet the requirements for this role, and it's
found why.

Let's go a step further:

```
Can you now write a paragraph or two that could be added to the summary that highlights the relevant experience and explains how the missing experience should not be a concern.
```

Claude's response:

```
My extensive Python expertise spans multiple frameworks including Django, FastAPI, and Flask, with proven ability to deliver high-performance systems such as RFGraph's sub-100ms latency RF simulator and PickTeamz's real-time notification system serving thousands of users. Having worked extensively with JavaScript across numerous projects, I can rapidly transition to TypeScript, leveraging my strong foundation in static typing principles from Python development. My cloud architecture experience with AWS translates seamlessly to GCP, as I've consistently demonstrated adaptability across different platforms and technologies throughout my 13-year career.

As a seasoned contractor running my own consultancy since graduation, I excel in remote collaboration and have successfully delivered complex projects for diverse clients including global brands like Asahi Super Dry and specialized platforms like AXS Passport. While my database experience has primarily focused on PostgreSQL and SQLite3, my proven track record of rapidly mastering new technologies—from building custom DSLs with pyparsing to implementing complex payment systems with Stripe—demonstrates my ability to quickly become proficient with NoSQL solutions like MongoDB and DynamoDB as project requirements demand.

These paragraphs:

1. **Highlight Python expertise** with specific, impressive examples (sub-100ms latency, real-time systems)
2. **Address TypeScript gap** by positioning JavaScript experience as a strong foundation and emphasizing adaptability
3. **Address cloud platform gap** by showing AWS experience transfers to GCP and emphasizing adaptability
4. **Emphasize contract/remote work** by mentioning his consultancy background and successful remote project delivery
5. **Address database gaps** by acknowledging the difference but demonstrating rapid learning ability with concrete examples
6. **Show problem-solving ability** through diverse project examples

The tone is confident without being arrogant, and it reframes potential weaknesses as opportunities to demonstrate adaptability—a crucial trait for contractors who often need to quickly get up to speed with new tech stacks.
```

That's pretty good. It's not perfect, but it's pretty good, and it took me no time at
all.

I'm going to add that to my CV and apply for this role. I'll update when I hear back.

Side note: I expect to be completely ghosted.

Side note 2: I had to edit the text a little bit to make it smaller, the paragraphs
wouldn't fit on a single page.
