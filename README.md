# Hyper-Personalized AI Outreach System

## Overview

This system is designed to automate the process of identifying top-fit candidates for highly technical roles and crafting hyper-personalized outreach emails using their LinkedIn profile data and recent activity.

We use large language models (LLMs) and semantic search to:

1. **Rank candidates** by semantic fit between job postings and profile descriptions.
2. **Draft personalized cold emails** based on a candidate’s recent public posts.
3. **Monitor and improve** the system with Weights & Biases (W\&B) Weave for observability and human-in-the-loop feedback.

---

## 🔍 Project Structure

```bash
.
├── profiles.json        # Sample LinkedIn profile data (scraped)
├── posting.json         # Job posting details
├── prompt.py            # Email generation prompt template
├── ranking.py           # Model 1: Profile ranking logic
├── draft.py             # Model 2: Email generation using Gemini
├── output.md            # Sample generated output emails
├── README.md            # This document
```

---

## ⚙️ Technical Details

### 1. Candidate Ranking (`ranking.py`)

**Objective:** Identify which profile best matches a job posting.

* Uses [`Qwen/Qwen3-Embedding-0.6B`](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B) via `sentence-transformers`.
* Computes cosine similarity between:

  * **Job description** (query with prompt)
  * **Profile descriptions** (document embeddings)
* Outputs a ranked list of candidates based on semantic fit.

**Snippet:**

```python
model = SentenceTransformer("Qwen/Qwen3-Embedding-0.6B")
query_embeddings = model.encode([job_description], prompt_name="query")
document_embeddings = model.encode(profile_descriptions)
similarity_scores = model.similarity(query_embeddings, document_embeddings)
```

---

### 2. Email Generation (`draft.py`)

**Objective:** Generate a hyper-personalized email for the top-ranked profile.

* Uses Gemini 2.5 Flash via the Google Generative AI SDK.
* Loads a structured prompt from `prompt.py` with placeholders filled dynamically.
* Leverages recent public posts to personalize messaging intelligently and naturally.

**LLM API:** Google Gemini 2.5 Flash
**Prompt Components:** Job, profile description, location, recent posts (x5)

---

### 3. Monitoring & Feedback Loop

**Tool:** [Weights & Biases Weave](https://wandb.ai/weave)

* All profile matches and generated emails are logged using W\&B for traceability.
* Human-in-the-loop feedback is supported for:

  * Profile match accept/reject
  * Email quality ratings (thumbs up/down, edit logs)

---

## 📊 Sample Data

### `posting.json`

```json
{
  "job_title": "Senior Machine Learning Scientist",
  "company": "TheoryFirst AI",
  "location": "Remote / San Francisco, CA",
  "description": "We're looking for a Senior ML Scientist with a strong foundation in classical ML, statistical modeling, and interpretability..."
}
```

---

### `profiles.json` (1 of 5)

```json
{
  "name": "Dr. Sarah Mitchell",
  "title": "ML Researcher | Statistical Learning | Causal Inference",
  "location": "Boston, MA",
  "profile_description": "ML scientist focused on interpretable systems, not generative fluff. Advocate for deep statistical grounding.",
  "recent_posts": [
    "LLMs can't even do bias-variance tradeoff right. Classical ML still rules.",
    "Just finished a paper on causal graphs for real-world experiments...",
    "Hype is not research. Repeat that.",
    "LLMs memorizing? Call it what it is: overfitting.",
    "New tutorial: convex optimization for model training stability."
  ]
}
```

---

### 📨 Sample Output (`output.md`)

```
Subject: Loved your post on bias-variance — we should talk

Hi Sarah,

I came across your post about how GPTs don’t get the bias-variance tradeoff — absolutely loved it. Honestly, it’s rare (and refreshing) to see someone calling for a return to core ML values in this current wave of GenAI hype.

At TheoryFirst AI, that’s kind of our whole philosophy — we’re building real ML systems, not just viral demos. We’re hiring a Senior ML Scientist and your focus on statistical learning theory and interpretability really resonated with us.

No pressure, but I’d love to chat and see if this might be up your alley. Either way, I’ll keep enjoying your posts :)

Warmly,  
Alex  
Founder, TheoryFirst AI
```

---

## ✅ Key Features

| Feature                         | Status |
| ------------------------------- | ------ |
| LLM-powered personalization     | ✅      |
| Job ↔ Profile semantic matching | ✅      |
| Real-time email drafting        | ✅      |
| Monitoring via W\&B Weave       | ✅      |
| Human-in-the-loop feedback      | ✅      |

---