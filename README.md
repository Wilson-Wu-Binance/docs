# HashDit Documentation

This repository contains the HashDit API documentation and blog, built with [Mintlify](https://mintlify.com/).

## What is Mintlify?

Mintlify is a documentation platform that makes it easy to create beautiful, interactive documentation sites. It uses Markdown (MDX) files to generate documentation with features like:

- Automatic API reference generation from OpenAPI specs
- Interactive code examples
- Search functionality
- Customizable themes
- Blog support

## Running Locally

To preview your documentation changes locally, you'll need to install the Mintlify CLI:

```bash
npm i -g mint
```

Then, run the following command at the root of this repository (where `docs.json` is located):

```bash
mint dev
```

Your local preview will be available at `http://localhost:3000`.


### Troubleshooting

- If your dev environment isn't running: Run `mint update` to ensure you have the most recent version of the CLI.
- If a page loads as a 404: Make sure you are running in a folder with a valid `docs.json`.

## Publishing Changes

Install the GitHub app from your [dashboard](https://dashboard.mintlify.com/settings/organization/github-app) to propagate changes from your repo to your deployment. Changes are deployed to production automatically after pushing to the default branch.

## Mintlify Quirks & Formatting Notes

When writing content for Mintlify, there are a few important quirks to keep in mind:

### Line Breaks

To put text on a new line, you must wrap it in a `<p>` tag. Regular line breaks in Markdown won't create new paragraphs.

**Example:**
```mdx
<p>This is the first paragraph.</p>
<p>This is on a new line.</p>
```

### Dollar Sign Escaping

The dollar sign (`$`) must be escaped with a backslash (`\$`) because of parsing issues.

**Example:**
```mdx
The user lost \$2.1 million in the attack.
```

### Blog Post Title Format

Blog post titles are defined in the frontmatter at the top of the file:

```mdx
---
title: 'PancakeSwap October 26th Weekly Security Report'
---
```

### Blog Post Date and Author Format

The date and author information for blog posts uses JSX components:

```mdx
<div style={{ marginBottom: '1rem', color: '#666', fontSize: '0.9rem' }}>October 26, 2023</div>

<div style={{ display: 'flex', alignItems: 'center', gap: '1rem'}}>
  <img src="/images/SebastianGitHub.jpeg" alt="Sebastian Lim" style={{ width: '50px', height: '50px', borderRadius: '50%', margin: '0' }} />
  <div style={{ display: 'flex', flexDirection: 'column' }}>
    <span style={{ color: '#4063FF' }}><strong>Author:</strong> <a href="https://github.com/slim115" target="_blank" rel="noopener noreferrer" style={{ color: '#4063FF', textDecoration: 'none' }} onMouseOver={(e) => e.target.style.textDecoration = 'underline'} onMouseOut={(e) => e.target.style.textDecoration = 'none'}>Sebastian Lim</a></span>
    <span style={{ fontSize: '0.85rem', color: '#666', marginTop: '0.25rem' }}>SCS@HashDit</span>
  </div>
</div>
```

## Resources

- [Mintlify documentation](https://mintlify.com/docs)
- [Mintlify quickstart guide](https://starter.mintlify.com/quickstart)
