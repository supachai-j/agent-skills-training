# Slide patterns

The seven patterns that cover ~95% of training slides. Copy the snippet,
adjust content. Don't invent new patterns until you've used these all.

## 1. Title slide

```html
<section class="center">
  <h1>Course Name</h1>
  <h3 style="color: #ddd">Subtitle / tagline</h3>
  <p class="muted">v1 · YYYY-MM-DD · author</p>
  <p><span class="pill">EN</span><span class="pill">also in ภาษาไทย</span></p>
</section>
```

## 2. Agenda

```html
<section>
  <h2>What we'll cover</h2>
  <ol>
    <li>Topic one</li>
    <li>Topic two</li>
    <li>Topic three</li>
    <li>Topic four</li>
  </ol>
  <p class="muted">By the end you should be able to ____.</p>
</section>
```

Cap at 6 items.

## 3. Definition

```html
<section>
  <h2>What is X?</h2>
  <p class="big">
    X is a <em>folder</em> of instructions that an agent can
    <strong>discover and load dynamically</strong>.
  </p>
  <ul>
    <li>Key fact 1</li>
    <li>Key fact 2</li>
    <li>Key fact 3</li>
  </ul>
</section>
```

## 4. Comparison table

```html
<section>
  <h2>Skills vs MCP vs Subagents</h2>
  <table>
    <tr><th></th><th>Skills</th><th>MCP</th><th>Subagents</th></tr>
    <tr><td>Purpose</td><td>How</td><td>Access</td><td>Delegate</td></tr>
    <tr><td>Includes code</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
  </table>
</section>
```

Max 5 columns × 5 data rows. If you need more, split into two tables.

## 5. Code example

```html
<section>
  <h2>SKILL.md — minimal example</h2>
<pre><code class="language-yaml">---
name: pdf-processing
description: Extract text from PDFs. Use when working with PDF files.
---

# PDF Processing
Use pdfplumber for text extraction.</code></pre>
  <p class="muted">Required: <code>name</code>, <code>description</code>.</p>
</section>
```

Max 15 lines of code.

## 6. Quote / takeaway

```html
<section>
  <h2>The principle</h2>
  <p class="quote">
    "Building a skill for an agent is like putting together
    an onboarding guide for a new hire."
  </p>
  <p class="muted">— Anthropic Engineering, 2025</p>
</section>
```

## 7. Two-column comparison

```html
<section>
  <h2>Before / After</h2>
  <div class="grid2">
    <div class="card">
      <h3>Before</h3>
      <ul>
        <li>Pain point 1</li>
        <li>Pain point 2</li>
      </ul>
    </div>
    <div class="card">
      <h3>After</h3>
      <ul>
        <li>Improvement 1</li>
        <li>Improvement 2</li>
      </ul>
    </div>
  </div>
</section>
```

## 8. Q&A close

```html
<section class="center">
  <h1>Questions?</h1>
  <p class="muted">course-name · author</p>
</section>
```
