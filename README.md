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

Changes are deployed to production automatically after pushing to the main branch.

## How to Create a Blog Post

Follow these steps to create a new blog post:

### Step 1: Create the Blog Post File

1. Navigate to the `blog/` directory
2. Create a new folder with the date in `YYYY-MM-DD` format (e.g., `2025-11-05`)
3. Create an `MDX` file inside that folder with the same date format (e.g., `2025-11-05.mdx`)

**Example:**
```
blog/
  └── 2025-11-05/
      └── 2025-11-05.mdx
```

### Step 2: Add Frontmatter

At the top of your MDX file, add the frontmatter with the required metadata:

```mdx
---
title: 'Your Blog Post Title Here'
sidebarTitle: 'Your Blog Post Title Here'
description: A brief description of your blog post.
---
```

**Fields:**
- `title`: The title of your blog post (required)
- `sidebarTitle`: The title displayed in the sidebar navigation (required - should match `title`)
- `description`: A short description for SEO and previews (optional)


**Important:** The `sidebarTitle` field is required for production builds. Without it, blog post titles may not display correctly in the sidebar menu. Always set `sidebarTitle` to match your `title` field.

### Step 3: Add Date and Author Information

After the frontmatter, add the date and author JSX components:

```mdx
<div style={{ marginBottom: '1rem', color: '#666', fontSize: '0.9rem' }}>November 5, 2025</div>

<div style={{ display: 'flex', alignItems: 'center', gap: '1rem'}}>
  <img src="/images/SebastianGitHub.jpeg" alt="Sebastian Lim" style={{ width: '50px', height: '50px', borderRadius: '50%', margin: '0' }} />
  <div style={{ display: 'flex', flexDirection: 'column' }}>
    <span style={{ color: '#4063FF' }}><strong>Author:</strong> <a href="https://github.com/slim115" target="_blank" rel="noopener noreferrer" style={{ color: '#4063FF', textDecoration: 'none' }} onMouseOver={(e) => e.target.style.textDecoration = 'underline'} onMouseOut={(e) => e.target.style.textDecoration = 'none'}>Sebastian Lim</a></span>
    <span style={{ fontSize: '0.85rem', color: '#666', marginTop: '0.25rem' }}>SCS@HashDit</span>
  </div>
</div>
```

**Note:** Update the date, image path, GitHub link, and author name as needed.

### Step 4: Write Your Content

Write your blog post content using Markdown/MDX. Remember the formatting quirks:

- **Line breaks**: Wrap paragraphs in `<p>` tags
- **Dollar signs**: Escape with `\$` (e.g., `\$2.1 million`)
- **Images**: Use relative paths like `![Alt text](./image.png)`

### Step 5: Add to Navigation

Add your new blog post to `docs.json` in the "Latest Posts" section:

1. Open `docs.json`
2. Find the `"Latest Posts"` group under the `"Blog"` tab
3. Add your blog post path at the top of the pages array:

```json
{
  "group": "Latest Posts",
  "pages": [
    "blog/2025-11-05/2025-11-05",
    // ... other blog posts
  ]
}
```

**Important:** Add new posts at the top of the list (most recent first).

### Step 6: Preview Locally

Run `mint dev` to preview your blog post locally at `http://localhost:3000`.

### Step 7: Commit and Push

Once you're satisfied with your blog post:

1. Commit your changes
2. Push to the default branch
3. Mintlify will automatically deploy the changes to production

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

Blog post titles are defined in the frontmatter at the top of the file. You must include both `title` and `sidebarTitle` fields:

```mdx
---
title: 'PancakeSwap October 26th Weekly Security Report'
sidebarTitle: 'PancakeSwap October 26th Weekly Security Report'
---
```

**Note:** The `sidebarTitle` field is required for production builds to ensure titles display correctly in the sidebar navigation. Always set it to match your `title` field.

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
