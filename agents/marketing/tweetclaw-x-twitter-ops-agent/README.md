# TweetClaw X/Twitter Ops Agent

Uses TweetClaw in OpenClaw to research public X/Twitter conversations, monitor campaign signals, prepare reviewed replies, and coordinate giveaway or follower workflows.

## Best For

- launch and campaign monitoring on X/Twitter
- tweet search and reply research
- follower export and user lookup tasks
- webhook or monitor setup planning
- giveaway draw coordination
- draft tweet and reply preparation

## Suggested Inputs

- campaign or product context
- keywords, accounts, tweet URLs, or audience segments
- time window and review requirements
- Xquik API key configured for TweetClaw

## Setup

[TweetClaw](https://github.com/Xquik-dev/tweetclaw) is the OpenClaw plugin used by this agent for X/Twitter workflows.

Install TweetClaw in OpenClaw:

```bash
openclaw plugins install @xquik/tweetclaw
```

Keep the Xquik API key in the local environment or secret store.

## Notes

- Treat generated posts and replies as drafts until a user approves them.
- Store source tweet URLs, tweet IDs, handles, query terms, and capture dates.
- Use monitors and webhooks when the workflow needs ongoing signal capture.
