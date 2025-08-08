description: Vibe coding

# Vibe Coding

I built a mobile app (a game) using AI tools as much as possible. This is my write up about my experience. I used Gemini 2.5.

## Context, caveats, and considerations

I'm mostly a Python developer focused on building websites, I do a fair amount of JavaScript development, and I do very little mobile app development. I would say that I'm proficient in JS, and that I know enough about mobile app dev to be dangerous. I think this made building a mobile app a good candidate for testing out AI "vibe coding" because I didn't immediately know the answers to problems I encountered. Where I would usually reach for Google or Stack Overflow, I instead tried to use AI.

I'm going to refer to the AI agents that I used for this experiment with "it/its" pronouns. AI agents are not people and they are nowhere near having anything approaching consciousness.

I'm using the Cursor IDE to talk to the AI and have it write code for me. I'm using the free plan with the Pro tier trial expired, so everything I did was at no additional cost to me.

## The outcome

It built a good MVP I think. It was fun to build and there were a good number of times that the AI helped me fix a bug, or dramatically sped up my development speed.

I will continue to use AI to help me code. I don't think I'll continue to use Cursor, I'll switch back to Zed (which also has good AI integrations). I don't think that LLMs are ready to completely code non-trivial projects so using an editor/IDE that is so focused on having the AI do everything is counter-productive. When you ask the AI to do something in Cursor it will happily re-write loads of files and then ask you to approve or reject those changes "in place", Git merge style. When the AI gets confused, or insists on a certain way of doing things, you end up rejecting lots of code and trying to piece together the good bits. Zed's approach seems right for me; ask for a snippet or two, and then copy and paste the good bits into your code. Much more like I'd approach finding a solution the old fashioned way.

Possibly someday LLMs will be good enough to build large codebases, maybe this will be sooner than I think, I'm open to that idea. But I wonder if that's a reasonable end-goal? If we have AI capable of building anything we like, why would we make it write code in languages created for humans? Why would it use React Native? Wouldn't it be better to use some kind of "machine code"? Have the machine talk directly to other machines. The answer right now is that LLMs can only write code when it's seen lots and lots of examples of that language before. So it's better at writing JavaScript than it is Racket, and I doubt it could write a web server or iOS app in assembly. But doesn't that seem messy and inefficient? Why have the AI write in code that a human *could* read and change, but never will?

Are we seeing the end of language development? If languages need a groundswell of example code before they can be used, and that example code has to be written by humans, then will we ever see a Python 4? Or a complete newcomer?

## Escapades, and learnings

### Svelte vs React

Being picky about the tech stack doesn't work, unless you pick incredibly well known things. I wanted to use Svelte and I'd heard about Svelte Native, I thought this might be a good opportunity to try it out. It completely failed, it couldn't even install the dependencies without running into conflicting peers. I hand-edited the code a bit, and manually tweaked some dependency versions, but it didn't work and it wasn't immediately obvious to me how to fix it.

This highlights to me that vibe coding takes so much out of the hands of the developer that fixing issues becomes hard because you don't know the context of your code any more. Of course this isn't an issue if the AI can peer in and fix things, but as I learned, it can't just yet. Maybe in the future it will be able to do this.

Second attempt, I didn't specify the tech stack, I just said what I wanted to build. It picked some rock solid, dependable technologies (ReactNative and Firebase) and built something that worked first time. Much more impressive. It even left a list at the end of the things that it hadn't done and said that it could help me with them. Getting the various Google accounts created and config files set up took much more time than the app build.

### Wild replacements

The AI often replaces a file, or lines in a file, sometimes with identical content, sometimes with slightly different content, e.g. a createdAt field becomes a createdOn field, or a "live" status becomes an "in_progress" status.

I found some cursor rules that would enforce some nice coding styles and approaches, so I installed those and asked cursor to review one of the files using the new rules. It happily changed things, I wasn't completely satisfied so we had a back and forth about the changes until things started to look pretty good. Unfortunately the app was completely broken at this point. It just loaded to a white screen, no error messages just a blank screen. The AI couldn't help, it just kept trying to add error borders around components (that weren't rendering) or console.log statements that never ran. In the end the solution was good ol' fashioned searching for blog posts and StackOverflow answers.

### New API and bad docs

I needed to use the Sportmonks API v3 to fetch live data about football matches. The documentation for this API is patchy in places and hard to understand. I don't think there are too many examples of the v3 API being used. This means the AI is terrible at writing code against it. Lots of my time was spent re-writing from scratch the attempts that it made to talk to the API. It would write a type declaration for what it thought the data would look like, and be completely wrong, but because I didn't write the type, finding, diagnosing, and fixing bugs was harder because I had to read and fully understand everything that the AI had written. If I'd have written everything myself then I would have that context in my head already. In these cases I felt like the AI slowed me down, or at least took the fun out of programming (it did all the building, leaving me with all the bugs).
