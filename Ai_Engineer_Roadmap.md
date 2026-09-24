# The Complete AI Engineer Roadmap
### Build first. Deepen after. Ship things that work.

---

## What an AI Engineer Actually Is

An AI engineer builds **intelligent systems that work in production** — not just experiments in a notebook. The job sits at the intersection of software engineering and machine intelligence.

RAG is one pattern. Here is the full picture:

```
┌─────────────────────────────────────────────────────────────────┐
│                     AI ENGINEER SCOPE                           │
│                                                                 │
│  LLM APPLICATIONS    AGENTS          CLASSICAL ML              │
│  ─────────────────   ──────          ────────────              │
│  Chatbots            Autonomous      Recommendation            │
│  Copilots            task runners    Fraud detection           │
│  Doc processors      Multi-agent     Ranking systems           │
│  Content pipelines   systems         Tabular prediction        │
│  RAG systems                                                    │
│                                                                 │
│  ──────────────────────────────────────────────────────────    │
│  EVALUATION & SAFETY   FINE-TUNING   MLOps & DEPLOYMENT        │
│  ────────────────────  ───────────   ────────────────────      │
│  Benchmarking          LoRA/QLoRA    Model serving APIs        │
│  Red-teaming           RLHF/DPO      Monitoring & alerts       │
│  Guardrails            Embeddings    CI/CD pipelines           │
│  LLM-as-judge          Datasets      Cost management           │
└─────────────────────────────────────────────────────────────────┘
```

**Every AI engineer needs the foundation.** After that, you go deep in 1–2 areas based on the role you want.

---

## How This Roadmap Works

```
FOUNDATION  →  everyone does this first (4–6 weeks)
     │
     ▼
CORE TRACKS  →  do all of these, in order (build first, deepen after)
     │
     ├── Track 1: LLM Applications
     ├── Track 2: RAG as a Pattern
     ├── Track 3: AI Agents
     ├── Track 4: Evaluation & Safety  ← the glue that holds everything together
     ├── Track 5: Fine-tuning
     ├── Track 6: MLOps & Deployment
     └── Track 7: Classical ML Engineering
     │
     ▼
SPECIALISE  →  pick 1–2 tracks to go deep based on the job you want
```

Each track has:
- **UNLOCK** — minimum you must know before starting
- **BUILD** — the thing you ship
- **DEEPEN** — what to study after it works

---

# FOUNDATION — LLM Fluency
**Time: 4–6 weeks**
**Entry requirement: Python Phase 1 complete**

> Everyone starts here. These three skills underpin every track.

---

## F.1 — LLM APIs
**Time: 1 week**

**What to learn:**
- Chat completions: `system` / `user` / `assistant` message format
- Key parameters: `temperature`, `max_tokens`, `top_p`, `stop`
- Streaming responses — words appear as they generate
- Structured output — force the model to return JSON
- Token counting and cost calculation with `tiktoken`
- Error handling: rate limits, timeouts, retries with exponential backoff
- Multi-provider: OpenAI, Anthropic, Google Gemini, Mistral — same pattern, different SDKs
- API keys in `.env` with `python-dotenv` — never hardcoded

```python
from openai import OpenAI
from pydantic import BaseModel

client = OpenAI()

# Structured output — model returns validated JSON
class SentimentResult(BaseModel):
    sentiment: str        # "positive" | "negative" | "neutral"
    confidence: float
    reasoning: str

response = client.beta.chat.completions.parse(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": f"Analyse: '{text}'"}],
    response_format=SentimentResult,
)
result = response.choices[0].message.parsed
```

**Build:**
- [ ] Multi-turn CLI chatbot with conversation history
- [ ] Streaming response that prints token by token
- [ ] Structured JSON extractor: paste any text, get back entities (names, dates, amounts) as a Pydantic model
- [ ] Cost calculator: count tokens before sending, estimate price, log actual usage after

---

## F.2 — Prompt Engineering
**Time: 1 week**

Not magic words. It is understanding how models process text and structuring input to get reliable output.

**Techniques that matter (in order of importance):**

| Technique | When to use |
|---|---|
| **Clear system prompt with role + constraints** | Always |
| **Few-shot examples** | When output format is non-standard |
| **Chain-of-thought** | Reasoning, maths, multi-step logic |
| **Output format specification** | Structured data extraction |
| **XML/delimiter separation** | Separate instructions from user content |
| **Prompt decomposition** | Break one complex task into sequential prompts |
| **Self-consistency** | Sample multiple outputs, take majority for high-stakes tasks |

**The test for a good prompt:** run it 10 times. Does it produce consistent, correct output? If not, it is not good enough for production.

**Build:**
- [ ] Take one messy task (classify support tickets by urgency + category + suggested response). Write 5 progressively better prompts. Measure on 20 examples. Document what each change improved.
- [ ] Build a self-healing extractor: if JSON parsing fails, feed the error back to the model and ask it to fix the output. Track fix rate.
- [ ] Write a prompt that works across GPT-4o, Claude, and Gemini without modification.

**Resources:**
- [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
- [OpenAI Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering)

---

## F.3 — Embeddings & Semantic Search
**Time: 3–5 days**

An embedding maps text to a vector where similar meaning = similar direction. Cosine similarity measures that direction match.

```python
import numpy as np
from openai import OpenAI

client = OpenAI()

def embed(text: str) -> list[float]:
    return client.embeddings.create(
        model="text-embedding-3-small", input=text
    ).data[0].embedding

def cosine_similarity(a, b):
    a, b = np.array(a), np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
```

**Build:**
- [ ] Semantic search over 50 of your own notes or documents
- [ ] Duplicate detector: find near-duplicate entries in a dataset using cosine similarity threshold
- [ ] Cluster 100 customer reviews by topic using embeddings + k-means — no labels needed

---

## F.4 — The Math You Need Right Now
**Time: 3–5 days (just these concepts, not a full course)**

**Vectors and dot products** — what cosine similarity actually computes. Watch [3Blue1Brown Linear Algebra ep. 9](https://www.youtube.com/watch?v=LyGKycYT2v0) (12 min).

**Probability basics** — what a probability distribution is, expected value, the difference between P(A) and P(A|B). You need this to read any model evaluation result.

**That is all.** The rest of the math (gradients, matrix operations, full linear algebra) comes in Track 5 (fine-tuning) when you actually need it.

---

# TRACK 1 — LLM Application Development
**Time: 5–7 weeks**
**Entry requirement: Foundation complete**

> This is the core of most AI engineer job descriptions. You build products and pipelines on top of LLMs.

---

## T1.1 — The Patterns Every LLM App Uses

Before building, know the four fundamental patterns. Every LLM application is one or more of these:

```
PATTERN 1: Single-turn transformation
  Input text → LLM → Output text
  Examples: summariser, classifier, extractor, translator, formatter

PATTERN 2: Multi-turn conversation
  History + new input → LLM → Response + updated history
  Examples: chatbot, copilot, tutoring system, customer support bot

PATTERN 3: Chain
  Input → LLM₁ → intermediate → LLM₂ → Output
  Examples: draft → review → rewrite, extract → classify → respond

PATTERN 4: Router
  Input → LLM classifies intent → routes to specialised handler
  Examples: support ticket → billing/tech/general handler
```

**Build (one of each):**
- [ ] **Transformer pipeline:** paste any document (contract, email, report) → get summary + key entities + action items + sentiment. One input, four structured outputs.
- [ ] **Support bot:** multi-turn, maintains context, classifies intent, routes to appropriate response template, knows when to escalate to human.
- [ ] **Review chain:** write a draft → LLM critiques it against a rubric → rewrite incorporating feedback → LLM scores final version. Three chained calls.
- [ ] **Router:** given a user message, classify it into one of 5 categories and dispatch to a different prompt/handler for each.

---

## T1.2 — Document Intelligence Pipeline
**Time: 1.5–2 weeks**

One of the highest-demand AI engineering tasks: extract structured information from unstructured documents at scale.

**What companies actually need:**
- Process 1000s of PDFs/emails/contracts automatically
- Extract specific fields (dates, amounts, parties, clauses)
- Classify documents by type
- Flag anomalies or missing required fields
- Route documents to the right workflow

**Build a document processor:**

```python
from pydantic import BaseModel
from typing import Optional
import pdfplumber

class InvoiceData(BaseModel):
    vendor_name: str
    invoice_number: str
    invoice_date: str
    due_date: Optional[str]
    line_items: list[dict]
    subtotal: float
    tax: Optional[float]
    total: float
    currency: str
    payment_terms: Optional[str]
    confidence: float  # model's self-reported confidence

def extract_invoice(pdf_path: str) -> InvoiceData:
    with pdfplumber.open(pdf_path) as pdf:
        text = "\n".join(page.extract_text() for page in pdf.pages)

    # structured extraction
    result = client.beta.chat.completions.parse(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Extract invoice data. Be precise. Set confidence to 0.0-1.0."},
            {"role": "user", "content": text}
        ],
        response_format=InvoiceData,
    )
    return result.choices[0].message.parsed
```

**Requirements:**
- [ ] Process any PDF: invoice, contract, résumé, or research paper — extract structured data
- [ ] Batch processing: handle a folder of 50 documents, save results to JSON
- [ ] Confidence scoring: flag extractions below 0.8 for human review
- [ ] Validation: cross-check extracted numbers (do line items add up to total?)
- [ ] Error handling: corrupted PDF, scanned image (no extractable text), missing fields

---

## T1.3 — Copilot / AI Assistant
**Time: 1–1.5 weeks**

A copilot is an LLM embedded inside a user's workflow — it has context about what the user is doing, not just a generic conversation.

**What makes a copilot different from a chatbot:**
- It has **workspace context** (the document they're editing, the code they're writing, the data they're viewing)
- It takes **actions** on behalf of the user (insert text, apply format, run a query)
- It has **persistent memory** of previous interactions in that workspace

**Build a writing copilot:**
```python
class CopilotSession:
    def __init__(self, document_text: str):
        self.document = document_text
        self.history = []
        self.system_prompt = f"""You are a writing assistant with access to the user's document.
You can: improve selected text, answer questions about the document,
suggest additions, check consistency, and rewrite sections.

Current document:
---
{document_text}
---"""

    def ask(self, user_request: str, selected_text: str = None) -> str:
        context = f"Selected: '{selected_text}'\n\nRequest: {user_request}" if selected_text else user_request
        self.history.append({"role": "user", "content": context})
        response = call_llm(self.system_prompt, self.history)
        self.history.append({"role": "assistant", "content": response})
        return response
```

**Requirements:**
- [ ] Build a coding copilot: explain selected code, suggest improvements, detect bugs, generate tests for a function
- [ ] OR build a writing copilot: improve tone, check consistency, suggest titles, summarise sections
- [ ] Context window management: when document is long, summarise older sections to stay within limits
- [ ] Streaming output so responses feel instant

---

## T1.4 — Content Generation Pipeline
**Time: 1 week**

AI-powered content pipelines generate, transform, or enrich content at scale. Common in marketing, media, e-commerce, and internal knowledge management.

**Build a content pipeline:**

```
Source data (product catalogue, research notes, raw data)
    ↓
Enrichment stage (fill missing fields, normalise format)
    ↓
Generation stage (write descriptions, summaries, translations)
    ↓
Quality gate (LLM reviews output against criteria)
    ↓
Output (structured, validated, ready for use)
```

**Requirements:**
- [ ] Input: a CSV of 100 products with name + category + specs only
- [ ] Output: marketing description, SEO title, bullet points, FAQ answers — for each product
- [ ] Quality gate: score each output against a rubric (accuracy, tone, length). Regenerate if score < threshold.
- [ ] Cost tracking: log token usage per item; calculate cost per 1000 items
- [ ] Batch with rate limiting: don't hit API rate limits; process in controlled batches with delays

---

## T1.5 — DEEPEN: After Track 1

- [ ] **LangChain LCEL** — chain components with `|` operator; useful once pipelines get complex
- [ ] **Context window management** — token counting, compression, sliding window strategies
- [ ] **Multimodal inputs** — GPT-4V / Claude vision: send images alongside text; extract data from screenshots, charts, forms
- [ ] **Function calling deeply** — parallel tool calls, tool choice strategies, handling tool errors
- [ ] **Prompt versioning** — treat prompts like code: version control, A/B test, track performance over time

---

# TRACK 2 — RAG Systems
**Time: 4–5 weeks**
**Entry requirement: Track 1 complete + embeddings**

> RAG is the pattern for grounding LLMs in private or up-to-date knowledge. It is one tool in the LLM app toolkit, not the whole job.

---

## T2.1 — Build Naive RAG
**Time: 1.5 weeks**

```
User question → embed → vector search → retrieve top-k chunks
→ inject chunks into prompt → LLM generates answer with citations
```

**Stack:**
- Chunking: `RecursiveCharacterTextSplitter` (LangChain)
- Embeddings: `text-embedding-3-small` (OpenAI) or `all-MiniLM-L6-v2` (free, local)
- Vector store: ChromaDB (local, easy start)
- LLM: `gpt-4o-mini` for cost efficiency

**Requirements:**
- [ ] Ingest 20+ pages of real documents you care about
- [ ] Return source citations with every answer
- [ ] Handle "I don't know" — when no relevant chunk exists, say so
- [ ] Simple Streamlit UI: document upload + chat interface

---

## T2.2 — Improve Retrieval
**Time: 1–1.5 weeks**

**In order of ROI:**

**Hybrid search** — BM25 (keyword) + semantic. Semantic misses exact terms; BM25 misses meaning. Together they beat either alone.

**Re-ranking** — retrieve 20 chunks cheaply, re-score the top 3–5 carefully with a cross-encoder.
```python
from sentence_transformers import CrossEncoder
reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")
scores = reranker.predict([[query, chunk] for chunk in candidates])
```

**Query rewriting** — clean and expand the user's messy question before embedding it.

**Requirements:**
- [ ] Add hybrid search; measure retrieval precision before and after
- [ ] Add re-ranking; measure again
- [ ] Move from ChromaDB to Qdrant for scalability

---

## T2.3 — Advanced RAG Patterns
**Time: 1 week**

| Pattern | Problem it solves |
|---|---|
| **Parent document retrieval** | Embed small chunks for precision, return the larger parent for context |
| **HyDE** | Generate a hypothetical answer, embed that instead of the question |
| **Multi-hop retrieval** | Questions that need two retrieval steps to answer |
| **Contextual compression** | Summarise retrieved chunks to only the relevant part |
| **Self-RAG** | Model decides when to retrieve and critiques its own answer |

**Requirements:**
- [ ] Implement one advanced pattern; measure its effect on your eval set

---

## T2.4 — RAG Evaluation
**Time: 3–5 days**

Build a test set of 25+ questions with reference answers. Score every RAG change against it.

**Metrics to track:**
- **Faithfulness** — does the answer contain only info from retrieved context?
- **Answer relevance** — does it address the question?
- **Context recall** — did retrieval find the chunks that actually contain the answer?

Use RAGAS library or build your own LLM-as-judge scorer.

**Rule:** never change chunking, embedding model, retrieval strategy, or prompt without running the eval set first and after.

---

# TRACK 3 — AI Agents
**Time: 5–7 weeks**
**Entry requirement: Tracks 1 + 2 complete**

> Agents are LLMs that take actions. This is where AI engineering gets genuinely hard — and where the most interesting problems live in 2026.

---

## T3.1 — What an Agent Is
**Time: 2–3 days**

```
AGENT LOOP:
    LLM receives: system prompt + conversation + available tools
         ↓
    LLM decides: call a tool OR produce final answer
         ↓
    If tool call: execute it, feed result back
         ↓
    Repeat until final answer
```

**What makes agents hard:**
- They can take wrong actions and cause real consequences
- They can get stuck in loops
- They run out of context window on long tasks
- Errors compound across steps — one bad decision cascades

**The reliability rule:** the more autonomous the agent, the more important evaluation and guardrails become. Never deploy an agent that can take irreversible actions without checkpoints.

---

## T3.2 — Tool Use / Function Calling
**Time: 1 week**

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "search_web",
            "description": "Search the internet for current information",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query"},
                    "num_results": {"type": "integer", "default": 5}
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read contents of a file by path",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"}
                },
                "required": ["path"]
            }
        }
    }
]

# The agent loop
def run_agent(user_message: str) -> str:
    messages = [{"role": "user", "content": user_message}]

    while True:
        response = client.chat.completions.create(
            model="gpt-4o", messages=messages, tools=tools
        )
        msg = response.choices[0].message

        if msg.tool_calls:
            messages.append(msg)
            for call in msg.tool_calls:
                result = execute_tool(call.function.name, call.function.arguments)
                messages.append({
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": str(result)
                })
        else:
            return msg.content  # final answer
```

**Build:**
- [ ] Agent with 4 tools: web search, calculator, file reader, Python code executor
- [ ] Parallel tool calls: make the agent call two tools simultaneously when both are needed
- [ ] Tool error handling: what happens when a tool fails? The agent should recover, not crash.

---

## T3.3 — ReAct Pattern
**Time: 3–5 days**

ReAct (Reason + Act) makes the agent's thinking explicit before each action. More reliable than letting it act silently.

```
Thought: I need to find the current price of gold.
Action: search_web("gold price today USD")
Observation: Gold is $2,345 per troy ounce as of today.
Thought: Now I can answer the question.
Final Answer: Gold is currently $2,345 per troy ounce.
```

**Why it works:** forcing the model to articulate reasoning before acting catches a large class of wrong actions before they happen.

**Build:**
- [ ] Research assistant using ReAct: given a question, plans a research strategy, executes it across multiple sources, synthesises a cited answer

---

## T3.4 — Memory Systems
**Time: 1 week**

Agents need memory to work across long tasks and multiple sessions.

| Memory type | What it stores | Implementation |
|---|---|---|
| **In-context (short-term)** | Recent conversation | Message list — limited by context window |
| **Summary memory** | Compressed older history | Periodically summarise and replace old messages |
| **Entity memory** | Facts about specific people/things | Dict or structured store; update as new facts appear |
| **Long-term (episodic)** | Past sessions and outcomes | Vector DB; retrieve relevant past episodes |

```python
class AgentMemory:
    def __init__(self):
        self.short_term = []        # recent messages
        self.entities = {}          # {entity_name: facts_dict}
        self.episodes = VectorStore()  # past sessions

    def add_message(self, role, content):
        self.short_term.append({"role": role, "content": content})
        if len(self.short_term) > 20:
            self._compress_old_messages()

    def update_entity(self, name, new_facts):
        if name not in self.entities:
            self.entities[name] = {}
        self.entities[name].update(new_facts)
```

**Build:**
- [ ] Customer support agent that remembers user's name, past issues, and preferences across sessions
- [ ] Entity extraction: after each conversation turn, extract and store any new facts mentioned

---

## T3.5 — Multi-Agent Systems
**Time: 1.5–2 weeks**

One agent with all tools becomes slow, confused, and unreliable on complex tasks. Multi-agent systems divide work across specialists.

**Common patterns:**

```
ORCHESTRATOR-WORKER
  Orchestrator: plans the task, delegates subtasks
  Workers: specialist agents (researcher, writer, coder, reviewer)

PIPELINE
  Agent A output → Agent B input → Agent C input
  Each agent transforms the work and passes it forward

DEBATE / CRITIQUE
  Agent A produces output
  Agent B critiques it
  Agent A revises
  Judge agent decides if it is good enough
```

**Build:**
- [ ] **Research-to-report pipeline:** Researcher agent gathers information → Analyst agent identifies key findings → Writer agent produces the report → Editor agent reviews and revises
- [ ] **Code review system:** Coder agent writes a function → Reviewer agent finds bugs → Tester agent writes tests → Orchestrator decides if it is shippable
- [ ] Add inter-agent critique: agents challenge each other's outputs before passing forward

**Resources:**
- [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
- [LangGraph](https://langchain-ai.github.io/langgraph/) — stateful multi-actor graph framework

---

## T3.6 — DEEPEN: After Track 3

- [ ] **Planning algorithms** — tree of thought, MCTS for agent planning; when simple ReAct isn't enough
- [ ] **Agent evaluation** — how to measure agent performance on open-ended tasks (not just accuracy)
- [ ] **Safety and containment** — agents that can take real actions need real guardrails; sandboxing, human-in-the-loop checkpoints, reversibility checks
- [ ] **Long-context models** — 1M token context windows change what memory is needed
- [ ] **Computer use agents** — models that can control a browser or desktop (Anthropic computer use, OpenAI Operator)

---

# TRACK 4 — Evaluation & Safety
**Time: 3–4 weeks**
**Entry requirement: At least one Track (1, 2, or 3) complete**

> This is the most underrated track and the one that most clearly signals a senior engineer. Anyone can build an LLM app. Few can systematically measure whether it works.

---

## T4.1 — Why Evaluation is Hard
**Time: 2–3 days**

With traditional software: input → function → deterministic output. Testing is straightforward.

With LLMs: input → probabilistic output. The same input produces different outputs. "Correctness" is often subjective. You can't write a simple `assert`.

**The three evaluation approaches:**

| Approach | What it is | When to use |
|---|---|---|
| **Human evaluation** | People score outputs | Gold standard; expensive and slow |
| **Reference-based** | Compare to a correct answer | When you have ground truth labels |
| **LLM-as-judge** | A model scores another model's output | Scalable; biased toward models similar to the judge |

**The trap:** optimising for your eval set instead of real-world quality. Your eval is a proxy — if you overfit to it, you will have high eval scores and bad production performance.

---

## T4.2 — Build an Evaluation Framework
**Time: 1–1.5 weeks**

```python
class EvalHarness:
    def __init__(self, test_cases: list[dict], system_fn):
        self.test_cases = test_cases   # [{input, expected, metadata}]
        self.system_fn = system_fn     # the function you're evaluating

    def run(self) -> dict:
        results = []
        for case in self.test_cases:
            output = self.system_fn(case["input"])
            scores = self.score(case, output)
            results.append({**case, "output": output, "scores": scores})
        return self.aggregate(results)

    def score(self, case, output) -> dict:
        return {
            "llm_judge": self.llm_judge_score(case["input"], case["expected"], output),
            "exact_match": output.strip() == case["expected"].strip(),
            "contains_key_terms": all(t in output for t in case.get("required_terms", [])),
        }

    def llm_judge_score(self, question, reference, answer) -> dict:
        prompt = f"""Score this answer (0-3 each):
- Faithfulness: only claims supported by context
- Relevance: addresses the question
- Completeness: covers the key points

Question: {question}
Reference: {reference}
Answer: {answer}

Return JSON: {{"faithfulness": X, "relevance": X, "completeness": X, "reasoning": "..."}}"""
        return json.loads(llm_call(prompt))
```

**Requirements:**
- [ ] Build a test set for every application you built in Tracks 1–3 (minimum 25 cases each)
- [ ] Score every change to prompt, model, or retrieval against the test set before and after
- [ ] Store results in JSON with timestamps so you can track improvement over time
- [ ] Dashboard: visualise score history across changes

---

## T4.3 — Safety & Guardrails
**Time: 1 week**

Production LLM applications face adversarial users, edge cases, and unexpected inputs. Guardrails are the defence.

**Types of failures to guard against:**

| Failure | What it is | Guard |
|---|---|---|
| **Prompt injection** | User embeds instructions in their input to override your system prompt | Input sanitisation, instruction hierarchy |
| **Jailbreaking** | User tricks model into ignoring safety rules | Input classifier, output classifier |
| **Hallucination** | Model states false information confidently | Grounding constraints, citation requirements |
| **Data leakage** | Model reveals contents of other users' conversations | Session isolation, PII detection |
| **Off-topic use** | User uses the system for unintended purposes | Intent classifier, usage policies |

**Build an input/output guard layer:**
```python
class GuardLayer:
    def check_input(self, user_input: str) -> GuardResult:
        checks = [
            self.detect_prompt_injection(user_input),
            self.detect_pii(user_input),
            self.check_topic_relevance(user_input),
            self.check_rate_limit(user_id),
        ]
        return GuardResult(passed=all(c.passed for c in checks), checks=checks)

    def check_output(self, output: str) -> GuardResult:
        checks = [
            self.detect_pii_in_output(output),
            self.check_factual_grounding(output),
            self.check_harmful_content(output),
        ]
        return GuardResult(passed=all(c.passed for c in checks), checks=checks)
```

**Build:**
- [ ] Wrap one of your Track 1–3 projects with a guard layer: input classifier + output validator
- [ ] Red-team your own application: spend 30 minutes trying to break it. Document every success.
- [ ] PII detector: scan inputs and outputs; redact or refuse when detected

**Resources:**
- [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [Llama Guard](https://huggingface.co/meta-llama/Llama-Guard-3-8B) — open-source safety classifier

---

## T4.4 — Benchmarking & Model Selection
**Time: 3–5 days**

Choosing the right model for a task requires systematic comparison, not vibes.

**Build a model comparison framework:**
```python
MODELS = ["gpt-4o", "gpt-4o-mini", "claude-3-5-sonnet", "claude-3-haiku"]

def benchmark_task(task_fn, eval_set, models) -> dict:
    results = {}
    for model in models:
        outputs = [task_fn(case["input"], model=model) for case in eval_set]
        results[model] = {
            "quality_score": score_outputs(eval_set, outputs),
            "avg_latency_ms": measure_latency(task_fn, eval_set, model),
            "avg_cost_per_call": calculate_cost(outputs, model),
            "cost_per_quality_point": ...  # the real comparison metric
        }
    return results
```

**For every new LLM task you build:**
- [ ] Define the task clearly with 20 test cases
- [ ] Benchmark at least 3 models on quality, latency, and cost
- [ ] Pick the cheapest model that meets your quality threshold — not the best model
- [ ] Document the decision with numbers

---

# TRACK 5 — Fine-tuning & Model Customisation
**Time: 7–9 weeks**
**Entry requirement: Tracks 1–4 + PyTorch basics**

> Fine-tune only what you've measured is broken. If eval shows the problem is retrieval, fix retrieval. Fine-tuning is expensive and slow — use it for what prompt engineering and RAG genuinely cannot solve.

---

## T5.1 — UNLOCK: Neural Networks & PyTorch
**Time: 3–4 weeks**

You cannot debug a broken training run without understanding how training works. No shortcuts.

**Step 1 — Neural net fundamentals (1 week):**
- [ ] [Karpathy — micrograd](https://www.youtube.com/watch?v=VMj-3S1tku0): build backpropagation from scratch (2.5 hrs). This is non-negotiable.
- Understand: forward pass → loss → backward pass → weight update → repeat

**Step 2 — PyTorch basics (2 weeks):**
- Tensors, shapes, device management
- `nn.Module`, `forward()`, layer types
- Training loop: forward → loss → `backward()` → `optimizer.step()` → `zero_grad()`
- `DataLoader` + `Dataset` for batching

**Step 3 — Hugging Face ecosystem (1 week):**
- `AutoTokenizer`, `AutoModelForCausalLM` — load any model the same way
- `datasets` library — loading and formatting training data
- `Trainer` — the standard training loop
- Hugging Face Hub — finding and publishing models

---

## T5.2 — When to Fine-tune vs. Other Approaches

```
Problem with LLM output
         │
         ▼
Is the output format inconsistent? ──YES──► Prompt engineering first
         │NO
         ▼
Is it missing domain knowledge? ──YES──► RAG first (cheaper, faster)
         │NO
         ▼
Is retrieval working but generation poor? ──YES──► Fine-tune the LLM
         │NO
         ▼
Is retrieval itself poor? ──YES──► Fine-tune the embedding model
         │NO
         ▼
Do you have <50 examples? ──YES──► Few-shot prompting
         │NO
         ▼
Fine-tuning is appropriate ✓
```

---

## T5.3 — Fine-tune Embedding Models
**Time: 1–1.5 weeks**

**Higher ROI than fine-tuning the LLM.** Better retrieval means better answers downstream.

**Data format — triplets:**
```python
# (query, positive_match, negative_non_match)
training_triplets = [
    {
        "query": "What is the cancellation policy?",
        "positive": "Subscriptions can be cancelled within 14 days for a full refund.",
        "negative": "We offer free shipping on all orders above $50."
    },
    # 300-500 minimum
]
```

```python
from sentence_transformers import SentenceTransformer, SentenceTransformerTrainer, losses

model = SentenceTransformer("all-MiniLM-L6-v2")
loss = losses.TripletLoss(model)

trainer = SentenceTransformerTrainer(model=model, train_dataset=dataset, loss=loss)
trainer.train()
model.save_pretrained("my-domain-embeddings")
```

**Build:**
- [ ] Create 300 triplets from your domain (use an LLM to generate negatives)
- [ ] Fine-tune `all-MiniLM-L6-v2`
- [ ] Swap it into your RAG system and run your Track 4 eval harness
- [ ] Document: retrieval precision before vs. after

---

## T5.4 — Fine-tune LLMs with LoRA/QLoRA
**Time: 2–3 weeks**

**LoRA** adds small trainable adapter matrices to a frozen base model. Instead of updating 7 billion parameters, you update ~65 thousand. Same results, 250× fewer parameters.

```python
from peft import LoraConfig, get_peft_model
from trl import SFTTrainer

lora_config = LoraConfig(
    r=8,                              # rank — higher = more capacity
    lora_alpha=16,
    target_modules=["q_proj", "v_proj"],
    task_type="CAUSAL_LM"
)

model = get_peft_model(base_model, lora_config)
model.print_trainable_parameters()
# trainable params: 0.06% — that's the point

trainer = SFTTrainer(
    model=model,
    args=TrainingArguments(output_dir="output", num_train_epochs=3, ...),
    train_dataset=dataset,
    dataset_text_field="text",
    peft_config=lora_config,
)
trainer.train()
```

**Data format for fine-tuning (critical — wrong format = silent failure):**
```python
def format_example(instruction, input_text, output):
    return f"""<|system|>{instruction}</s>
<|user|>{input_text}</s>
<|assistant|>{output}</s>"""
```

**Build:**
- [ ] Fine-tune `Llama-3.2-1B` on 500+ domain examples
- [ ] Run your eval harness: base model vs. fine-tuned
- [ ] Publish the adapter to Hugging Face Hub with a model card showing the eval results

---

## T5.5 — RLHF / DPO (Conceptual + Hands-on)
**Time: 1 week**

**RLHF** (Reinforcement Learning from Human Feedback) is how GPT-4 and Claude were made helpful. A reward model trained on human preferences guides the LLM to produce preferred outputs.

**DPO** (Direct Preference Optimisation) achieves the same result more simply — no separate reward model needed. It is the current standard.

```python
# DPO data format: chosen vs rejected pairs
dpo_data = [
    {
        "prompt": "Explain quantum entanglement simply.",
        "chosen": "Quantum entanglement means two particles...[clear explanation]",
        "rejected": "Quantum entanglement is when particles exhibit...[jargon-heavy]"
    }
]

from trl import DPOTrainer
trainer = DPOTrainer(model=model, ref_model=ref_model, args=args, train_dataset=dataset)
trainer.train()
```

**Build:**
- [ ] Create 200 (prompt, chosen, rejected) pairs for a task you care about
- [ ] Run DPO on a small model; evaluate preference alignment before and after

---

# TRACK 6 — MLOps & Deployment
**Time: 4–5 weeks**
**Entry requirement: Tracks 1–4 complete**

> Building a great model means nothing if it's a Jupyter notebook on your laptop. This track makes your AI work production-grade.

---

## T6.1 — Serving Models as APIs
**Time: 1 week**

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio

app = FastAPI()

class QueryRequest(BaseModel):
    input: str
    max_tokens: int = 500

@app.post("/predict")
async def predict(req: QueryRequest):
    try:
        result = await run_pipeline_async(req.input, req.max_tokens)
        return {"output": result.text, "usage": result.usage}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "ok", "model": MODEL_NAME}
```

**Requirements:**
- [ ] Wrap every AI system you built (chatbot, RAG, agent) in a FastAPI endpoint
- [ ] Async endpoints for all LLM calls — never block the server
- [ ] Streaming responses via `StreamingResponse`
- [ ] Input validation with Pydantic — reject bad inputs before they hit the model
- [ ] Request ID + structured logging on every call

---

## T6.2 — Observability Stack
**Time: 1 week**

You cannot improve what you cannot see. Log everything from day one.

**What to log per request:**
```python
log.info("ai_request", extra={
    "request_id": req_id,
    "endpoint": "/predict",
    "model": model_name,
    "input_tokens": prompt_tokens,
    "output_tokens": completion_tokens,
    "cost_usd": calculate_cost(prompt_tokens, completion_tokens, model_name),
    "latency_ms": round((time.time() - start) * 1000),
    "status": "success" | "error",
    "error_type": error.__class__.__name__ if error else None,
})
```

**Metrics to track (and alert on):**

| Metric | Alert threshold |
|---|---|
| p95 latency | > 5 seconds |
| Error rate | > 2% |
| Daily cost | > your budget |
| Tokens per request | 3× baseline (runaway inputs) |
| Eval score (scheduled) | Drop > 5% from baseline |

**Build:**
- [ ] Structured JSON logging with `structlog`
- [ ] SQLite metrics store: query average latency, cost, error rate for any time window
- [ ] Slack alert when cost threshold exceeded or error rate spikes
- [ ] Weekly eval report: automatically run your eval harness every Monday, log results

---

## T6.3 — Caching & Cost Control
**Time: 3–5 days**

LLM API calls cost money. Cache aggressively.

```python
import redis
import hashlib

r = redis.Redis()

def cached_llm_call(prompt: str, ttl: int = 3600) -> str:
    cache_key = f"llm:{hashlib.md5(prompt.encode()).hexdigest()}"
    cached = r.get(cache_key)
    if cached:
        return cached.decode()
    result = llm_call(prompt)
    r.setex(cache_key, ttl, result)
    return result

def cached_embed(text: str) -> list[float]:
    # embeddings are deterministic — cache forever
    cache_key = f"emb:{hashlib.md5(text.encode()).hexdigest()}"
    ...
```

**Build:**
- [ ] Embedding cache (embeddings are deterministic — never recompute the same text)
- [ ] Query cache with TTL (same question within 1 hour → return cached answer)
- [ ] Cost dashboard: daily spend by endpoint, by user, by model

---

## T6.4 — Docker + CI/CD
**Time: 1 week**

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```yaml
# .github/workflows/ci-cd.yml
name: Test → Eval → Deploy
on:
  push:
    branches: [main]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install -r requirements.txt
      - run: pytest tests/ -v

  eval:
    needs: test
    steps:
      - run: python run_eval.py --save-results
      - run: python check_eval_regression.py  # fail if scores dropped >5%

  deploy:
    needs: eval
    steps:
      - name: Deploy to Render
        run: curl -X POST ${{ secrets.RENDER_DEPLOY_HOOK }}

      - name: Smoke test
        run: |
          curl -f https://your-app.onrender.com/health
          python smoke_test.py
```

**Requirements:**
- [ ] Every project containerised with Docker
- [ ] GitHub Actions: test → eval → deploy pipeline. Eval regression blocks deployment.
- [ ] Zero secrets in the repo — all in environment variables

---

## T6.5 — Serving Open-Source Models
**Time: 3–5 days**

Not every deployment uses the OpenAI API. Sometimes you serve your own model for cost, privacy, or latency.

```bash
# Run any model locally with Ollama
ollama pull llama3.2
ollama serve  # starts on localhost:11434

# Same OpenAI-compatible API
from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
```

**For production serving of larger models:**
- **vLLM** — the standard for high-throughput GPU serving; PagedAttention gives 2–24× higher throughput
- **Ollama** — local development and small-scale deployment
- **Hugging Face Inference Endpoints** — managed hosting for any HF model

**Build:**
- [ ] Run your fine-tuned model locally with Ollama; test the same API calls
- [ ] Compare: OpenAI API vs local model for your use case (quality, latency, cost per 1000 calls)

---

# TRACK 7 — Classical ML Engineering
**Time: 5–7 weeks**
**Entry requirement: Foundation complete (can do in parallel with other tracks)**

> LLMs get the headlines but classical ML runs more production systems than anything else. Recommendation engines, fraud detection, search ranking, anomaly detection — these are all classical ML. An AI engineer who only knows LLMs is a narrow specialist.

---

## T7.1 — The ML Workflow
**Time: 1 week**

```
Business question → data → features → model → evaluate → deploy → monitor → iterate
```

**Every ML project follows this. Learn it once:**

- **Train / validation / test split** — three sets, not two. Leakage kills production models.
- **Baseline first** — build the dumbest model before the smart one. If smart doesn't beat dumb, something is wrong.
- **Overfitting vs underfitting** — the bias-variance trade-off; what each looks like in a learning curve
- **Cross-validation** — more reliable estimates when data is limited
- **Feature engineering** — the craft that separates strong practitioners from weak ones

---

## T7.2 — Core Algorithms
**Time: 2–3 weeks**

| Algorithm | Best for |
|---|---|
| **Logistic Regression** | Baseline classification, interpretability required |
| **Random Forest** | Tabular data, feature importance, robust default |
| **XGBoost / LightGBM** | Tabular data at scale, competition winner, production standard |
| **k-Means** | Customer segmentation, data exploration |
| **k-NN** | Similarity search, recommendation (for small scale) |
| **Isolation Forest** | Anomaly detection |
| **Linear Regression** | Baseline regression, trend analysis |

**80/20 call:** master Random Forests and XGBoost. They handle real tabular data better than almost anything else and appear in the majority of production ML systems.

**Build:**
- [ ] **Fraud detection:** train XGBoost on a transaction dataset; optimise for precision-recall trade-off (not accuracy — class imbalance)
- [ ] **Recommender:** given user-item interactions, build a simple collaborative filtering system
- [ ] **Anomaly detector:** isolation forest on server metrics; flag unusual patterns

---

## T7.3 — Evaluation for Classical ML
**Time: 3–5 days**

**Why accuracy is a lie:** a fraud model that predicts "not fraud" for every transaction achieves 99.9% accuracy. It is completely useless.

**Metrics you must know:**

| Metric | When to use |
|---|---|
| **Precision** | Cost of false positives is high (fraud flagging, spam) |
| **Recall** | Cost of false negatives is high (cancer detection, safety) |
| **F1** | Balance of both |
| **AUC-ROC** | Ranking quality across thresholds |
| **PR curve** | Imbalanced classes — more informative than ROC |
| **MAE / RMSE** | Regression problems |
| **NDCG** | Ranking systems (search, recommendation) |

**Build:**
- [ ] Given a dataset: compute every metric above, plot the ROC curve and PR curve, and explain in plain English what each one tells you

---

## T7.4 — Feature Engineering & Data Pipelines
**Time: 1 week**

The model is 20% of the work. The data pipeline is 80%.

**Feature engineering techniques:**
- Normalisation / standardisation (and when each matters)
- Encoding categoricals: one-hot, ordinal, target encoding — and when each is appropriate
- Handling missing values: imputation strategies and their hidden biases
- Date/time features: extract day of week, hour, month, days since an event
- Interaction features: multiply two features that you believe interact
- Log transforms: for skewed distributions

**Build:**
- [ ] Data pipeline that reads raw CSV, applies 10+ feature engineering steps, and produces a clean feature matrix ready for modelling
- [ ] Use `sklearn.pipeline.Pipeline` so the same transformations apply to train and test consistently

---

## T7.5 — Deploy a Classical ML Model
**Time: 3–5 days**

```python
import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

model = joblib.load("fraud_model.pkl")
preprocessor = joblib.load("preprocessor.pkl")

app = FastAPI()

class Transaction(BaseModel):
    amount: float
    merchant_category: str
    hour_of_day: int
    days_since_last_transaction: float

@app.post("/predict")
def predict(transaction: Transaction):
    df = pd.DataFrame([transaction.dict()])
    features = preprocessor.transform(df)
    probability = model.predict_proba(features)[0, 1]
    return {
        "fraud_probability": round(float(probability), 4),
        "is_flagged": probability > 0.85,
        "model_version": "v2.1"
    }
```

**Requirements:**
- [ ] Save model + preprocessor together so they can't get out of sync
- [ ] Version your models: `fraud_model_v1.pkl`, `v2.pkl` — never overwrite
- [ ] A/B test infrastructure: serve two model versions to different traffic splits and compare metrics

---

# PUTTING IT ALL TOGETHER

## The AI Engineer Competency Map

```
FOUNDATION
  LLM APIs ────────────────────────────────── everyone needs this
  Prompt Engineering ──────────────────────── everyone needs this
  Embeddings ──────────────────────────────── everyone needs this

CORE TRACKS (do all of these)
  Track 1: LLM Apps ───────────────────────── the bread and butter
  Track 2: RAG ────────────────────────────── one essential pattern
  Track 3: Agents ─────────────────────────── the frontier
  Track 4: Evaluation ─────────────────────── the glue
  Track 5: Fine-tuning ────────────────────── go deep when needed
  Track 6: MLOps ──────────────────────────── how you ship
  Track 7: Classical ML ───────────────────── the evergreen layer

SPECIALISE (go deep in 1–2 based on target role)
  LLM App Engineer ────► Tracks 1, 4, 6 deepest
  RAG Engineer ────────► Tracks 2, 4 deepest
  Agent Engineer ──────► Track 3 deepest
  ML Engineer ─────────► Tracks 7, 5, 6 deepest
  MLOps Engineer ──────► Track 6 deepest + infrastructure
```

---

## Recommended Order

```
Month 1–4 ──► Your Python syllabus (Phases 1–3)

Month 5 ────► Foundation (F.1 LLM APIs, F.2 Prompting, F.3 Embeddings)
              Track 1 begins (LLM Applications)

Month 6 ────► Track 1 complete
              Track 2 (RAG) begins
              Track 7 (Classical ML) in parallel — 4 hrs/week alongside

Month 7 ────► Track 2 complete
              Track 3 (Agents) begins

Month 8 ────► Track 3 complete
              Track 4 (Evaluation) — runs across everything from now on
              Track 5 begins (unlock: PyTorch)

Month 9 ────► Track 5 complete
              Track 6 (MLOps) begins — deploy everything you built

Month 10 ───► Track 6 complete
              Track 7 complete
              Build capstone project

Month 11–12 ► Job search + portfolio polish
```

---

## Timeline

| Phase | Hours | At 12 hrs/week |
|---|---|---|
| Python syllabus | 315–415 hrs | 4 months |
| Foundation | 25–35 hrs | 2–3 weeks |
| Track 1: LLM Apps | 55–70 hrs | 5–6 weeks |
| Track 2: RAG | 40–55 hrs | 4–5 weeks |
| Track 3: Agents | 55–75 hrs | 5–6 weeks |
| Track 4: Evaluation | 35–50 hrs | 3–4 weeks |
| Track 5: Fine-tuning | 70–90 hrs | 6–7 weeks |
| Track 6: MLOps | 50–65 hrs | 4–5 weeks |
| Track 7: Classical ML | 55–70 hrs | 5–6 weeks |
| **Total AI supplement** | **~385–510 hrs** | **~35–45 weeks** |
| **Grand total** | **~700–925 hrs** | **~14–18 months** |

---

## What Your Portfolio Looks Like When Done

| Project | Track | What it shows |
|---|---|---|
| Document intelligence pipeline | T1 | Structured extraction, batch processing, production error handling |
| AI coding / writing copilot | T1 | Context management, UX thinking, streaming |
| RAG system with eval harness | T2+T4 | You can measure quality, not just build |
| Autonomous research agent | T3 | Multi-step reasoning, tool use, reliability |
| Fine-tuned embedding + LLM | T5 | You understand what's inside, not just the API |
| Fraud detection deployed API | T7+T6 | Classical ML + production deployment |
| Full MLOps pipeline for one of the above | T6 | CI/CD, Docker, monitoring — you can ship |

This portfolio answers the implicit question in every AI engineering interview: *can this person build something that actually works, or just something that sometimes works in a demo?*

---

## The 5 Things That Separate Good AI Engineers from the Rest

1. **They measure before they optimise.** An eval harness before changing anything — ever.

2. **They know when not to use LLMs.** A regex, a database query, or a classical classifier is faster, cheaper, and more reliable for many problems. Reaching for an LLM first is a smell.

3. **They understand failure modes.** They can debug a RAG system returning wrong answers, an agent stuck in a loop, or a model that was trained on the wrong data format — because they've seen these failures and know what causes them.

4. **They think about cost.** Token usage, API costs, caching strategies, model selection. AI in production is expensive and cost awareness is a professional signal.

5. **They ship.** A deployed, documented, evaluated project beats 10 half-built ones. The last 20% — error handling, monitoring, documentation, deployment — is where the craft lives.

---

*The foundation is small. Build it fast. Then build things. The understanding follows the building — not the other way around.*