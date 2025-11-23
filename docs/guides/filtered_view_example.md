# Filtered View Example: Ingredient Aggregation

This guide demonstrates how to use the **Heading Extraction Query** to create an aggregated view of content from multiple notes.

## Scenario

You have a collection of TCM formula notes, each tagged with `#formula`. Each note has an `## Ingredients` section listing the herbs used. You want a single dashboard view that lists all formulas and their ingredients.

## The Query

Using the `build_heading_extraction_query` function from `capsule.utils.dataview_queries`, you can generate the following DataviewJS query:

```dataviewjs
function extractHeading(content, heading) {
    // Escape special regex characters in heading
    const escapedHeading = heading.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const regex = new RegExp(`^#+\\s+${escapedHeading}\\s*\\n([\\s\\S]*?)(?=\\n#+|$)`, 'm');
    const match = content.match(regex);
    return match ? match[1].trim() : null;
}

const notes = dv.pages('#formula');

// Performance warning for large datasets
if (notes.length > 50) {
    dv.paragraph("⚠️ **Performance Warning**: Processing " + notes.length + " notes. This extraction requires reading file contents and may be slow.");
}

const results = [];

for (let note of notes) {
  const content = await dv.io.load(note.file.path);
  const headingContent = extractHeading(content, "Ingredients");
  if (headingContent) {
    results.push({
      name: note.file.name,
      content: headingContent
    });
  }
}

dv.table(["Note", "Ingredients"], 
  results.map(r => [r.name, r.content]));
```

## Sample Output

| Note | Ingredients |
|------|-------------|
| Ba Zhen Tang | Dang Gui, Chuan Xiong, Bai Shao, Shu Di Huang, Ren Shen, Bai Zhu, Fu Ling, Gan Cao |
| Si Jun Zi Tang | Ren Shen, Bai Zhu, Fu Ling, Gan Cao |

## Usage in Templates

You can include this query in your dashboard templates using Jinja2:

```jinja2
## All Formula Ingredients

{{ build_heading_extraction_query("#formula", "Ingredients") }}
```
