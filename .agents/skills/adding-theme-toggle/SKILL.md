---
name: adding-theme-toggle
description: Adds a dark/light theme toggle to an existing static HTML page — inline FOUC-prevention script, CSS variable refactor, sun/moon SVG button, localStorage persistence, prefers-color-scheme sync. Use when the user wants dark mode, light mode, theme switcher, ใส่ธีมมืด/สว่าง, or to convert a single-mode page to dual-mode. Even applies when the user describes the symptom ("the site is too bright") rather than naming "theme".
license: Apache-2.0
compatibility: Vanilla HTML/CSS/JS — no framework. Works in all modern browsers.
metadata:
  author: supachai-j
  version: "1.0"
allowed-tools: Read Edit Write Grep
---

# Adding a dark/light theme toggle

The same drop-in pattern used across `supachai-j.github.io`,
`agent-skills-training`, and `course-portal-template`. Three pieces to add,
no FOUC.

## When to use

Trigger when:
- User wants "dark mode", "light mode", "theme toggle", "theme switcher"
- User says "make it switchable" / "responsive to system theme"
- User reports site is too bright/dark (likely wants a toggle)
- A static HTML page currently has hardcoded colours

Don't use for:
- Sites already using Tailwind/Material/styled-components — they have their own theming
- Sites with JS frameworks (React, Vue) — they need framework-specific patterns

## The three drop-ins

### 1. Inline bootstrap script (in `<head>`, before stylesheet)

Prevents the flash of wrong theme when the page first renders.

```html
<script>
  (function() {
    try {
      var stored = localStorage.getItem('theme');
      var theme = stored || (window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
      document.documentElement.dataset.theme = theme;
    } catch (e) { document.documentElement.dataset.theme = 'dark'; }
  })();
</script>
```

Bundled at [`assets/theme-bootstrap.html`](assets/theme-bootstrap.html).

### 2. CSS variable blocks (in `<style>`)

Replace the existing `:root { ... }` block:

```css
:root, [data-theme="dark"] {
  --bg: #0b0d12;
  --panel: #161922;
  --accent: #d97757;
  --text: #e8ecf2;
  --muted: #8a93a3;
  --border: rgba(255,255,255,0.06);
  --soft-1: rgba(255,255,255,0.04);
  /* ... all your dark-mode tokens ... */
}
[data-theme="light"] {
  --bg: #fafbfc;
  --panel: #ffffff;
  --accent: #c95a30;
  --text: #1a1d27;
  --muted: #58607a;
  --border: rgba(0,0,0,0.08);
  --soft-1: rgba(0,0,0,0.03);
  /* ... mirror tokens for light ... */
}
```

Full palette at [`assets/theme-vars.css`](assets/theme-vars.css). Then replace
every hardcoded colour in your CSS with `var(--token)`.

### 3. Toggle button (in nav or header)

```html
<button class="theme-toggle" id="theme-toggle" type="button"
        aria-label="Toggle dark/light theme" title="Toggle theme">
  <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor"
       stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="12" cy="12" r="4"/>
    <path d="M12 2v2"/><path d="M12 20v2"/>
    <path d="m4.93 4.93 1.41 1.41"/><path d="m17.66 17.66 1.41 1.41"/>
    <path d="M2 12h2"/><path d="M20 12h2"/>
    <path d="m4.93 19.07 1.41-1.41"/><path d="m17.66 6.34 1.41-1.41"/>
  </svg>
  <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor"
       stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>
  </svg>
</button>
```

CSS for the button:

```css
.theme-toggle {
  background: var(--soft-1); border: 1px solid var(--border);
  color: var(--muted); width: 34px; height: 34px;
  border-radius: 8px; display: inline-grid; place-items: center;
  cursor: pointer; padding: 0;
  transition: background-color .15s, color .15s, border-color .15s;
}
.theme-toggle:hover { background: var(--soft-2); color: var(--text); }
.theme-toggle svg { width: 16px; height: 16px; display: block; }
.theme-toggle .icon-moon { display: none; }
[data-theme="light"] .theme-toggle .icon-sun { display: none; }
[data-theme="light"] .theme-toggle .icon-moon { display: block; }
```

Full button + CSS at [`assets/theme-toggle-button.html`](assets/theme-toggle-button.html).

### 4. Click handler (before `</body>`)

```html
<script>
  (function() {
    var btn = document.getElementById('theme-toggle');
    if (!btn) return;
    btn.addEventListener('click', function() {
      var current = document.documentElement.dataset.theme || 'dark';
      var next = current === 'light' ? 'dark' : 'light';
      document.documentElement.dataset.theme = next;
      try { localStorage.setItem('theme', next); } catch (e) {}
    });
    var mq = window.matchMedia('(prefers-color-scheme: light)');
    if (mq.addEventListener) {
      mq.addEventListener('change', function(e) {
        if (!localStorage.getItem('theme')) {
          document.documentElement.dataset.theme = e.matches ? 'light' : 'dark';
        }
      });
    }
  })();
</script>
```

## Step-by-step workflow

1. **Audit hardcoded colours.** Run:

   ```bash
   grep -nE '#[0-9a-fA-F]{3,6}|rgba?\(' your-page.html | head -50
   ```

   Group them: text, bg, border, accent. These become CSS variables.

2. **Add `:root` + `[data-theme="light"]`** blocks at top of `<style>`. Define
   one variable per role.

3. **Replace hardcoded values** with `var(--token)` throughout the rest of CSS.

4. **Add inline bootstrap script** in `<head>` right after `<title>`,
   **before** `<link rel="stylesheet">`.

5. **Add toggle button** in nav/header. Wire the click handler script before `</body>`.

6. **Add `<meta name="theme-color">`** for browser chrome:

   ```html
   <meta name="theme-color" content="#0b0d12" media="(prefers-color-scheme: dark)" />
   <meta name="theme-color" content="#fafbfc" media="(prefers-color-scheme: light)" />
   ```

7. **Add transitions** on `body` so colour changes feel smooth:

   ```css
   body { transition: background-color .25s ease, color .25s ease; }
   ```

8. **Test both modes** by clicking the toggle, scrolling every section,
   refreshing to verify localStorage persistence.

## Anti-patterns

- ❌ **Forgetting the inline bootstrap script** → site flashes dark before
  switching to light. Inline `<script>` runs before stylesheet, before paint.
- ❌ **Hardcoding `color: white` somewhere deep** in CSS → looks fine in dark,
  invisible in light. Always grep before saying "done".
- ❌ **Using `prefers-color-scheme` media queries** instead of CSS variables →
  works for system preference but breaks user override. Use `data-theme`
  attribute as the source of truth.
- ❌ **localStorage but no system sync** → users who never click the button
  but switch their OS theme expect the site to follow.
- ❌ **One `--accent` for both modes** → orange `#d97757` works on dark but is
  too light on white. Use a darker accent (`#c95a30`) for light mode.

## Multi-page sites

For a multi-page site (course portal, blog), put the bootstrap script + click
handler in **every page**. Use the same `localStorage` key so a toggle on one
page persists across navigation.

The CSS vars and toggle button can either be inlined per-page (current
pattern) or moved to a shared external CSS file (better for ~5+ pages).

## Final checklist

- [ ] Inline FOUC-prevention script in `<head>`
- [ ] `:root` + `[data-theme="light"]` blocks define every colour token
- [ ] No hardcoded `#hex` or `rgba()` outside the variable blocks
- [ ] Toggle button in nav with sun/moon SVGs
- [ ] Click handler persists to `localStorage`
- [ ] Live-syncs to `prefers-color-scheme` when user hasn't manually toggled
- [ ] `<meta name="theme-color">` for browser chrome
- [ ] Transitions on `body` for smooth switch
- [ ] Tested both modes by scrolling every section

## Related skills

- [`scaffolding-course-portal`](../scaffolding-course-portal/SKILL.md) — calls this in Phase 9
- [`generating-reveal-deck`](../generating-reveal-deck/SKILL.md) — slides usually skip the toggle (presented in fixed lighting)

## Bundled assets

- [`assets/theme-bootstrap.html`](assets/theme-bootstrap.html) — head script
- [`assets/theme-toggle-button.html`](assets/theme-toggle-button.html) — button + CSS
- [`assets/theme-vars.css`](assets/theme-vars.css) — full palette for both modes
- [`references/COLOR-PALETTE.md`](references/COLOR-PALETTE.md) — palette rationale + alternatives
